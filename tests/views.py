# tests/views.py - Updated with comprehensive test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import logging

from .models import TestCategory, TestQuestion, TestResult, UserAnswer, Question, Choice
from .question_bank import COMPREHENSIVE_QUESTIONS, get_all_categories
from advisor.ai_service import AIAdvisor

logger = logging.getLogger(__name__)


@login_required
def personality_test_view(request):
    """Display the comprehensive personality test - 10 random questions"""
    
    import random
    
    # Select 10 random questions from all available questions
    all_questions = COMPREHENSIVE_QUESTIONS
    selected_questions = random.sample(all_questions, min(10, len(all_questions)))
    
    context = {
        'questions_json': json.dumps(selected_questions, ensure_ascii=False),
        'total_questions': len(selected_questions)
    }
    
    return render(request, 'tests/personality_test.html', context)


@login_required
def submit_test_view(request):
    """Receive and analyze test answers"""
    
    # Detailed logging to help with diagnosis
    import os
    debug_log_path = os.path.join(os.path.dirname(__file__), 'debug_submit.log')
    with open(debug_log_path, 'a', encoding='utf-8') as f:
        f.write(f"\n{'='*50}\n")
        f.write(f"TIME: {request.user.username} attempt\n")
        f.write(f"Method: {request.method}\n")
        f.write(f"Content-Type: {request.content_type}\n")
        f.write(f"Body length: {len(request.body) if request.body else 0}\n")
    
    if request.method != 'POST':
        return redirect('tests:personality_test')
    
    try:
        answers_data = {}
        
        # 1. Try reading from JSON body
        if request.body:
            try:
                body_unicode = request.body.decode('utf-8')
                with open(debug_log_path, 'a', encoding='utf-8') as f:
                    f.write(f"Body snippet: {body_unicode[:500]}\n")
                
                body_data = json.loads(body_unicode)
                
                # Check if data contains answers directly
                for key, value in body_data.items():
                    if key.startswith('answer_'):
                        answers_data[key] = value
                
                with open(debug_log_path, 'a', encoding='utf-8') as f:
                    f.write(f"Parsed from body: {len(answers_data)} answers\n")
            except Exception as e:
                with open(debug_log_path, 'a', encoding='utf-8') as f:
                    f.write(f"JSON body parsing failed: {e}\n")

        # 2. Try from request.POST (Form Data - for compatibility with old and new test)
        if not answers_data and request.POST:
            for key, value in request.POST.items():
                # Support new format: answer_X
                if key.startswith('answer_'):
                    try:
                        answers_data[key] = json.loads(value)
                    except:
                        answers_data[key] = value
                
                # Support old format: question_X (for compatibility)
                elif key.startswith('question_'):
                    # Convert old format to new
                    question_index = key.replace('question_', '')
                    choice_id = value
                    
                    # Create data in similar format to the new format
                    answers_data[f'answer_{question_index}'] = {
                        'question_id': question_index,
                        'question_text': f'Question {question_index}',
                        'choice_index': choice_id,
                        'choice_text': f'Choice {choice_id}',
                        'traits': 'analytical',  # default value
                        'value': 5,  # default average value
                        'category': 'general'
                    }
            
            with open(debug_log_path, 'a', encoding='utf-8') as f:
                f.write(f"Parsed from POST: {len(answers_data)} answers\n")
        
        if not answers_data:
            with open(debug_log_path, 'a', encoding='utf-8') as f:
                f.write("ERROR: No answers data found\n")
            return JsonResponse({
                'success': False,
                'error': 'No answers were received or the format is incorrect. Please make sure to answer all questions.'
            }, status=400)
        
        # Analyze the answers
        analysis_result = analyze_test_answers_v2(request.user, answers_data)
        
        # Save the results
        test_result = save_test_results_v2(request.user, answers_data, analysis_result)
        
        with open(debug_log_path, 'a', encoding='utf-8') as f:
            f.write(f"SUCCESS: Result ID {test_result.id}\n")
        
        return JsonResponse({
            'success': True,
            'redirect_url': f"/tests/results/{test_result.id}/"
        })
    
    except Exception as e:
        import traceback
        error_msg = traceback.format_exc()
        with open(debug_log_path, 'a', encoding='utf-8') as f:
            f.write(f"CRITICAL ERROR: {e}\n{error_msg}\n")
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)


def map_trait_to_arabic(trait_en):
    """Map a trait from English to internal key"""
    mapping = {
        'analytical': 'analytical',
        'creative': 'creative',
        'social': 'social',
        'organized': 'organized',
        'practical': 'practical'
    }
    return mapping.get(trait_en.lower(), trait_en)


