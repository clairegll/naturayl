# -*- coding: utf-8 -*-

from odoo import models, fields, api

class shopify_connector(models.Model):
    _name = 'shopify_connector.shopify_connector'
    name = fields.Char(string="Title", required=True)description = fields.Text()
