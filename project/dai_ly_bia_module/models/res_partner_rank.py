from odoo import api, models, fields


class ResPartnerRank(models.Model):
    _name = 'res.partner.rank'
    _description = 'Res Partner Rank'

    name = fields.Char(
        string='Name',
        required=True,
    )
    code = fields.Char(
        'Code',
    )
    description = fields.Text(
        'Description',
    )

    # ##########################################
    # Onchange, constraint, compute functions
    # ##########################################

    @api.model
    def create(self, vals):
        vals_name = vals.get('name', False)
        vals_code = vals.get('code', False)
        vals_description = vals.get('description', False)

        if not vals_code:
            vals.update({
                'code': vals_name.upper()
            })

        if not vals_description:
            vals.update({
                'description': vals_name
            })

        res = super().create(vals)

        return res

