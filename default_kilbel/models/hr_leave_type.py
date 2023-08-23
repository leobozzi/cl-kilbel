# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.translate import _


class HrLeaveType(models.Model):
    _inherit = "hr.leave.type"
    _description = 'hr.leave.type'

    remunerative_leave_type = fields.Selection(
        selection=[
            ('remunerative', 'Remunerative'),
            ('non-remunerative', 'Non Remunerative')],
        string="Leave Type",
        #default='remunerative',
    )
