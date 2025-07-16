from odoo import models, fields


class HospitalInvoice(models.Model):
    _name = 'hospital.invoice'
    _description = 'Factures de l’hôpital'

    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    appointment_id = fields.Many2one('hospital.appointment', string="Rendez-vous", required=False)
    amount = fields.Float(string="Montant total", required=True)
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('paid', 'Payé'),
        ('unpaid', 'Non payé')
    ], string="État", default='unpaid')
