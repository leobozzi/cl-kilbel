# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.translate import _
from odoo.exceptions import ValidationError


class HrAttendance(models.Model):
    _inherit = "hr.attendance"
    _description = 'hr.attendance'

    branch = fields.Char(
        string="Branch",
        related='employee_id.work_location_id.name',
        store=True,
    )
    assigned_turn = fields.Char(
        string="Assigned Turn",
        related='employee_id.resource_calendar_id.name',
        store=True,
    )
    job = fields.Char(
        string="Job",
        related='employee_id.job_id.name',
        store=True,
    )
    
