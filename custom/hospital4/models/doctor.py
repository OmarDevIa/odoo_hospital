from odoo import models, fields


class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Médecin'

    name = fields.Char(string='Nom', required=True)
    _specialties_ids = fields.Many2many(
    'hospital.specialty', string="Spécialités"
)
    partner_id = fields.Many2one('res.partner', string="Contact associé")
    user_id = fields.Many2one('res.users', string="Utilisateur Odoo")

    # Ajoutez d'autres champs spécifiques aux médecins si nécessaire


class ResPartner(models.Model):
    _inherit = 'res.partner'  # Hérite du modèle res.partner

    # Champ pour identifier si le partenaire est un médecin
    is_doctor = fields.Boolean(string="Est un Médecin", default=False)

    # Champ spécialités associé au médecin
    specialties_ids = fields.Many2many(
        'hospital.specialty',  # Modèle des spécialités (à créer si nécessaire)
        string="Spécialités"
    )