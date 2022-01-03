from odoo import api, fields, models


class FirstXlsxReportWizard(models.TransientModel):
    _name = 'first.xlsx.report.wizard'
    _description = 'First Xlsx Report Wizard'

    from_datetime = fields.Datetime(
        'From Creation Datetime',
        required=True,
    )
    to_datetime = fields.Datetime(
        'To Creation Datetime',
        required=True,
    )

    # ##########################################
    # Main functions
    # ##########################################

    def btn_print_report(self):
        self.ensure_one()

        report = self.env.ref(
            'dai_ly_bia_module.report_first_xlsx'
        )

        res = report.report_action(self.id)

        return res
