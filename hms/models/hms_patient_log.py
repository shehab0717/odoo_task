from odoo import models, fields


class PatientLog(models.Model):
    _name = 'hms.patient_log'

    date = fields.Date(required=True, default=fields.Date.context_today)
    description = fields.Text(default="N/A")
    patient_id = fields.Many2one('hms.patient')