from odoo import models, fields


class CertTrafficDepartment(models.Model):
    _name = "cert.traffic.department"
    _description = "Cert Traffic Department"

    name = fields.Char()