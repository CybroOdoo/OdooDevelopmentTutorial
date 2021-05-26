# -*- coding: utf-8 -*-
{
    'name': "Odoo 13 Development Tutorial",

    'summary': """
         Odoo 13 Development Tutorials""",

    'description': """
        Open acadaemy module for managing trainings:
        -Manage student enroll
        -Attendance registration
        -Trainer
        -Training sessions
        -Courses
        -More..
    """,

    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'live_test_url': 'https://bit.ly/3knPv8t',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tutorials',
    'version': '13.0.1.0.0',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website_slides'],
    'images': ['static/description/banner.gif'],
    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/openacademy.xml',
        'views/partner.xml',
        'wizard/wizard_view.xml',
        'data/slide_channel_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
