from datetime import datetime

from odoo import models, fields, api, _


class CertCertificateType(models.Model):
    _name = "cert.certificate"
    _description = "Cert Certificate"
    _rec_name = "customer_id"

    serial_number = fields.Char(string="Serial number", required=True, copy=False, readonly=True, index=True,
                                default=lambda self: _("New"))

    """Car, Bus, Minibus, Microbus"""
    vehicle_type = fields.Selection([
        ("car", "Car"),
        ("bus", "Bus"),
        ("minibus", "Minibus"),
        ("microbus", "Microbus")
    ])

    certificate_type = fields.Many2one(comodel_name="cert.certificate.type")
    traffic_department = fields.Many2one(comodel_name="cert.traffic.department")
    customer_id = fields.Many2one(comodel_name="res.partner")
    price = fields.Integer()
    motor_number = fields.Char()
    chassis_number = fields.Char()
    #car_model = fields.Char()
    car_model = fields.Selection(
          [(str(num), str(num)) for num in range((datetime.now().year - 20), (datetime.now().year + 1))], 'Year')
    # car_model = fields.Selection([(num, str(num)) for num in range(1900, datetime.now().year + 1)], 'Year')
    Brand = fields.Many2one(comodel_name="cert.vehicle.brand")
    print_history_ids = fields.One2many('cert.print.history', 'certificate_id')
    reprint_report = fields.Boolean()


    @api.model
    def create(self, vals):
        if vals.get("serial_number", _("New")) == _("New"):
            vals["serial_number"] = self.env['ir.sequence'].next_by_code('cert.serial') or _("New")
        res = super().create(vals)
        return res

    def allow_reprint(self):
        self.reprint_report = True