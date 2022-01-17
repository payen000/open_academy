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
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/course.xml',
        'views/session.xml',
        'views/partner.xml',
        'data/ir_ui_menu.xml',
    ],
    'demo': [
        'demo/course.xml',
        'demo/session.xml',
        'demo/category.xml',
    ],
}
