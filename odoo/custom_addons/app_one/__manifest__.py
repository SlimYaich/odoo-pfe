# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "App One",
    'author': "Slim Yaiche",
    'version': '1.2',
    'category': '',
    'depends': ['base', 'sale_management', 'account_accountant' , 'mail'
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/property_view.xml',
        'views/owner_view.xml',
        'views/tag_view.xml',
        'views/sale_order_view.xml',

    ],
    'assets': {
        'web.assets_backend': ['app_one\static\src\css\property.css']
    },
    'application': True,

}
