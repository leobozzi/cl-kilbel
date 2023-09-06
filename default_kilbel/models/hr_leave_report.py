# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.translate import _


class HrLeaveReport(models.Model):
    _inherit = "hr.leave.report"
    _description = 'hr.leave.report'

    leave_category = fields.Selection(
        related='holiday_status_id.leave_category',
    )
