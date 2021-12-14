from odoo import api, models, fields, _
from odoo.exceptions import ValidationError, UserError


class ResPartnerRankVendor(models.Model):
    _name = 'res.partner.rank.vendor'
    _inherit = 'res.partner.rank'
    _description = 'Res Partner Rank - Vendor'

    minimum_amount = fields.Float(
        'Minimum Amount',
        required=True
    )
    code = fields.Char(
        compute='_compute_code',
        store=True,
    )

    # ##########################################
    # Onchange, constraint, compute functions
    # ##########################################

    @api.onchange('name')
    def _onchange_name(self):
        if self.name:
            self.description = self.name

    @api.constrains('minimum_amount')
    def _check_minimum_amount(self):
        for rec in self:
            if rec.minimum_amount <= 0:
                rec.minimum_amount = 100

    @api.depends('name')
    def _compute_code(self):
        for rec in self:
            str_upper_code = ''

            if rec.name:
                str_upper_code = rec.name.upper()

            rec.code = str_upper_code
