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

        return True
