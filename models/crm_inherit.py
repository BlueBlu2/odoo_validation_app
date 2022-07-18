from odoo import models, fields, api
from odoo.exceptions import UserError


class CrmInherit(models.Model):
    _inherit = 'res.partner'

    #related_certificate_id = fields.Many2one("cert.certificate")
    certificate_ids = fields.One2many(comodel_name="cert.certificate", inverse_name="customer_id", string="Certifications")

    #cert_user_access_crm_inherit,CERT USER access Crm Inherit,model_crm_inherit,cert.cert_user_group,1,0,0,0
    #cert_manager_access_crm_inherit,CERT Manager access Crm Inherit,model_crm_inherit,cert.cert_manager_group,1,1,1,1