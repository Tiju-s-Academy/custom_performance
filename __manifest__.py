{
    'name': 'Performance',
    'version': '17.0.1.0',
    'author': 'Tijus Academy',
    'summary': 'use for Calculate employee performance',
    'depends': ['base','hr','gamification','tijus_custom_base'],
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'views/employee_performance_view.xml',
        'views/performance_menu.xml'
    ],
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}