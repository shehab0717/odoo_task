from odoo import models, fields


class Doctor(models.Model):
    _name = 'hms.doctor'
    name = fields.Char()
    patients_ids = fields.One2many('hms.patient', 'doctor_id')
    # departments = fields.Many2many('hms.department')
