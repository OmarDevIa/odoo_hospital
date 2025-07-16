from odoo import models, fields, api


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Rendez-vous médicaux'

    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    doctor_id = fields.Many2one('hospital.doctor', string="Docteur", required=True)
    date_appointment = fields.Datetime(string="Date du rendez-vous", required=True)
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('confirmed', 'Confirmé'),
        ('done', 'Effectué'),
        ('cancelled', 'Annulé'),
    ], string="État", default='draft')
