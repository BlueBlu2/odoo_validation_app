from odoo import models, fields

class PrintHistory(models.Model):
    _name = "cert.print.history"
    certificate_id = fields.Many2one('cert.certificate')