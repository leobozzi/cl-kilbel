# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.translate import _


class HrLeaveReport(models.Model):
    _inherit = "hr.leave.report"
    _description = 'hr.leave.report'

    remunerative_leave_type = fields.Selection(
        related='holiday_status_id.remunerative_leave_type',
    )
