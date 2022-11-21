from odoo import models, fields, api


class Patient(models.Model):
    _name = 'hms.patient'

    firstName = fields.Char(string='First name', required=True)
    lastName = fields.Char(string='Last name', required=True)
    birthDate = fields.Date()
    bloodType = fields.Selection([('A+', 'a+'), ('B+', 'b+')])
    history = fields.Html()
    CR_ratio = fields.Float()
    pcr = fields.Boolean()
    image = fields.Binary()
    address = fields.Text()
    age = fields.Integer()

    state = fields.Selection([
        ('Undetermined', 'Undetermined'),
        ('Fair', 'Fair'),
        ('Good', 'Good'),
        ('Serious', 'Serious')
    ])
    patient_logs = fields.One2many('hms.patient_log', 'patient_id')
    doctor_id = fields.Many2one('hms.doctor')
    department_id = fields.Many2one('hms.department')
    department_is_open = fields.Boolean(related='department_id.is_open')

    @api.onchange('state')
    def record_log(self):
        self.env['hms.patient_log'].create({
            'description': f"patient state changed to {self.state}",
            'patient_id': self.id
        })



