from odoo import models, fields


class Department(models.Model):
    _name = 'hms.department'

    name = fields.Char()
    capacity = fields.Integer()
    is_open = fields.Boolean()
    patients_ids = fields.One2many('hms.patient', 'department_id')
    # doctors = fields.Many2many('hms.doctor')
