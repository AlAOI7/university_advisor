# advisor/ai_service.py
"""
Main AI Service - University Advisor System
Orchestrates between Google Gemini (primary) and RuleBasedAI (secondary/fallback).
"""

import logging
from typing import Dict, List

from majors.models import Major
from .gemini_service import GeminiService
from .rule_based_ai import RuleBasedAI

logger = logging.getLogger(__name__)


class AIAdvisor:
    """
    Dual-engine AI advisor:
    - Primary: Google Gemini Pro (when API key is configured)
    - Secondary: RuleBasedAI (always available, no API needed)
    """

    def __init__(self):
        self.gemini = GeminiService()
        self.rule_ai = RuleBasedAI()

    # ------------------------------------------------------------------
    # Main Analysis
    # ------------------------------------------------------------------

    def analyze_user_profile(self, user_data: Dict) -> Dict:
        """
        Full user profile analysis and major recommendation.
        Tries Gemini first, falls back to RuleBasedAI automatically.
        """
        # ---- Attempt Gemini ----
        if self.gemini.is_configured:
            try:
                gemini_analysis = self.gemini.analyze_test_results(user_data)
                interests = gemini_analysis.get('interests', [])
                interests_with_scores = [(interest, 1.0) for interest in interests]

                gemini_recommendations = self.gemini.recommend_majors(gemini_analysis, interests)
                matched_majors = [
                    {
                        'name': rec.get('major_name', rec.get('name', '')),
                        'match_percentage': rec.get('match_percentage', 75),
                        'reasons': rec.get('reasons', []),
                        'required_skills': rec.get('required_skills', []),
                        'career_opportunities': rec.get('career_opportunities', [])
                    }
                    for rec in gemini_recommendations[:5]
                ]

                return {
                    'personality_analysis': {
                        'personality_type': gemini_analysis.get('personality_type', 'Balanced'),
                        'strengths': gemini_analysis.get('strengths', []),
                        'learning_style': gemini_analysis.get('learning_style', ''),
                        'suitable_environment': gemini_analysis.get('suitable_environment', ''),
                    },
                    'interest_analysis': {
                        'top_interests': interests_with_scores,
                        'suitable_environment': gemini_analysis.get('suitable_environment', ''),
                    },
                    'recommendations': matched_majors,
                    'suggested_skills': self.rule_ai._suggest_skills(
                        gemini_analysis.get('personality_type', ''), 'arabic'
                    ),
                    'ai_powered': True,
                    'model': 'Google Gemini Pro',
                }
            except Exception as e:
                logger.error(f"Gemini analysis failed: {e}. Falling back to RuleBasedAI.")

        # ---- Fallback: RuleBasedAI ----
        result = self.rule_ai.analyze(user_data)

        # Also enrich with database majors if available
        db_majors = self._find_db_majors(user_data)
        if db_majors:
            result['db_recommendations'] = db_majors

        return result

    # ------------------------------------------------------------------
    # Chat Interface
    # ------------------------------------------------------------------

    def get_chat_response(self, message: str, context: Dict = None) -> Dict:
        """
        Get a chat response. Uses Gemini if available, else RuleBasedAI.
        """
        if self.gemini.is_configured:
            try:
                response_text = self.gemini.chat_response(message, context)
                return {
                    'response': response_text,
                    'ai_powered': True,
                    'model': 'Google Gemini Pro',
                }
            except Exception as e:
                logger.error(f"Gemini chat failed: {e}.")

        # Fallback
        response_text = self.rule_ai.chat(message)
        return {
            'response': response_text,
            'ai_powered': False,
            'model': 'RuleBasedAI v2.0',
        }

    # ------------------------------------------------------------------
    # Database Major Matching (helper)
    # ------------------------------------------------------------------

    def _find_db_majors(self, user_data: Dict) -> List[Dict]:
        """Query the database for majors matching the user's profile."""
        try:
            personality_scores = user_data.get('personality_scores', {})
            interests_data = user_data.get('interests', {})

            traits = list(personality_scores.items())
            interests_list = [k for k, v in interests_data.items() if v > 5]

            majors = Major.objects.all()
            matched = []

            for major in majors:
                score = 0
                major_text = (major.description or '') + ' ' + (major.job_opportunities or '')

                for interest in interests_list:
                    if interest in major_text:
                        score += 2

                for trait, val in traits:
                    if trait in major_text:
                        score += val * 0.5

                if score >= 2:
                    matched.append({
                        'name': major.name,
                        'match_percentage': min(int(50 + score * 5), 95),
                        'description': major.description,
                        'id': major.id,
                    })

            matched.sort(key=lambda x: x['match_percentage'], reverse=True)
            return matched[:5]
        except Exception as e:
            logger.warning(f"DB major search failed: {e}")
            return []

    # ------------------------------------------------------------------
    # Convenience Wrappers (backward compatibility)
    # ------------------------------------------------------------------

    def find_matching_majors(self, traits, interests, preferences):
        """Legacy method — delegates to RuleBasedAI."""
        user_data = {
            'personality_scores': dict(traits) if isinstance(traits, list) else traits,
            'interests': dict(interests) if isinstance(interests, list) else interests,
            'academic_preferences': preferences,
        }
        return self._find_db_majors(user_data)

    def calculate_match_score(self, major, traits, interests):
        """Simple score for a given major object."""
        base = 50
        major_text = (major.description or '') + ' ' + (major.job_opportunities or '')
        for trait, val in (traits.items() if isinstance(traits, dict) else traits):
            if trait in major_text:
                base += val * 3
        for interest, val in (interests.items() if isinstance(interests, dict) else interests):
            if interest in major_text:
                base += val * 2
        return min(int(base), 98)

    def suggest_skills_to_develop(self, traits, interests):
        """Suggest development skills."""
        personality_type = ''
        if traits:
            best = max(traits, key=lambda x: x[1]) if isinstance(traits, list) else max(traits, key=traits.get)
            personality_type = best[0] if isinstance(best, tuple) else best
        return self.rule_ai._suggest_skills(personality_type, 'arabic')