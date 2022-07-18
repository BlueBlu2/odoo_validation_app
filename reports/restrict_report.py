from odoo import api, models
from odoo.exceptions import ValidationError

class RestrictReport(models.AbstractModel):
    _name = 'cert.cert_certificate_template'
    _description = "change print behavior"

    @api.model
    def _get_report_values(self, docids, data):
        current = self.env["cert.certificate"].browse(docids)
        if self.env.user.has_group('cert.cert_user_group'):
            if not current.allow_reprint_report:
                raise ValidationError('You can not print the report again')
        self.env["cert.print.history"].create({"cert_id": current.id})
        return dict(doc_ids=docids, doc_model=self.env['cert.certificate'], data=data)