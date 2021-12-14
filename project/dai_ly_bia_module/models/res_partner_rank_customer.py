from odoo import api, models, fields


class ResPartnerRankCustomer(models.Model):
    _name = 'res.partner.rank.customer'
    _inherits = {
        'res.partner.rank': 'partner_rank_id',
    }
    _description = 'Res Partner Rank - Customer'

    partner_rank_id = fields.Many2one(
        'res.partner.rank',
        'Partner Rank',
    )
    minimum_amount = fields.Float(
        'Minimum Amount',
        required=True
    )
