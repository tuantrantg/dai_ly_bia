import json
from lxml import etree

from odoo import api, models, fields, _
from odoo.exceptions import UserError


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
    status = fields.Selection(
        [
            ('new', 'New'),
            ('old', 'Old'),
        ],
        'Status',
    )
    active = fields.Boolean(
        'Active',
        default=True,
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

    # ##########################################
    # Main functions
    # ##########################################

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        # print('\n\n\n> search >>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # print('\n==== self ====', self)
        # print('\n==== self._context ====', self._context)
        # print('\n')

        res = super(ResPartnerRank, self).search(
            args, offset=offset, limit=limit, order=order, count=count
        )

        return res

    @api.model
    def fields_view_get(self, view_id=None, view_type='form',
                        toolbar=False, submenu=False):
        # print('\n\n\n> fields_view_get >>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # print('\n==== self ====', self)
        # print('\n==== view_id ====', view_id)
        # print('\n==== view_type ====', view_type)
        # print('\n==== toolbar ====', toolbar)
        # print('\n==== submenu ====', submenu)
        # print('\n==== self._context ====', self._context)

        res = super().fields_view_get(
            view_id=view_id,
            view_type=view_type,
            toolbar=toolbar,
            submenu=submenu
        )

        doc = etree.XML(res['arch'])

        # print('\n==== doc ====', doc)
        # print('\n')

        for node in doc.xpath("//field[@name='name']"):
            # node.set("readonly", "1")
            node.set("string", "[ NEW ] label of Name")

            # # Take care `modifiers`
            # modifiers = json.loads(node.get("modifiers"))
            # modifiers['readonly'] = True
            # node.set("modifiers", json.dumps(modifiers))

        res['arch'] = etree.tostring(doc, encoding='unicode')

        return res

    @api.model
    def create(self, vals):
        # print('\n\n\n> create >>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # print('\n@@ self @@', self)
        # print('\n@@ self._context @@', self._context)
        # print('\n')

        res = super().create(vals)

        return res

    # ##########################################
    # Main functions
    # ##########################################

    def btn_primary_1(self):
        # print('\n\n\n> btn_primary_1 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # print('\n@@ self @@', self)
        # print('\n@@ self._context @@', self._context)
        # print('\n')

        # self._context is frozen dictionary
        ctx = self._context.copy()
        ctx.update({'day_la_khach_hang': 2})

        self = self.with_context(ctx)

        res = self.search([])

        raise UserError(_('This is Primary 1'))
