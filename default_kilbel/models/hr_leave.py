# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.translate import _


class HrLeave(models.Model):
    _inherit = "hr.leave"
    _description = 'hr.leave'

    leave_category = fields.Selection(
        related='holiday_status_id.leave_category',
    )
