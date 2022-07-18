from odoo import models, fields


class CertCertificateType(models.Model):
    _name = "cert.certificate.type"
    _description = "Cert Certificate Type"

    name = fields.Char()
