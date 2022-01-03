from odoo import api, fields, models


class FirstWizard(models.TransientModel):
    _name = 'first.wizard'
    _description = 'First Wizard'

    from_date = fields.Date(
        'From Date',
        required=True,
    )
    to_date = fields.Date(
        'To Date',
        required=True,
    )

    # ##########################################
    # Main functions
    # ##########################################

    def btn_click_me(self):
        print('\n\n\n\n=== [ Do something in here, please!!! ]===\n\n\n\n')
        print('\n\n> FirstWizard > btn_click_me >>>>>>>>>>>>>>>>>>>>>>>>')
        print('@@@ self @@@', self)
        print('@@@ self._context @@@', self._context)
        print('\n\n')

        ctx_sale_order_id = self._context.get('active_id', False)

        if ctx_sale_order_id:
            sale_order = self.env['sale.order'].browse(ctx_sale_order_id)

            res = self.env.ref(
                'dai_ly_bia_module.action_report_saleorder_2'
            ).report_action(sale_order)

            return res

        return True
