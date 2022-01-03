from odoo import models


class ReportFirstXlsx(models.AbstractModel):
    _name = 'report.report_first_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'Report First Xlsx'

    # ##########################################
    # Functions to support main functions
    # ##########################################

    # ==========================================
    # Define format & setup config
    # ==========================================

    def _define_formats(self, workbook):
        res = {}

        # ------------------------
        # Title Format
        # ------------------------

        title_format = {
            'bold': True,
            'font_name': 'Arial',
            'valign': 'vcenter',
        }

        title_format_13 = title_format.copy()
        title_format_13.update({
            'font_size': 13,
            'align': 'center',
        })
        res['title_format_13'] = workbook.add_format(title_format_13)

        # ------------------------
        # Header Format
        # ------------------------

        header_format = {
            'font_size': 9,
            'border': 1,
            'bold': True,
            'text_wrap': True,
            'align': 'center',
            'valign': 'vcenter',
            'font_name': 'Arial',
            'bg_color': '#bfbfbf',
        }
        res['header_format'] = \
            workbook.add_format(header_format)

        # ------------------------
        # Body Format
        # ------------------------

        cell_border_format = {
            'font_size': 8,
            'border': 1,
            'text_wrap': True,
            'valign': 'vcenter',
            'font_name': 'Arial',
        }
        res['cell_border_format'] = \
            workbook.add_format(cell_border_format)

        # ------------------------
        # Footer Format
        # ------------------------

        footer_format = {
            'font_size': 8,
            'valign': 'vcenter',
            'font_name': 'Arial',
        }
        res['footer_format'] = workbook.add_format(footer_format)

        return res

    def _setup_config(self, sheet):
        sheet.set_landscape()
        sheet.set_paper(9)  # Paper 9: A4
        sheet.set_margins(0.05, 0.05, 0.1, 0.1)
        sheet.fit_to_pages(1, 1)
        sheet.set_header('', {'margin': 0})
        sheet.set_footer('', {'margin': 0})
        sheet.center_horizontally()

        sheet.set_column('A:A', 15)
        sheet.set_column('B:B', 15)
        sheet.set_column('C:C', 15)
        sheet.set_column('D:D', 15)
        sheet.set_column('E:E', 15)
        sheet.set_column('F:F', 15)

    # ==========================================
    # Handle Data
    # ==========================================

    def _get_data(self, objects):
        sql = """
SELECT
    rp.id,
    rp.create_date,
    rp.name,
    rp.email,
    rp.phone,
    rp.mobile
FROM
    res_partner rp
WHERE
    rp.create_date >= %(from_creation_datetime)s
    AND rp.create_date <= %(to_creation_datetime)s
ORDER BY
    rp.id
        """

        sql_args = {
            'from_creation_datetime': objects.from_datetime,
            'to_creation_datetime': objects.to_datetime,
        }

        self._cr.execute(sql, sql_args)

        if not self._cr.rowcount:
            return []

        res = self._cr.dictfetchall()

        return res

    # ==========================================
    # Generate Report
    # ==========================================

    def _generate_title(self, sheet):
        sheet.merge_range(
            0, 0, 0, 4,
            'Sample Report XLSX',
            self._context['title_format_13'],
        )

    def _generate_header(self, sheet):
        sheet.write(
            2, 0,
            'ID',
            self._context['header_format'],
        )
        sheet.write(
            2, 1,
            'Name',
            self._context['header_format'],
        )
        sheet.write(
            2, 2,
            'Email',
            self._context['header_format'],
        )
        sheet.write(
            2, 3,
            'Phone',
            self._context['header_format'],
        )
        sheet.write(
            2, 4,
            'Mobile',
            self._context['header_format'],
        )

    def _generate_body(self, sheet, data):
        row = 3

        for item in data:
            sheet.write(
                row, 0,
                item['id'],
                self._context['cell_border_format'],
            )
            sheet.write(
                row, 1,
                item['name'],
                self._context['cell_border_format'],
            )
            sheet.write(
                row, 2,
                item['email'],
                self._context['cell_border_format'],
            )
            sheet.write(
                row, 3,
                item['phone'],
                self._context['cell_border_format'],
            )
            sheet.write(
                row, 4,
                item['mobile'],
                self._context['cell_border_format'],
            )

            row += 1

        return row

    def _generate_footer(self, sheet, row):
        row += 1

        sheet.write(
            row, 4,
            'Signature',
            self._context['footer_format'],
        )

        sheet.write(
            row + 4, 4,
            'Nguyen Van A',
            self._context['footer_format'],
        )

    # ##########################################
    # Main functions
    # ##########################################

    def generate_xlsx_report(self, workbook, data, objects):
        self = self.with_context(self._define_formats(workbook))

        sheet = workbook.add_worksheet('First Sheet')

        self._setup_config(sheet)

        # Get data first
        raw_data = self._get_data(objects)

        # Generate report content
        self._generate_title(sheet)
        self._generate_header(sheet)
        last_row = self._generate_body(sheet, raw_data)
        self._generate_footer(sheet, last_row)
