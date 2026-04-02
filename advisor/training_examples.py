# advisor/training_examples.py
"""
Bilingual Training Examples for AI Model - Arabic & English
Few-Shot Learning examples for personality analysis and major recommendation
"""

# ============================================
# Arabic Personality Analysis Examples
# ============================================

ARABIC_PERSONALITY_EXAMPLES = [
    # 1 - Analytical
    {
        "input": {
            "personality_scores": {"تحليلي": 9, "إبداعي": 3, "اجتماعي": 2, "تنظيمي": 7, "عملي": 5},
            "interests": {"العلوم": 8, "التكنولوجيا": 9, "الهندسة": 7, "الرياضيات": 8, "الطب": 2}
        },
        "output": {
            "personality_type": "تحليلي",
            "strengths": ["التفكير المنطقي والنقدي", "حل المشكلات المعقدة", "تحليل البيانات بدقة", "التركيز العالي", "مهارات رياضية قوية"],
            "interests": ["العلوم", "التكنولوجيا", "الرياضيات"],
            "recommended_majors": [
                {"name": "علوم الحاسب", "match_percentage": 95, "reasons": ["يتطلب تفكير تحليلي", "يناسب محبي التكنولوجيا", "فرص عمل واسعة"]},
                {"name": "هندسة البرمجيات", "match_percentage": 92, "reasons": ["يجمع التحليل والتطبيق", "منظم وهيكلي", "مطلوب في سوق العمل"]},
                {"name": "الذكاء الاصطناعي", "match_percentage": 90, "reasons": ["يحتاج تفكير رياضي", "مجال مستقبلي", "راوتب مرتفعة"]},
                {"name": "الإحصاء", "match_percentage": 85, "reasons": ["يناسب الشخصية التحليلية", "مطلوب في كل الصناعات", "أساس علمي قوي"]},
                {"name": "هندسة الشبكات", "match_percentage": 80, "reasons": ["يجمع التقنية والتحليل", "بنية تحتية حيوية", "تطور مستمر"]}
            ]
        }
    },
    # 2 - Creative
    {
        "input": {
            "personality_scores": {"تحليلي": 4, "إبداعي": 9, "اجتماعي": 7, "تنظيمي": 3, "عملي": 5},
            "interests": {"الفنون": 9, "التصميم": 8, "الإعلام": 7, "الأدب": 6, "التكنولوجيا": 5}
        },
        "output": {
            "personality_type": "إبداعي",
            "strengths": ["التفكير الإبداعي", "التعبير الفني", "التواصل الاجتماعي", "رؤية مبتكرة", "العمل في بيئات ديناميكية"],
            "interests": ["الفنون", "التصميم", "الإعلام"],
            "recommended_majors": [
                {"name": "التصميم الجرافيكي", "match_percentage": 93, "reasons": ["إبداع وخيال", "يجمع الفن والتقنية", "فرص عمل متنوعة"]},
                {"name": "الإعلام الرقمي", "match_percentage": 88, "reasons": ["مجال متطور", "يناسب الإبداعيين الاجتماعيين", "تعبير حر"]},
                {"name": "العمارة والتصميم الداخلي", "match_percentage": 85, "reasons": ["إبداع وتطبيق عملي", "تأثير ملموس", "متعدد التخصصات"]},
                {"name": "الأدب والترجمة", "match_percentage": 80, "reasons": ["يناسب محبي الكلمات", "مجال واسع الثقافة", "الترجمة مطلوبة"]},
                {"name": "تصميم الأزياء", "match_percentage": 77, "reasons": ["إبداع تطبيقي", "صناعة مزدهرة", "تعبير شخصي"]}
            ]
        }
    },
    # 3 - Social
    {
        "input": {
            "personality_scores": {"تحليلي": 5, "إبداعي": 4, "اجتماعي": 9, "تنظيمي": 6, "عملي": 7},
            "interests": {"الطب": 8, "العلوم": 6, "التواصل": 9, "المساعدة الاجتماعية": 8, "التعليم": 7}
        },
        "output": {
            "personality_type": "اجتماعي",
            "strengths": ["تواصل ممتاز", "تعاطف مع الآخرين", "العمل الجماعي", "حب مساعدة الناس", "مهارات استماع فعالة"],
            "interests": ["الطب", "التواصل", "المساعدة الاجتماعية"],
            "recommended_majors": [
                {"name": "التمريض", "match_percentage": 91, "reasons": ["تعامل مباشر مع الناس", "مهنة إنسانية", "مساعدة المرضى"]},
                {"name": "علم النفس", "match_percentage": 89, "reasons": ["فهم الآخرين", "يجمع العلم والاجتماع", "فرص متنوعة"]},
                {"name": "التربية وعلم الاجتماع", "match_percentage": 86, "reasons": ["تأثير إيجابي", "تطوير المجتمع", "مجال واسع"]},
                {"name": "العلاقات العامة والإعلام", "match_percentage": 83, "reasons": ["يناسب الشخصيات الاجتماعية", "تواصل مستمر", "تطور مهني سريع"]},
                {"name": "الخدمة الاجتماعية", "match_percentage": 80, "reasons": ["خدمة المجتمع", "عمل إنساني", "تأثير اجتماعي حقيقي"]}
            ]
        }
    },
    # 4 - Organized
    {
        "input": {
            "personality_scores": {"تحليلي": 6, "إبداعي": 3, "اجتماعي": 5, "تنظيمي": 9, "عملي": 8},
            "interests": {"التجارة": 8, "المال والأعمال": 9, "الإدارة": 7, "القانون": 6, "الاقتصاد": 7}
        },
        "output": {
            "personality_type": "تنظيمي",
            "strengths": ["التخطيط الممتاز", "الانتباه للتفاصيل", "الالتزام والمسؤولية", "إدارة الوقت", "قرارات محسوبة"],
            "interests": ["التجارة", "المال والأعمال", "الإدارة"],
            "recommended_majors": [
                {"name": "إدارة الأعمال", "match_percentage": 94, "reasons": ["مهارات تنظيمية", "فرص قيادية", "مجال متنوع"]},
                {"name": "المحاسبة", "match_percentage": 90, "reasons": ["دقة وتنظيم", "مهنة مستقرة", "رياضيات مالية"]},
                {"name": "الاقتصاد", "match_percentage": 87, "reasons": ["تحليل مالي", "فهم الأسواق", "منهجي ومنطقي"]},
                {"name": "القانون", "match_percentage": 84, "reasons": ["دقة وتنظيم عالٍ", "منهجية تفكير", "مهنة محترمة"]},
                {"name": "إدارة المشاريع", "match_percentage": 81, "reasons": ["تخطيط وتنسيق", "قيادة الفرق", "متطلب في كل الصناعات"]}
            ]
        }
    },
    # 5 - Practical
    {
        "input": {
            "personality_scores": {"تحليلي": 5, "إبداعي": 5, "اجتماعي": 4, "تنظيمي": 6, "عملي": 9},
            "interests": {"الهندسة": 9, "البناء": 8, "التكنولوجيا": 7, "الميكانيكا": 8, "التطبيق العملي": 9}
        },
        "output": {
            "personality_type": "عملي",
            "strengths": ["مهارات عملية قوية", "حل مشاكل واقعية", "التعلم بالتجربة", "عمل تقني", "التفكير الواقعي"],
            "interests": ["الهندسة", "البناء", "الميكانيكا"],
            "recommended_majors": [
                {"name": "الهندسة الميكانيكية", "match_percentage": 93, "reasons": ["نظري وتطبيقي", "مشاريع ملموسة", "صناعات متعددة"]},
                {"name": "الهندسة المدنية", "match_percentage": 89, "reasons": ["بناء وإنشاءات", "تأثير مجتمعي", "مشاريع كبيرة"]},
                {"name": "هندسة الطاقة", "match_percentage": 85, "reasons": ["الطاقة المتجددة مستقبلية", "تطبيق عملي", "طلب عالٍ"]},
                {"name": "التقنيات الصناعية", "match_percentage": 82, "reasons": ["تطبيق مباشر", "مجال متنامٍ", "مهارات عملية"]},
                {"name": "هندسة التصنيع", "match_percentage": 78, "reasons": ["تصنيع وإنتاج", "إبداع عملي", "صناعة متطورة"]}
            ]
        }
    },
    # 6 - Medical / Analytical-Practical Mix
    {
        "input": {
            "personality_scores": {"تحليلي": 8, "إبداعي": 3, "اجتماعي": 6, "تنظيمي": 7, "عملي": 8},
            "interests": {"الطب": 10, "العلوم البيولوجية": 9, "الكيمياء": 8, "مساعدة الناس": 7}
        },
        "output": {
            "personality_type": "تحليلي عملي",
            "strengths": ["دقة علمية عالية", "صبر وتحمل", "ذاكرة قوية", "العمل تحت الضغط", "تفكير منطقي وإنساني"],
            "interests": ["الطب", "العلوم البيولوجية", "الكيمياء"],
            "recommended_majors": [
                {"name": "الطب البشري", "match_percentage": 96, "reasons": ["علم وإنسانية", "تحدي حقيقي", "مهنة مرموقة"]},
                {"name": "طب الأسنان", "match_percentage": 90, "reasons": ["دقة تقنية", "استقلالية مهنية", "دخل جيد"]},
                {"name": "الصيدلة", "match_percentage": 87, "reasons": ["علوم وتطبيق", "تنوع في الوظائف", "تطوير الأدوية"]},
                {"name": "التمريض الإكلينيكي", "match_percentage": 83, "reasons": ["تطبيق مباشر", "مساعدة المرضى", "مهنة حيوية"]},
                {"name": "الأحياء الجزيئية والوراثة", "match_percentage": 80, "reasons": ["علم متقدم", "بحث علمي", "مستقبل واعد"]}
            ]
        }
    },
    # 7 - Law and humanities
    {
        "input": {
            "personality_scores": {"تحليلي": 7, "إبداعي": 5, "اجتماعي": 8, "تنظيمي": 7, "عملي": 4},
            "interests": {"القانون": 9, "العدالة": 8, "الكتابة": 7, "السياسة": 6}
        },
        "output": {
            "personality_type": "اجتماعي تحليلي",
            "strengths": ["إقناع وحجج منطقية", "قراءة واسعة", "الدفاع عن الحقوق", "استراتيجية التفكير", "언어 skills"],
            "interests": ["القانون", "العدالة", "الكتابة"],
            "recommended_majors": [
                {"name": "الحقوق والقانون", "match_percentage": 95, "reasons": ["يجمع التحليل والتواصل", "مهنة مرموقة", "العدالة والحقوق"]},
                {"name": "العلوم السياسية", "match_percentage": 88, "reasons": ["فهم النظم السياسية", "تأثير على القرار", "نظرة شاملة"]},
                {"name": "الصحافة والإعلام", "match_percentage": 84, "reasons": ["تعبير ورأي", "وصول للجماهير", "دور حيوي في المجتمع"]},
                {"name": "العلاقات الدولية", "match_percentage": 81, "reasons": ["دبلوماسية وتفاوض", "عالمي ومفتوح", "مهارات تواصل"]},
                {"name": "الفلسفة والأخلاق", "match_percentage": 77, "reasons": ["تفكير نقدي", "حجج وبراهين", "فهم عميق"]}
            ]
        }
    },
    # 8 - Science / Research oriented
    {
        "input": {
            "personality_scores": {"تحليلي": 9, "إبداعي": 6, "اجتماعي": 3, "تنظيمي": 8, "عملي": 5},
            "interests": {"الفيزياء": 10, "الرياضيات": 9, "البحث العلمي": 9, "الكون والفضاء": 8}
        },
        "output": {
            "personality_type": "باحث علمي",
            "strengths": ["فضول علمي لا حدود له", "تفكير رياضي دقيق", "صبر في التجارب", "ابتكار حلول جديدة", "منهجية علمية"],
            "interests": ["الفيزياء", "الرياضيات", "البحث العلمي"],
            "recommended_majors": [
                {"name": "الفيزياء النظرية والتطبيقية", "match_percentage": 97, "reasons": ["إجابات عن الكون", "بحث أكاديمي", "تحديات فكرية"]},
                {"name": "هندسة الفيزياء", "match_percentage": 91, "reasons": ["تطبيق الفيزياء", "تقنيات حديثة", "نظري وعملي"]},
                {"name": "علوم الفضاء والفلك", "match_percentage": 88, "reasons": ["استكشاف الكون", "أبحاث مبتكرة", "مجال مميز"]},
                {"name": "الرياضيات البحتة والتطبيقية", "match_percentage": 85, "reasons": ["أساس كل العلوم", "تحديات ذهنية", "تدريس وبحث"]},
                {"name": "الهندسة النووية", "match_percentage": 80, "reasons": ["طاقة المستقبل", "علم متقدم", "تحديات حقيقية"]}
            ]
        }
    },
    # 9 - Education oriented
    {
        "input": {
            "personality_scores": {"تحليلي": 5, "إبداعي": 7, "اجتماعي": 9, "تنظيمي": 7, "عملي": 6},
            "interests": {"التعليم": 10, "الأطفال": 9, "التطوير البشري": 8, "القراءة": 7}
        },
        "output": {
            "personality_type": "تربوي اجتماعي",
            "strengths": ["الصبر وحب التعليم", "التواصل مع الأطفال", "الإبداع في الشرح", "الالتزام والمسؤولية", "التأثير الإيجابي"],
            "interests": ["التعليم", "الأطفال", "التطوير البشري"],
            "recommended_majors": [
                {"name": "التربية وعلم النفس التربوي", "match_percentage": 95, "reasons": ["شغف التعليم", "فهم الأطفال", "تأثير حقيقي"]},
                {"name": "تعليم اللغة العربية", "match_percentage": 88, "reasons": ["حب اللغة والتعليم", "دور ثقافي", "مربٍّ قدير"]},
                {"name": "تعليم الرياضيات والعلوم", "match_percentage": 84, "reasons": ["توصيل المعرفة", "مجال حيوي", "مطلوب دائماً"]},
                {"name": "علم النفس التربوي والإرشاد", "match_percentage": 81, "reasons": ["مساعدة الطلاب", "فهم التعلم", "دور إنساني"]},
                {"name": "الإدارة التربوية", "match_percentage": 78, "reasons": ["قيادة مؤسسات تعليمية", "تطوير المناهج", "إدارة ورؤية"]}
            ]
        }
    },
    # 10 - Business / Entrepreneurship
    {
        "input": {
            "personality_scores": {"تحليلي": 7, "إبداعي": 7, "اجتماعي": 7, "تنظيمي": 8, "عملي": 7},
            "interests": {"ريادة الأعمال": 10, "الابتكار": 9, "الأعمال التجارية": 8, "التسويق": 7}
        },
        "output": {
            "personality_type": "رائد أعمال",
            "strengths": ["رؤية شاملة", "روح مبادرة", "قدرة على الإقناع", "التفكير الاستراتيجي", "تحمل المخاطر المحسوبة"],
            "interests": ["ريادة الأعمال", "الابتكار", "الأعمال التجارية"],
            "recommended_majors": [
                {"name": "إدارة الأعمال والريادة", "match_percentage": 96, "reasons": ["يصنع قادة الأعمال", "ريادة وابتكار", "شبكات تجارية"]},
                {"name": "التسويق والعلامة التجارية", "match_percentage": 90, "reasons": ["إبداع وتحليل", "تأثير على السوق", "مجال حيوي"]},
                {"name": "الاقتصاد والتجارة الدولية", "match_percentage": 86, "reasons": ["فهم الاقتصاد العالمي", "فرص دولية", "تفكير استراتيجي"]},
                {"name": "التكنولوجيا والأعمال", "match_percentage": 83, "reasons": ["الجمع بين التقنية والأعمال", "مجال المستقبل", "راتب تنافسي"]},
                {"name": "إدارة سلاسل التوريد", "match_percentage": 79, "reasons": ["تنظيم لوجستي دقيق", "تحليل وتخطيط", "مطلوب عالمياً"]}
            ]
        }
    }
]


