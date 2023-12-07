# -*- coding: utf-8 -*-

from odoo import models, fields, api

class shopify_connector(models.Model):
    _name = 'shopify_connector.shopify_connector'

    name = fields.Char()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100