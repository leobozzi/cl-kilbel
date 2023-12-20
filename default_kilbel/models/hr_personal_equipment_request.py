# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.translate import _
from odoo.exceptions import ValidationError


class HrPersonalEquipmentRequest(models.Model):
    _inherit = "hr.personal.equipment.request"
    _description = 'hr.personal.equipment.request'

    state = fields.Selection(
        selection_add=[('delivered', 'Entregado')],
        )
    
    def delivered_request(self):
        for rec in self:
            rec.state = 'delivered'