{
    'name': 'Sales Dashboard Realtime',
    'version': '1.0',
    'depends': ['sale_management', 'web'],
    'data': [
        'views/menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'sale_dashboard/static/src/js/dashboard.js',
            'sale_dashboard/static/src/xml/dashboard.xml',
            'sale_dashboard/static/src/css/style.css',
        ],
    },
    'installable': True,
}