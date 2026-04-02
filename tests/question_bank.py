# tests/question_bank.py
"""
بنك أسئلة شامل - 40+ سؤال
Comprehensive Question Bank - 40+ questions
"""

COMPREHENSIVE_QUESTIONS = [
    {
        'category': 'personality',
        'text': 'كيف تتعامل مع المواقف الضاغطة؟',
        'choices': [
            {'text': 'أحلل الموقف بهدوء وأبحث عن حلول منطقية', 'value': 9, 'traits': 'analytical,organized'},
            {'text': 'أفكر بطريقة إبداعية خارج الصندوق', 'value': 7, 'traits': 'creative,practical'},
            {'text': 'أطلب المساعدة والدعم من الآخرين', 'value': 6, 'traits': 'social'},
            {'text': 'أتعامل معها خطوة بخطوة بشكل منهجي', 'value': 8, 'traits': 'organized,practical'},
        ]
    },
    {
        'category': 'personality',
        'text': 'ما أسلوبك المفضّل في اتخاذ القرارات؟',
        'choices': [
            {'text': 'تحليل جميع الخيارات بعناية قبل القرار', 'value': 9, 'traits': 'analytical'},
            {'text': 'الاستماع لحدسي وخبرتي الشخصية', 'value': 7, 'traits': 'creative'},
            {'text': 'استشارة الآخرين وأخذ آرائهم', 'value': 6, 'traits': 'social'},
            {'text': 'القرار السريع بناءً على المعلومات المتاحة', 'value': 8, 'traits': 'practical'},
        ]
    },
    {
        'category': 'personality',
        'text': 'كيف تتعلم أفضل؟',
        'choices': [
            {'text': 'من خلال البحث والقراءة المكثفة', 'value': 9, 'traits': 'analytical'},
            {'text': 'من خلال التجربة والاستكشاف', 'value': 8, 'traits': 'creative,practical'},
            {'text': 'من خلال المناقشات الجماعية', 'value': 7, 'traits': 'social'},
            {'text': 'من خلال الدروس المنظمة والممارسة', 'value': 8, 'traits': 'organized'},
        ]
    },
    {
        'category': 'personality',
        'text': 'ما الذي يحفزك أكثر؟',
        'choices': [
            {'text': 'حل ألغاز وتحديات معقدة', 'value': 9, 'traits': 'analytical'},
            {'text': 'ابتكار شيء جديد ومميز', 'value': 9, 'traits': 'creative'},
            {'text': 'مساعدة الآخرين وإحداث فرق', 'value': 9, 'traits': 'social'},
            {'text': 'إنجاز المهام بكفاءة عالية', 'value': 9, 'traits': 'organized,practical'},
        ]
    },
    {
        'category': 'personality',
        'text': 'كيف تصف نفسك في الأوقات الصعبة؟',
        'choices': [
            {'text': 'أبقى هادئاً وأحلل الوضع', 'value': 9, 'traits': 'analytical,organized'},
            {'text': 'أبحث عن حلول غير تقليدية', 'value': 8, 'traits': 'creative'},
            {'text': 'أطلب الدعم من أصدقائي وعائلتي', 'value': 7, 'traits': 'social'},
            {'text': 'أعمل بجد حتى تنتهي المشكلة', 'value': 8, 'traits': 'practical'},
        ]
    },
    {
        'category': 'personality',
        'text': 'ما الذي تفضله في وقت فراغك؟',
        'choices': [
            {'text': 'القراءة أو حل puzzles', 'value': 9, 'traits': 'analytical'},
            {'text': 'الرسم أو الكتابة أو التصميم', 'value': 9, 'traits': 'creative'},
            {'text': 'الخروج مع الأصدقاء', 'value': 9, 'traits': 'social'},
            {'text': 'ممارسة هواية عملية أو رياضة', 'value': 8, 'traits': 'practical'},
        ]
    },
    {
        'category': 'personality',
        'text': 'كيف تتفاعل مع الأفكار الجديدة؟',
        'choices': [
            {'text': 'أدرسها بعمق قبل تبنيها', 'value': 9, 'traits': 'analytical'},
            {'text': 'أتحمس لتجربتها فوراً', 'value': 8, 'traits': 'creative'},
            {'text': 'أناقشها مع الآخرين أولاً', 'value': 7, 'traits': 'social'},
            {'text': 'أقيّم فائدتها العملية أولاً', 'value': 8, 'traits': 'practical,organized'},
        ]
    },
    {
        'category': 'personality',
        'text': 'ما مدى أهمية التخطيط المسبق بالنسبة لك؟',
        'choices': [
            {'text': 'مهم جداً - أخطط لكل شيء', 'value': 10, 'traits': 'organized,analytical'},
            {'text': 'أخطط للأمور المهمة فقط', 'value': 7, 'traits': 'practical'},
            {'text': 'أفضل التلقائية والمرونة', 'value': 5, 'traits': 'creative,social'},
            {'text': 'أخطط لكن أترك مجال للتغيير', 'value': 8, 'traits': 'analytical'},
        ]
    },
    {
        'category': 'personality',
        'text': 'كيف تعبّر عن أفكارك؟',
        'choices': [
            {'text': 'بطريقة منطقية ومنظمة', 'value': 9, 'traits': 'analytical,organized'},
            {'text': 'بطريقة فنية أو إبداعية', 'value': 9, 'traits': 'creative'},
            {'text': 'من خلال النقاشات والحوارات', 'value': 8, 'traits': 'social'},
            {'text': 'من خلال الأمثلة العملية', 'value': 8, 'traits': 'practical'},
        ]
    },
    {
        'category': 'personality',
        'text': 'ماذا تفعل عند مواجهة فشل؟',
        'choices': [
            {'text': 'أحلل ما حدث لأتعلم منه', 'value': 9, 'traits': 'analytical'},
            {'text': 'أفكر في طرق جديدة للمحاولة', 'value': 8, 'traits': 'creative'},
            {'text': 'أتحدث عنه مع من أثق بهم', 'value': 7, 'traits': 'social'},
            {'text': 'أحاول مرة أخرى بعزيمة أقوى', 'value': 9, 'traits': 'practical,organized'},
        ]
    },
    
    {
        'category': 'skills',
        'text': 'هل تفضل العمل الفردي أم الجماعي؟',
        'choices': [
            {'text': 'العمل الفردي بشكل كبير', 'value': 9, 'traits': 'analytical,organized'},
            {'text': 'العمل الجماعي بشكل كبير', 'value': 9, 'traits': 'social'},
            {'text': 'مزيج حسب نوع المشروع', 'value': 7, 'traits': 'practical'},
            {'text': 'العمل الفردي مع تنسيق جماعي', 'value': 8, 'traits': 'creative,analytical'},
        ]
    },
    {
        'category': 'skills',
        'text': 'كيف تدير وقتك؟',
        'choices': [
            {'text': 'باستخدام جداول وخطط مفصلة', 'value': 10, 'traits': 'organized'},
            {'text': 'أعطي أولوية للمهام المهمة', 'value': 8, 'traits': 'analytical,practical'},
            {'text': 'أعمل حسب الموقف والحاجة', 'value': 6, 'traits': 'creative,social'},
            {'text': 'أوازن بين التخطيط والمرونة', 'value': 8, 'traits': 'organized,practical'},
        ]
    },
    {
        'category': 'skills',
        'text': 'ما مستوى راحتك مع التكنولوجيا؟',
        'choices': [
            {'text': 'مرتاح جداً وأحب تعلم الجديد', 'value': 10, 'traits': 'analytical,creative'},
            {'text': 'أستخدمها للحاجات الأساسية', 'value': 6, 'traits': 'practical'},
            {'text': 'أفضل التواصل الشخصي المباشر', 'value': 5, 'traits': 'social'},
            {'text': 'أحب التكنولوجيا للإنتاجية', 'value': 9, 'traits': 'organized,analytical'},
        ]
    },
    {
        'category': 'skills',
        'text': 'هل تحب التعامل مع الأرقام؟',
        'choices': [
            {'text': 'نعم، أستمتع بالحسابات المعقدة', 'value': 10, 'traits': 'analytical'},
            {'text': 'أستطيع لكن أفضل الإبداع', 'value': 6, 'traits': 'creative'},
            {'text': 'أفضل التعامل مع الأشخاص', 'value': 4, 'traits': 'social'},
            {'text': 'نعم، للأمور العملية', 'value': 8, 'traits': 'practical,organized'},
        ]
    },
    {
        'category': 'skills',
        'text': 'كيف تتعامل مع التفاصيل الدقيقة؟',
        'choices': [
            {'text': 'أحرص على كل تفصيلة', 'value': 10, 'traits': 'analytical,organized'},
            {'text': 'أركز على الصورة الكبيرة', 'value': 6, 'traits': 'creative'},
            {'text': 'أهتم بالتفاصيل المهمة', 'value': 8, 'traits': 'practical'},
            {'text': 'أتأكد منها مع الفريق', 'value': 7, 'traits': 'social,organized'},
        ]
    },
    {
        'category': 'skills',
        'text': 'ما مدى قدرتك على التحدث أمام الجمهور؟',
        'choices': [
            {'text': 'ممتازة وأستمتع بها', 'value': 9, 'traits': 'social,creative'},
            {'text': 'جيدة عند تقديم معلومات واضحة', 'value': 7, 'traits': 'analytical,organized'},
            {'text': 'أفضل العمل خلف الكواليس', 'value': 5, 'traits': 'analytical'},
            {'text': 'أستطيع عند الحاجة', 'value': 7, 'traits': 'practical'},
        ]
    },
    {
        'category': 'skills',
        'text': 'كيف تتعامل مع النقد؟',
        'choices': [
            {'text': 'أحلله و أستفيد منه', 'value': 9, 'traits': 'analytical,organized'},
            {'text': 'أستخدمه لتطوير أفكاري', 'value': 8, 'traits': 'creative,practical'},
            {'text': 'أستشير الآخرين في رأيهم', 'value': 7, 'traits': 'social'},
            {'text': 'أقبله وأعمل على التحسين', 'value': 9, 'traits': 'practical,analytical'},
        ]
    },
    {
        'category': 'skills',
        'text': 'ما مدى قدرتك على حل الصراعات؟',
        'choices': [
            {'text': 'أحللها منطقياً وأجد حلول عادلة', 'value': 9, 'traits': 'analytical,organized'},
            {'text': 'أبحث عن حلول إبداعية تُرضي الجميع', 'value': 8, 'traits': 'creative,social'},
 {'text': 'أفضل الحوار و الوساطة', 'value': 9, 'traits': 'social'},
            {'text': 'أعمل على حل سريع وعملي', 'value': 8, 'traits': 'practical'},
        ]
    },
    {
        'category': 'skills',
        'text': 'كيف تتعامل مع المهام المتعددة؟',
        'choices': [
            {'text': 'أنظمها حسب الأولوية بشكل دقيق', 'value': 10, 'traits': 'organized'},
            {'text': 'أستطيع التبديل بينها بمرونة', 'value': 8, 'traits': 'creative,practical'},
            {'text': 'أوزعها مع الفريق', 'value': 7, 'traits': 'social'},
            {'text': 'أركز على كل مهمة حتى تنتهي', 'value': 8, 'traits': 'analytical'},
        ]
    },
    {
        'category': 'skills',
        'text': 'ما مستوى إتقانك للغات؟',
        'choices': [
            {'text': 'أجيد لغات متعددة', 'value': 9, 'traits': 'analytical,social'},
            {'text': 'أركز على لغتي الأم بشكل ممتاز', 'value': 7, 'traits': 'creative'},
            {'text': 'أستخدم اللغة للتواصل', 'value': 8, 'traits': 'social,practical'},
            {'text': 'أتعلم حسب الحاجة', 'value': 7, 'traits': 'practical,organized'},
        ]
    },
    
    {
        'category': 'academic',
        'text': 'ما المواد الدراسية التي تتفوق فيها؟',
        'choices': [
            {'text': 'الرياضيات والعلوم', 'value': 10, 'traits': 'analytical'},
            {'text': 'الفنون واللغات', 'value': 9, 'traits': 'creative'},
            {'text': 'الدراسات الاجتماعية والإنسانية', 'value': 9, 'traits': 'social'},
            {'text': 'المواد التطبيقية والعملية', 'value': 9, 'traits': 'practical'},
        ]
    },
    {
        'category': 'academic',
        'text': 'هل تفضل الدراسة النظرية أم العملية؟',
        'choices': [
            {'text': 'النظرية بشكل كبير', 'value': 9, 'traits': 'analytical,creative'},
            {'text': 'العملية بشكل كبير', 'value': 10, 'traits': 'practical'},
            {'text': 'مزيج متوازن', 'value': 7, 'traits': 'organized'},
            {'text': 'التعلم التفاعلي الجماعي', 'value': 8, 'traits': 'social'},
        ]
    },
    {
        'category': 'academic',
        'text': 'كيف تتعامل مع البحوث والمشاريع؟',
        'choices': [
            {'text': 'أحب البحث العميق والتحليل', 'value': 10, 'traits': 'analytical'},
            {'text': 'أفضل المشاريع الإبداعية', 'value': 9, 'traits': 'creative'},
            {'text': 'أستمتع بالعمل الجماعي', 'value': 9, 'traits': 'social'},
            {'text': 'أركز على النتائج العملية', 'value': 9, 'traits': 'practical,organized'},
        ]
    },
    {
        'category': 'academic',
        'text': 'ما نوع المشاريع التي تستمتع بها؟',
        'choices': [
            {'text': 'تحليل بيانات أو برمجة', 'value': 10, 'traits': 'analytical'},
            {'text': 'تصميم أو إبداع فني', 'value': 9, 'traits': 'creative'},
            {'text': 'خدمة مجتمع أو توعية', 'value': 9, 'traits': 'social'},
            {'text': 'بناء أو تطوير شيء ملموس', 'value': 9, 'traits': 'practical'},
        ]
    },
    {
        'category': 'academic',
        'text': 'كيف تستعد للامتحانات؟',
        'choices': [
            {'text': 'أضع خطة منظمة وأتبعها', 'value': 10, 'traits': 'organized'},
            {'text': 'أدرس المواضيع المهمة بعمق', 'value': 9, 'traits': 'analytical'},
            {'text': 'أدرس مع مجموعات', 'value': 8, 'traits': 'social'},
            {'text': 'أركز على الأمثلة العملية', 'value': 8, 'traits': 'practical'},
        ]
    },
    {
        'category': 'academic',
        'text': 'ما مدى حبك للقراءة؟',
        'choices': [
            {'text': 'أحب القراءة الأكاديمية جداً', 'value': 10, 'traits': 'analytical'},
            {'text': 'أحب الروايات والقصص', 'value': 9, 'traits': 'creative'},
            {'text': 'أفضل الكتب الملهمة والتنموية', 'value': 8, 'traits': 'social'},
            {'text': 'أقرأ للتعلم والفائدة', 'value': 8, 'traits': 'practical,organized'},
        ]
    },
    {
        'category': 'academic',
        'text': 'هل تفضل التعلم الذاتي أم الموجّه؟',
        'choices': [
            {'text': 'التعلم الذاتي بشكل كبير', 'value': 9, 'traits': 'analytical,creative'},
            {'text': 'التعلم الموجّه والمنظم', 'value': 9, 'traits': 'organized'},
            {'text': 'التعلم التعاوني', 'value': 9, 'traits': 'social'},
            {'text': 'مزيج حسب الموضوع', 'value': 8, 'traits': 'practical'},
        ]
    },
    {
        'category': 'academic',
        'text': 'ما رأيك في التعليم عن بُعد؟',
        'choices': [
            {'text': 'ممتاز للتعلم المستقل', 'value': 9, 'traits': 'analytical,organized'},
            {'text': 'جيد للمواد الإبداعية', 'value': 7, 'traits': 'creative'},
            {'text': 'أفضل التعليم الحضوري', 'value': 6, 'traits': 'social'},
            {'text': 'عملي ومفيد', 'value': 8, 'traits': 'practical'},
        ]
    },
    {
        'category': 'academic',
        'text': 'كيف تقيّم نجاحك الأكاديمي؟',
        'choices': [
            {'text': 'بالدرجات والتقييمات الدقيقة', 'value': 9, 'traits': 'analytical,organized'},
            {'text': 'بمدى فهمي وإبداعي', 'value': 8, 'traits': 'creative'},
            {'text': 'بمدى تأثيري وتواصلي', 'value': 7, 'traits': 'social'},
            {'text': 'بما تعلمته فعلياً', 'value': 9, 'traits': 'practical'},
        ]
    },
    {
        'category': 'academic',
        'text': 'ما مدى اهتمامك بالبحث العلمي؟',
        'choices': [
            {'text': 'مهتم جداً وأطمح للدراسات العليا', 'value': 10, 'traits': 'analytical'},
            {'text': 'مهتم بالجوانب الإبداعية منه', 'value': 8, 'traits': 'creative'},
            {'text': 'أفضل التطبيق المباشر', 'value': 7, 'traits': 'practical,social'},
            {'text': 'أحب البحث المنظم', 'value': 9, 'traits': 'organized,analytical'},
        ]
    },
    
    {
        'category': 'goals',
        'text': 'ما بيئة العمل المفضلة لك؟',
        'choices': [
            {'text': 'مكتب هادئ للتركيز', 'value': 9, 'traits': 'analytical,organized'},
            {'text': 'مكان إبداعي ملهم', 'value': 9, 'traits': 'creative'},
            {'text': 'بيئة جماعية نشطة', 'value': 10, 'traits': 'social'},
            {'text': 'ميدان العمل العملي', 'value': 9, 'traits': 'practical'},
        ]
    },
    {
        'category': 'goals',
        'text': 'ما أولوياتك المهنية؟',
        'choices': [
            {'text': 'التطور المهني والخبرة', 'value': 9, 'traits': 'analytical,organized'},
            {'text': 'الإبداع والابتكار', 'value': 9, 'traits': 'creative'},
            {'text': 'التأثير الاجتماعي', 'value': 10, 'traits': 'social'},
            {'text': 'الدخل والاستقرار', 'value': 9, 'traits': 'practical,organized'},
        ]
    },
    {
        'category': 'goals',
        'text': 'هل تفضل الوظيفة الثابتة أم ريادة الأعمال؟',
        'choices': [
            {'text': 'وظيفة ثابتة في مجال تخصصي', 'value': 8, 'traits': 'analytical,organized'},
            {'text': 'ريادة أعمال إبداعية', 'value': 10, 'traits': 'creative'},
            {'text': 'عمل يتضمن تفاعل مع الناس', 'value': 8, 'traits': 'social'},
            {'text': 'مشاريع مستقلة عملية', 'value': 9, 'traits': 'practical'},
        ]
    },
    {
        'category': 'goals',
        'text': 'ما مدى أهمية السفر والتنقل في عملك؟',
        'choices': [
            {'text': 'أفضل الاستقرار في مكان واحد', 'value': 7, 'traits': 'organized,analytical'},
            {'text': 'أحب السفر للإلهام', 'value': 8, 'traits': 'creative'},
            {'text': 'أحب التواجد مع مجتمعات مختلفة', 'value': 9, 'traits': 'social'},
            {'text': 'حسب متطلبات العمل', 'value': 7, 'traits': 'practical'},
        ]
    },
    {
        'category': 'goals',
        'text': 'كم ساعة عمل مثالية لك يومياً؟',
        'choices': [
            {'text': '6-8 ساعات منظمة', 'value': 8, 'traits': 'organized'},
            {'text': 'حسب الإبداع والإلهام', 'value': 7, 'traits': 'creative'},
            {'text': 'ساعات مرنة للتوازن', 'value': 8, 'traits': 'social,practical'},
            {'text': 'طالما أنجز المطلوب', 'value': 8, 'traits': 'practical,analytical'},
        ]
    },
    {
        'category': 'goals',
        'text': 'ما مدى أهمية المردود المادي؟',
        'choices': [
            {'text': 'مهم لكن ليس الأولوية الوحيدة', 'value': 7, 'traits': 'analytical,organized'},
            {'text': 'أهم من المال الرضا عن العمل', 'value': 6, 'traits': 'creative,social'},
            {'text': 'مهم جداً للاستقرار', 'value': 9, 'traits': 'practical,organized'},
            {'text': 'متوسط الأهمية', 'value': 7, 'traits': 'social'},
        ]
    },
    {
        'category': 'goals',
        'text': 'هل تحب العمل تحت الضغط؟',
        'choices': [
            {'text': 'أفضل البيئة الهادئة', 'value': 6, 'traits': 'analytical,organized'},
            {'text': 'أستطيع لكن أفضل المرونة', 'value': 7, 'traits': 'creative'},
            {'text': 'نعم إذا كان هناك فريق داعم', 'value': 8, 'traits': 'social'},
            {'text': 'نعم، أنجز أفضل تحت التحديات', 'value': 9, 'traits': 'practical'},
        ]
    },
    {
        'category': 'goals',
        'text': 'ما رأيك في العمل الحر (Freelancing)؟',
        'choices': [
            {'text': 'ممتاز للمشاريع المحددة', 'value': 8, 'traits': 'analytical,practical'},
            {'text': 'مثالي للحرية الإبداعية', 'value': 10, 'traits': 'creative'},
            {'text': 'أفضل الوظيفة الثابتة', 'value': 6, 'traits': 'organized,social'},
            {'text': 'جيد للتنوع', 'value': 8, 'traits': 'practical'},
        ]
    },
    {
        'category': 'goals',
        'text': 'كيف ترى نفسك بعد 10 سنوات؟',
        'choices': [
            {'text': 'خبير في مجالي التخصصي', 'value': 9, 'traits': 'analytical,organized'},
            {'text': 'رائد أعمال مبتكر', 'value': 10, 'traits': 'creative'},
            {'text': 'مؤثر اجتماعي أو قائد', 'value': 10, 'traits': 'social'},
            {'text': 'محترف ناجح في عملي', 'value': 9, 'traits': 'practical,organized'},
        ]
    },
    {
        'category': 'goals',
        'text': 'ما مدى اهتمامك بالتوازن بين العمل والحياة؟',
        'choices': [
            {'text': 'مهم جداً - أخطط له بعناية', 'value': 9, 'traits': 'organized'},
            {'text': 'مهم لكن أركز على الشغف', 'value': 7, 'traits': 'creative'},
            {'text': 'أولوية قصوى للعائلة والمجتمع', 'value': 10, 'traits': 'social'},
            {'text': 'مهم حسب الظروف', 'value': 8, 'traits': 'practical'},
        ]
    },
]


def get_questions_by_category(category: str = None):
    """الحصول على الأسئلة حسب الفئة"""
    if category:
        return [q for q in COMPREHENSIVE_QUESTIONS if q['category'] == category]
    return COMPREHENSIVE_QUESTIONS


def get_all_categories():
    """الحصول على جميع الفئات"""
    return list(set(q['category'] for q in COMPREHENSIVE_QUESTIONS))
