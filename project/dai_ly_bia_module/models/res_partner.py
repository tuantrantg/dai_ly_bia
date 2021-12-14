from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_rank_id = fields.Many2one(
        'res.partner.rank.customer',
        'Customer Rank',
        compute='_compute_customer_rank_id',
    )
    vendor_rank_id = fields.Many2one(
        'res.partner.rank.vendor',
        'Vendor Rank',
        compute='_compute_vendor_rank_id',
    )
    purchase_order_ids = fields.One2many(
        'purchase.order',
        'partner_id',
    )
    total_sale_order_amount = fields.Float(
        compute='_compute_total_sale_order_amount',
    )
    total_purchase_order_amount = fields.Float(
        compute='_compute_total_purchase_order_amount',
    )

    # ##########################################
    # Onchange, constraint, compute functions
    # ##########################################

    def _compute_total_sale_order_amount(self):
        for rec in self:
            rec.total_sale_order_amount = \
                sum(
                    rec.sale_order_ids.filtered(
                        lambda r: r.state in ['sale', 'done']
                    ).mapped('amount_total')
                )

    @api.depends(
        'purchase_order_ids',
        'purchase_order_ids.state',
        'purchase_order_ids.amount_total',
    )
    def _compute_total_purchase_order_amount(self):
        for rec in self:
            rec.total_purchase_order_amount = \
                sum(
                    rec.purchase_order_ids.filtered(
                        lambda r: r.state in ['purchase', 'done']
                    ).mapped('amount_total')
                )

    @api.depends(
        'total_sale_order_amount',
    )
    def _compute_customer_rank_id(self):
        rprc_obj = self.env['res.partner.rank.customer']

        for rec in self:
            found_rank = rprc_obj.search(
                [
                    ('minimum_amount', '<=', rec.total_sale_order_amount)
                ],
                limit=1,
                order='id',
            )

            rec.customer_rank_id = found_rank or False

    @api.depends(
        'total_purchase_order_amount',
    )
    def _compute_vendor_rank_id(self):
        rprc_obj = self.env['res.partner.rank.vendor']

        for rec in self:
            found_rank = rprc_obj.search(
                [
                    ('minimum_amount', '<=', rec.total_purchase_order_amount)
                ],
                limit=1,
                order='id',
            )

            rec.vendor_rank_id = found_rank or False
