from odoo import models, fields


class HospitalSpecialty(models.Model):
    _name = 'hospital.specialty'
    _description = 'Spécialité médicale'

    name = fields.Char(string="Nom", required=True)
