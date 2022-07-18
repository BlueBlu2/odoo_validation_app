from odoo import models, fields


class CertTestInherit(models.Model):
    _name = "cert.test.inherit"
    _description = "Cert Test Inherit"

    customer_id = fields.Many2one(comodel_name="res.partner")
    name = fields.Char()