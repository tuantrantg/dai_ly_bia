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

        # ============================================================
        # REPORT
        # ============================================================
        # 'reports/',

        # ============================================================
        # WIZARD
        # ============================================================
        # 'wizard/',

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