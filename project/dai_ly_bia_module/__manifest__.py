{
    'name' : 'Dai Ly Bia Module',
    'version' : '1.1',
    'summary': 'Dai Ly Bia Module',
    'sequence': 16,
    'description': """
    """,
    'category': 'Sales',
    'website': 'https://github.com/tuantrantg/dai_ly_bia',
    'depends': [
        'contacts',
        'sale_management',
        'purchase',
        'stock',
        'report_xlsx',
    ],
    'data': [
        # ============================================================
        # SECURITY SETTING - GROUP
        # ============================================================
        # 'security/',

        # ============================================================
        # DATA
        # ============================================================
        # 'data/',

        # ============================================================
        # VIEWS
        # ============================================================
        # 'views/',
        'views/res_partner_view.xml',
        'views/res_partner_rank_view.xml',
        'views/res_partner_rank_view_2.xml',  # Đây chỉ là vd, nên tách ra module riêng
        'views/res_partner_rank_view_3.xml',  # Đây chỉ là vd, nên tách ra module riêng
        'views/sale_order_view.xml',

        # ============================================================
        # REPORT
        # ============================================================
        # 'reports/',
        'reports/sale_report_templates.xml',
        'reports/sale_report.xml',
        'reports/report_first_xlsx_report.xml',

        # ============================================================
        # WIZARD
        # ============================================================
        # 'wizard/',
        'wizards/first_wizard_wizard.xml',
        'wizards/first_xlsx_report_wizard.xml',

        # ============================================================
        # MENU
        # ============================================================
        # 'menu/',
    ],
    'qweb': [],
    'test': [],
    'demo': [],
    'installable': True,
    'application': True,
}
