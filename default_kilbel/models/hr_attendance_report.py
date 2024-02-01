# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.translate import _
from odoo.exceptions import ValidationError

import datetime

class HrAttendanceReport(models.Model):
    _inherit = "hr.attendance.report"
    _description = 'hr.attendance.report'

    day_of_week = fields.Char(
        string="Día",
        compute='_compute_day_of_week',
    )

    @api.depends("check_in")
    def _compute_day_of_week(self):
        for rec in self:
            if datetime.datetime.weekday(rec.check_in) == 0:
                rec.day_of_week = "Lunes"
            elif datetime.datetime.weekday(rec.check_in) == 1:
                rec.day_of_week = "Martes"
            elif datetime.datetime.weekday(rec.check_in) == 2:
                rec.day_of_week = "Miércoles"
            elif datetime.datetime.weekday(rec.check_in) == 3:
                rec.day_of_week= "Jueves"
            elif datetime.datetime.weekday(rec.check_in) == 4:
                rec.day_of_week = "Viernes"
            elif datetime.datetime.weekday(rec.check_in) == 5:
                rec.day_of_week = "Sábado"
            elif datetime.datetime.weekday(rec.check_in) == 6:
                rec.day_of_week = "Domingo"
            #rec.day_of_week = rec.check_in.strftime('%A')


    