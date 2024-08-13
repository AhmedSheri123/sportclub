from django.shortcuts import render
def index(request):
    nav_items = [
        {"name": "الرئيسية", "href": "/"},
        {"name": "عن منصتنا", "href": "/about"},
        {"name": "خدماتنا", "href": "/services"},
        {"name": "اتصل بنا", "href": "/contact"},
    ]
    bullets = [
        {
            "title": "سهولة الاستخدام",
            "description": "واجهة مستخدم بسيطة وسهلة الاستخدام تساعدك في إدارة كل شيء بكل سهولة."
        },
        {
            "title": "دعم فني 24/7",
            "description": "فريق دعم فني متوفر على مدار الساعة لضمان استمرارية العمل."
        },
        {
            "title": "تحديثات مستمرة",
            "description": "تحديثات دورية وتحسينات لضمان تجربة مستخدم متميزة."
        },
        {
            "title": "تقارير متقدمة",
            "description": "تقارير متقدمة تساعدك على اتخاذ قرارات مدروسة."
        }
    ]
    
    services = [
        {
        "name": "إدارة الفرق",
        "icon": "fas fa-users",
        "description": "إدارة شاملة لجميع جوانب الفريق",
        },
        {
        "name": "جدولة المباريات",
        "icon": "fas fa-calendar-alt",
        "description": "تنظيم وجدولة المباريات بسهولة",
        },
        {
        "name": "تحليل الأداء",
        "icon": "fas fa-chart-bar",
        "description": "تحليلات متقدمة لتحسين أداء الفريق",
        },
        {
        "name": "إدارة الأعضاء",
        "icon": "fas fa-user-plus",
        "description": "إدارة فعالة لجميع أعضاء الفريق",
        },
    {
      "name": "التواصل الداخلي",
      "icon": "fas fa-comments",
      "description": "منصة تواصل مدمجة للفريق",
    },
    {
      "name": "تتبع الإنجازات",
      "icon": "fas fa-trophy",
      "description": "تتبع وعرض إنجازات الفريق والأعضاء",
    },
    {
      "name": "إدارة المهام",
      "icon": "fas fa-tasks",
      "description": "توزيع وتتبع المهام بكفاءة",
    },
    {
      "name": "إدارة الميزانية",
      "icon": "fas fa-credit-card",
      "description": "تخطيط وإدارة ميزانية الفريق",
    },
    {
      "name": "أمان البيانات",
      "icon": "fas fa-shield-alt",
      "description": "حماية قوية لبيانات الفريق والأعضاء",
    },
    {
      "name": "أداء سريع",
      "icon": "fas fa-bolt",
      "description": "نظام سريع وفعال لتحسين الإنتاجية",
    },
    {
      "name": "دعم العملاء",
      "icon": "fas fa-headset",
      "description": "دعم فني متميز على مدار الساعة",
    },
    {
      "name": "تحديثات مستمرة",
      "icon": "fas fa-sync-alt",
      "description": "تحديثات منتظمة لتحسين الأداء والميزات",
    },
  ];
    
    pricing = [
        {
            "name": "الباقة المجانية",
            "price": "0",
            "features": ["مستخدم واحد", "20 لاعب", "تقارير أساسية"]
        },
        {
            "name": "الباقة الأساسية",
            "price": "50",
            "features": ["5 مستخدمين", "100 لاعب", "تقارير متقدمة"]
        },
        {
            "name": "الباقة الاحترافية",
            "price": "150",
            "features": ["10 مستخدمين", "500 لاعب", "تحليل شامل للبيانات"]
        },
        {
            "name": "الباقة المميزة",
            "price": "300",
            "features": ["عدد غير محدود من المستخدمين", "عدد غير محدود من اللاعبين", "كل الميزات المتاحة"]
        }
    ]

    context = {
        'nav_items': nav_items,
        "bullets": bullets,
        "services": services,
        "pricing": pricing
    }
    return render(request, 'pages/index.html', context)