# ============================================
# English Personality Analysis Examples
# ============================================

ENGLISH_PERSONALITY_EXAMPLES = [
    # 1 - Analytical
    {
        "input": {
            "personality_scores": {"analytical": 9, "creative": 3, "social": 2, "organized": 7, "practical": 5},
            "interests": {"science": 8, "technology": 9, "engineering": 7, "mathematics": 8, "medicine": 2}
        },
        "output": {
            "personality_type": "analytical",
            "strengths": ["Logical and critical thinking", "Complex problem solving", "Data analysis precision", "Long-term focus", "Strong mathematical skills"],
            "interests": ["science", "technology", "mathematics"],
            "recommended_majors": [
                {"name": "Computer Science", "match_percentage": 95, "reasons": ["Strong analytical requirements", "Perfect for tech enthusiasts", "Wide career range"]},
                {"name": "Software Engineering", "match_percentage": 92, "reasons": ["Combines analysis with application", "Organized structure", "High market demand"]},
                {"name": "Artificial Intelligence", "match_percentage": 90, "reasons": ["Mathematical thinking required", "Future-proof field", "High salaries"]},
                {"name": "Statistics & Data Science", "match_percentage": 85, "reasons": ["Suits analytical minds", "Needed in all industries", "Strong scientific base"]},
                {"name": "Cybersecurity", "match_percentage": 80, "reasons": ["Combines tech and analysis", "Critical infrastructure", "Continuous evolution"]}
            ]
        }
    },
    # 2 - Creative
    {
        "input": {
            "personality_scores": {"analytical": 4, "creative": 9, "social": 7, "organized": 3, "practical": 5},
            "interests": {"arts": 9, "design": 8, "media": 7, "literature": 6, "technology": 5}
        },
        "output": {
            "personality_type": "creative",
            "strengths": ["Creative and innovative thinking", "Artistic expression", "Social communication", "Unique perspective", "Dynamic environments"],
            "interests": ["arts", "design", "media"],
            "recommended_majors": [
                {"name": "Graphic Design", "match_percentage": 93, "reasons": ["Creativity and imagination", "Art meets technology", "Diverse job market"]},
                {"name": "Digital Media", "match_percentage": 88, "reasons": ["Evolving field", "Creative social personalities", "Innovative expression"]},
                {"name": "Architecture & Interior Design", "match_percentage": 85, "reasons": ["Creative application", "Tangible impact", "Multidisciplinary"]},
                {"name": "Literature & Translation", "match_percentage": 80, "reasons": ["Suits word lovers", "Broad cultural field", "Translation demand"]},
                {"name": "Film & Media Production", "match_percentage": 77, "reasons": ["Visual storytelling", "Team creativity", "Growing industry"]}
            ]
        }
    },
    # 3 - Social
    {
        "input": {
            "personality_scores": {"analytical": 5, "creative": 4, "social": 9, "organized": 6, "practical": 7},
            "interests": {"medicine": 8, "science": 6, "communication": 9, "social_help": 8, "education": 7}
        },
        "output": {
            "personality_type": "social",
            "strengths": ["Excellent communication", "Empathy", "Teamwork ability", "Helping passion", "Active listening"],
            "interests": ["medicine", "communication", "social_help"],
            "recommended_majors": [
                {"name": "Nursing", "match_percentage": 91, "reasons": ["Direct people interaction", "Humanitarian profession", "Helping patients"]},
                {"name": "Psychology", "match_percentage": 89, "reasons": ["Understanding others", "Science and social work", "Diverse career paths"]},
                {"name": "Social Work & Sociology", "match_percentage": 86, "reasons": ["Positive impact", "Community development", "Broad field"]},
                {"name": "Public Relations & Media", "match_percentage": 83, "reasons": ["Social personalities", "Constant communication", "Fast career growth"]},
                {"name": "Community Development", "match_percentage": 80, "reasons": ["Serving society", "Humanitarian work", "Real social impact"]}
            ]
        }
    },
    # 4 - Organized
    {
        "input": {
            "personality_scores": {"analytical": 6, "creative": 3, "social": 5, "organized": 9, "practical": 8},
            "interests": {"business": 8, "finance": 9, "management": 7, "law": 6, "economics": 7}
        },
        "output": {
            "personality_type": "organized",
            "strengths": ["Excellent planning", "Attention to detail", "Commitment and responsibility", "Time management", "Calculated decisions"],
            "interests": ["business", "finance", "management"],
            "recommended_majors": [
                {"name": "Business Administration", "match_percentage": 94, "reasons": ["Requires organizational skills", "Leadership opportunities", "Diverse field"]},
                {"name": "Accounting", "match_percentage": 90, "reasons": ["Precision and organization", "Stable profession", "Financial mathematics"]},
                {"name": "Economics", "match_percentage": 87, "reasons": ["Financial analysis", "Market understanding", "Systematic thinking"]},
                {"name": "Law", "match_percentage": 84, "reasons": ["High precision", "Methodical thinking", "Respected profession"]},
                {"name": "Project Management", "match_percentage": 81, "reasons": ["Planning and coordination", "Team leadership", "Needed in all industries"]}
            ]
        }
    },
    # 5 - Practical
    {
        "input": {
            "personality_scores": {"analytical": 5, "creative": 5, "social": 4, "organized": 6, "practical": 9},
            "interests": {"engineering": 9, "construction": 8, "technology": 7, "mechanics": 8, "practical": 9}
        },
        "output": {
            "personality_type": "practical",
            "strengths": ["Strong practical skills", "Real-world problem solving", "Learning by doing", "Technical work", "Realistic thinking"],
            "interests": ["engineering", "construction", "mechanics"],
            "recommended_majors": [
                {"name": "Mechanical Engineering", "match_percentage": 93, "reasons": ["Theory meets application", "Tangible projects", "Multiple industries"]},
                {"name": "Civil Engineering", "match_percentage": 89, "reasons": ["Construction lover", "Community impact", "Large-scale projects"]},
                {"name": "Energy Engineering", "match_percentage": 85, "reasons": ["Renewable energy future", "Practical application", "High demand"]},
                {"name": "Industrial Technology", "match_percentage": 82, "reasons": ["Direct application", "Growing field", "Hands-on skills"]},
                {"name": "Manufacturing Engineering", "match_percentage": 78, "reasons": ["Production and fabrication", "Practical creativity", "Advanced industry"]}
            ]
        }
    },
    # 6 - Medical / Analytical-Practical
    {
        "input": {
            "personality_scores": {"analytical": 8, "creative": 3, "social": 6, "organized": 7, "practical": 8},
            "interests": {"medicine": 10, "biology": 9, "chemistry": 8, "helping_people": 7}
        },
        "output": {
            "personality_type": "analytical-practical",
            "strengths": ["High scientific precision", "Patience and persistence", "Strong memory", "Working under pressure", "Empathetic logic"],
            "interests": ["medicine", "biology", "chemistry"],
            "recommended_majors": [
                {"name": "Medicine & Surgery", "match_percentage": 96, "reasons": ["Science and humanity", "Real challenge", "Prestigious career"]},
                {"name": "Dentistry", "match_percentage": 90, "reasons": ["Technical precision", "Professional independence", "Good income"]},
                {"name": "Pharmacy", "match_percentage": 87, "reasons": ["Science and application", "Diverse roles", "Drug development"]},
                {"name": "Clinical Nursing", "match_percentage": 83, "reasons": ["Direct application", "Helping patients", "Vital profession"]},
                {"name": "Molecular Biology & Genetics", "match_percentage": 80, "reasons": ["Advanced science", "Research", "Promising future"]}
            ]
        }
    },
    # 7 - Research / Science oriented
    {
        "input": {
            "personality_scores": {"analytical": 9, "creative": 6, "social": 3, "organized": 8, "practical": 5},
            "interests": {"physics": 10, "mathematics": 9, "research": 9, "space": 8}
        },
        "output": {
            "personality_type": "scientific researcher",
            "strengths": ["Boundless scientific curiosity", "Precise mathematical thinking", "Patience in experiments", "Innovative solutions", "Scientific methodology"],
            "interests": ["physics", "mathematics", "research"],
            "recommended_majors": [
                {"name": "Physics (Theoretical & Applied)", "match_percentage": 97, "reasons": ["Answers about the universe", "Academic research", "Intellectual challenges"]},
                {"name": "Engineering Physics", "match_percentage": 91, "reasons": ["Physics application", "Modern technology", "Theory and practice"]},
                {"name": "Space Science & Astronomy", "match_percentage": 88, "reasons": ["Universe exploration", "Innovative research", "Unique field"]},
                {"name": "Pure & Applied Mathematics", "match_percentage": 85, "reasons": ["Foundation of all sciences", "Mental challenges", "Teaching and research"]},
                {"name": "Nuclear Engineering", "match_percentage": 80, "reasons": ["Energy of the future", "Advanced science", "Real challenges"]}
            ]
        }
    },
    # 8 - Entrepreneurship
    {
        "input": {
            "personality_scores": {"analytical": 7, "creative": 7, "social": 7, "organized": 8, "practical": 7},
            "interests": {"entrepreneurship": 10, "innovation": 9, "business": 8, "marketing": 7}
        },
        "output": {
            "personality_type": "entrepreneur",
            "strengths": ["Comprehensive vision", "Initiative spirit", "Persuasion ability", "Strategic thinking", "Calculated risk-taking"],
            "interests": ["entrepreneurship", "innovation", "business"],
            "recommended_majors": [
                {"name": "Business Administration & Entrepreneurship", "match_percentage": 96, "reasons": ["Creates business leaders", "Innovation spirit", "Business networks"]},
                {"name": "Marketing & Branding", "match_percentage": 90, "reasons": ["Creativity and analysis", "Market impact", "Vital field"]},
                {"name": "Economics & International Trade", "match_percentage": 86, "reasons": ["Global economic understanding", "International opportunities", "Strategic thinking"]},
                {"name": "Technology & Business", "match_percentage": 83, "reasons": ["Tech meets business", "Future field", "Competitive salary"]},
                {"name": "Supply Chain Management", "match_percentage": 79, "reasons": ["Precise logistics", "Analysis and planning", "Globally needed"]}
            ]
        }
    }
]


# ============================================
# Combined Examples Dictionary
# ============================================

ALL_TRAINING_EXAMPLES = {
    "arabic": ARABIC_PERSONALITY_EXAMPLES,
    "english": ENGLISH_PERSONALITY_EXAMPLES
}


def get_examples_for_language(language="arabic"):
    """Get examples by language: 'arabic' or 'english'"""
    return ALL_TRAINING_EXAMPLES.get(language, ARABIC_PERSONALITY_EXAMPLES)


def format_examples_for_prompt(language="arabic", max_examples=3):
    """Format examples for inclusion in prompts as Few-Shot context"""
    examples = get_examples_for_language(language)[:max_examples]
    formatted = ""
    for i, example in enumerate(examples, 1):
        if language == "arabic":
            formatted += f"\n### مثال {i}:\n"
            formatted += f"**المدخلات:**\n{example['input']}\n\n"
            formatted += f"**المخرجات المتوقعة:**\n{example['output']}\n\n"
        else:
            formatted += f"\n### Example {i}:\n"
            formatted += f"**Input:**\n{example['input']}\n\n"
            formatted += f"**Expected Output:**\n{example['output']}\n\n"
    return formatted
