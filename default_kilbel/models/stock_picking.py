# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.translate import _
from odoo.exceptions import ValidationError


class StockPicking(models.Model):
    _inherit = "stock.picking"
    _description = 'stock.picking'

    work_location_id = fields.Many2one(
        related='partner_id.employee_ids.work_location_id',
        string="Sucursal",
        store=True,
    )
