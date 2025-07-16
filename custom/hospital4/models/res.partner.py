from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'  # Hérite de res.partner

    is_doctor = fields.Boolean(string="Est Médecin", default=False)  # Marqueur pour les médecins
    specialties_ids = fields.Many2many(
        'hospital.specialty', string="Spécialités"
    )  # Lien avec les spécialités
