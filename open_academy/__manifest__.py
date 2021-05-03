# -*- coding: utf-8 -*-
{
    'name': "Odoo 14 Development Tutorial",

    'summary': """
        Odoo 13 And 14 Development Tutorial""",

    'description': """
        Odoo 14 Development Tutorial,
        Odoo 13 Development Tutorial,
        Development Tutorial,
        Odoo Tutorial,
        Odoo13, Odoo14, odoo Tutorials, odoo learning, odoo13 Tutorials, odoo14 Tutorials, Tutorial,
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
    'category': 'Extra Tools',
    'version': '14.0.1.3.0',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board', 'website_slides'],
    'images': ['static/description/banner.gif'],

    # always loaded
    'data': [
        'data/slide_channel_data.xml',
        'data/slide_channel_data_v13.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/session_board.xml',
        'reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
