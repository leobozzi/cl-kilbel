# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.translate import _
from odoo.exceptions import ValidationError


class HrEmployee(models.Model):
    _inherit = "hr.employee"
    _description = 'hr.employee'

    def write(self, vals):
        res = super(HrEmployee, self).write(vals)
        for rec in self:
            if 'active' in vals:
                if vals['active'] == False:
                    hr_contract_ids = rec.env['hr.contract'].search([('employee_id','=',rec.id),('active','=',True)])
                    for hr_contract_id in hr_contract_ids:
                        hr_contract_id.active = False
                else:
                    hr_contract_ids = rec.env['hr.contract'].search([('employee_id','=',rec.id),('active','=',False)])
                    for hr_contract_id in hr_contract_ids:
                        hr_contract_id.active = True
        return res