def analyze_test_answers_v2(user, answers_data):
    """Analyze answers using data sent directly from the frontend"""
    
    personality_scores = {
        'analytical': 0, 'creative': 0, 'social': 0, 'organized': 0, 'practical': 0
    }
    trait_counts = {trait: 0 for trait in personality_scores.keys()}
    
    for key, data in answers_data.items():
        value = data.get('value', 0)
        traits_str = data.get('traits', '')
        traits = [t.strip() for t in traits_str.split(',') if t.strip()]
        
        for trait in traits:
            trait_key = map_trait_to_arabic(trait)
            if trait_key in personality_scores:
                personality_scores[trait_key] += value
                trait_counts[trait_key] += 1
    
    # Calculate the average
    for trait in personality_scores.keys():
        if trait_counts[trait] > 0:
            personality_scores[trait] = personality_scores[trait] / trait_counts[trait]
    
    # Get major recommendations
    ai_advisor = AIAdvisor()
    full_result = ai_advisor.analyze_user_profile({
        'personality_scores': personality_scores,
        'interests': {}
    })
    
    return full_result


def save_test_results_v2(user, answers_data, analysis_result):
    """Save results compatible with the new data format"""
    
    try:
        # Get the test category
        category, _ = TestCategory.objects.get_or_create(
            name='Personality Test',
            defaults={'description': 'A comprehensive personality and career interest assessment test'}
        )
        
        # Extract data for the summary
        personality_analysis = analysis_result.get('personality_analysis', {})
        recommendations = analysis_result.get('recommendations', [])
        
        # Calculate score (avg personality scores * 10 to scale to 100)
        scores = personality_analysis.get('scores', personality_analysis.get('dominant_traits', {}))
        if not scores and 'personality_scores' in analysis_result:
             scores = analysis_result['personality_scores']
             
        avg_score = sum(scores.values()) / len(scores) if scores else 0
        total_score = min(100, int(avg_score * 10))
        
        # Result summary
        result_summary = f"Personality Type: {personality_analysis.get('personality_type', 'Balanced')}\n\n"
        
        strengths = personality_analysis.get('strengths', [])
        if strengths:
            result_summary += f"Strengths: {', '.join(strengths[:3])}\n\n"
        
        rec_names = [r.get('major_name', r.get('name', '')) for r in recommendations[:5]]
        result_summary += f"Recommendations: {', '.join([n for n in rec_names if n])}"
        
        recommended_majors = ', '.join([n for n in rec_names if n])
        
        # Create the result record
        test_result = TestResult.objects.create(
            user=user,
            test_category=category,
            score=total_score,
            result_summary=result_summary,
            recommended_majors=recommended_majors
        )
        
        # Save detailed answers to the database
        for key, data in answers_data.items():
            try:
                question_text = data.get('question_text', f"Question {data.get('question_id')}")
                selected_choice = data.get('choice_text', '')
                choice_index = data.get('choice_index', '')
                
                # Create answer record
                UserAnswer.objects.create(
                    user=user,
                    test_result=test_result,
                    question_text=question_text,
                    selected_choice=selected_choice,
                    answer=str(choice_index)[:1]
                )
                
            except Exception as e:
                logger.warning(f"Could not save answer for question: {e}")
                
        logger.info(f"Test result and {len(answers_data)} answers saved for user {user.username}: ID {test_result.id}")
        return test_result
        
    except Exception as e:
        logger.error(f"Error in save_test_results_v2: {e}")
        raise


def map_category_to_english(category_en):
    """Map category from internal key to English label"""
    mapping = {
        'personality': 'Personality',
        'skills': 'Skills',
        'academic': 'Academic',
        'goals': 'Goals'
    }
    return mapping.get(category_en, category_en)


@login_required
def test_results_view(request, result_id):
    """Display test results"""
    
    test_result = get_object_or_404(TestResult, id=result_id, user=request.user)
    
    # Parse recommendations
    try:
        if test_result.recommended_majors:
            # If JSON
            if test_result.recommended_majors.startswith('{') or test_result.recommended_majors.startswith('['):
                recommended_data = json.loads(test_result.recommended_majors)
                recommended_majors_list = recommended_data.get('majors', [])
            else:
                # If plain text separated by commas
                recommended_majors_list = [m.strip() for m in test_result.recommended_majors.split(',') if m.strip()]
        else:
            recommended_majors_list = []
    except Exception as e:
        logger.warning(f"Error parsing recommended majors: {e}")
        recommended_majors_list = []
    
    context = {
        'result': test_result,
        'recommended_majors': recommended_majors_list
    }
    
    return render(request, 'tests/results.html', context)


# ===== Views for the old test (for compatibility) =====

@login_required
def test_view(request):
    """Redirect to the new comprehensive test"""
    return redirect('tests:personality_test')