{
    'name': 'EMS Hospital',
    'author': 'Omar Atta',
    'version': '17.0.1.0',    # Changed to match Odoo version format
    'summary': 'A module for hospital management',
    'description': 'A module for hospital management',  # Added description
    'category': 'Healthcare',
    'license': 'LGPL-3',      # Added license field
    'depends': ['base','contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient.xml',
        'views/docteur.xml',  # Nouv fichier à créer
        'views/res_partner_inherit.xml',
        'views/appointment_views.xml',
        'views/invoice_views.xml',
        'views/specialty_views.xml',
    ],               # Added data field for views/security files
    'installable': True,
    'application': True,
    'sequence': 1,            # Added sequence for Apps list ordering
}
