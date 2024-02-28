# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.translate import _
from odoo.exceptions import ValidationError


class HrEmployeePublic(models.Model):
    _inherit = "hr.employee.public"
    _description = 'hr.employee.public'

    cashier_number = fields.Char(
        related='employee_id.cashier_number',
    )
    file_number = fields.Char(
        related='employee_id.file_number',
    )

    