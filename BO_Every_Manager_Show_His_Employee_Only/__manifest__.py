# -*- coding: utf-8 -*-
{
    'name': "BO Every Manager Show His Employees Only",

    'summary': """
       Manager Show His Employee Only """,

    'description': """
        This module is useful to departments that operate on the Odoo system and preserve the privacy of each department in the organization. So that no manager can control an employee outside his powers .
    """,

    'author': "Boot",
    'website': "http://www.yourcompany.com",
    'company': 'Boot Solutions For Information Technology',
    "category": "Employees",
    "license": "AGPL-3",


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'HR',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    "application": True,
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "images": ["static/description/poster.jpg", ],
    "auto_install": False,
    "installable": True,
}
