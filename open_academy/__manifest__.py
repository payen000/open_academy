{
    'name': "open_academy",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'author': "Vauxoo",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'license': 'LGPL-3',
    'version': '15.0.0.0.0',
    'depends': [
        'base',
        'contacts',
        'board',
    ],
    'data': [
        'security/res_groups.xml',
        'security/ir_rule.xml',
        'security/ir.model.access.csv',
        'wizards/assign_attendee_sessions_views.xml',
        'views/course.xml',
        'views/session.xml',
        'views/partner.xml',
        'views/report_session.xml',
        'views/dashboard.xml',
        'data/ir_ui_menu.xml',
    ],
    'demo': [
        'demo/course.xml',
        'demo/session.xml',
        'demo/category.xml',
        'demo/res_users.xml',
    ],
}
