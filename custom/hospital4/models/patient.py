from odoo import models, fields, api


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Records'

    # Champs
    name = fields.Char(string="Nom du patient", required=True)

    date_naissance = fields.Date(string="Date de naissance")
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    gender = fields.Selection([('male', 'Homme'), ('female', 'Femme')], string="Genre")
    note_docteur = fields.Text(string="Note du docteur")
    docteur_ids = fields.Many2many('hospital.doctor', string="Liste des docteurs")

    # Calcul automatique de l'âge à partir de la date de naissance
    @api.depends('date_naissance')
    def _compute_age(self):
        for patient in self:
            if patient.date_naissance:
                today = fields.Date.today()
                patient.age = today.year - patient.date_naissance.year
            else:
                patient.age = 0

    # Exemple de méthode dépendante (non utilisée actuellement dans votre code)
    @api.depends('age')
    def _compute_is_child(self):
        for patient in self:
            patient.is_child = patient.age < 18 if patient.age else False

    class ResPartner(models.Model):
        _inherit = 'res.partner'  # Hérite du modèle res.partner

        # Champ pour identifier si le partenaire est un médecin
        is_patient = fields.Boolean(string="Est un Patient", default=False)



    # Méthode appelée par le bouton pour ouvrir les Contacts
    def open_contacts_action(self):
        """Action déclenchée à partir du bouton pour ouvrir la vue Contact"""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Contacts',
            'res_model': 'res.partner',
            'view_mode': 'tree,form',
            'target': 'current',  # Ouvre dans la même fenêtre
        }

def name_get(self):
    result = []
    for rec in self:
        label = f"Patient #{rec.id}"
        if rec.partner_id:
            label = f"{rec.partner_id.name} (Patient)"
        result.append((rec.id, label))
    return result
