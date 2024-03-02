# -*- coding: utf-8 -*-
{
    'name': "Resume Screening",
    'author': "Slim Yaiche",
    'version': '1.2',
    'category': '',
    'depends': ['base', 'web'],
    'data': [
        'views/base_menu.xml',
        'views/view.xml',
        'security/ir.model.access.csv',
        # Ajoutez d'autres fichiers de données si nécessaire
    ],
    'assets': {
        'web.assets_backend': ['resume_screening/static/src/css/job_application.css'],
        'web.assets_frontend': [
            ('prepend', 'resume_screening/static/src/css/bootstrap.min.css'),
            ('prepend', 'resume_screening/static/src/css/custom_animations.css'),
            ('prepend', 'resume_screening/static/src/js/bootstrap.bundle.min.js'),
            ('prepend', 'resume_screening/static/src/js/custom_animations.js'),
        ],

        'web.assets_qweb': [
            'resume_screening/views/qweb.xml',
        ],
    },
    'application': True,
}
