from odoo import models, fields

class CertVehicleBrand(models.Model):
    _name = "cert.vehicle.brand"
    _description = "Cert Vehicle Brand"

    name = fields.Char()