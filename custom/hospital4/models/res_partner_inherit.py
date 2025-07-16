from odoo import models, fields, api
from datetime import date


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    is_patient = fields.Boolean(string='Est un patient')
    is_doctor = fields.Boolean(string='Est un médecin')
    birth_date = fields.Date(string='Date de naissance')
    doctor_notes = fields.Text(string='Notes du médecin')

    # Correction du champ Many2many
    doctor_ids = fields.Many2many(
        'res.partner',
        'res_partner_doctor_rel',
        'patient_id',
        'doctor_id',
        string='Liste des médecins',
        domain=[('is_doctor', '=', True)]
    )

    @api.depends('birth_date')
    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.birth_date:
                birth_date = fields.Date.from_string(record.birth_date)
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                record.age = age
            else:
                record.age = 0

    age = fields.Integer(string='Âge', compute='_compute_age', store=True)