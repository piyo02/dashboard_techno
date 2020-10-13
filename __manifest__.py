{
    'author': "TechnoIndo",
    'name': 'Dashboard TechnoIndo',
    'category': 'Tools',
    'version': '10.0',
    'summary': 'Revamp odoo Dashboard.',
    'description': '''Dashboard Odoo v10.0'''
                   ,
    'depends': ['base', 'web', 'base_setup', 'sale'],
    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'data/sales_data.xml',
        'data/default_data.xml',
        'views/dashboard_techno_view.xml',
        'views/dashboard_techno_item_view.xml',
        'views/dashboard_techno_assets.xml',
        'views/dashboard_action.xml',
    ],
    'qweb': [
        'static/src/xml/ks_dashboard_ninja_templates.xml',
        'static/src/xml/ks_dashboard_ninja_item_templates.xml',
        'static/src/xml/ks_dashboard_ninja_item_theme.xml',
        'static/src/xml/ks_widget_toggle.xml',
        'static/src/xml/ks_dashboard_pro.xml',
        'static/src/xml/ks_import_list_view_template.xml',
    ],
    'images': [''],
    'auto_install': False,
    'installable': True,
    'application': False,
    
    'uninstall_hook': 'uninstall_hook',
}
