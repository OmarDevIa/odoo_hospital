# Hospital Management Module for Odoo 17

A custom Odoo module for managing basic hospital patient records. This module provides functionality to store and manage patient information in a healthcare setting.

## Features

- Patient management with basic information
  - Name
  - Age
  - Gender
  - Child Status

## Technical Details

### Dependencies
- Odoo 17.0
- Python 3.10 or higher

### Installation

1. Clone this repository into your Odoo addons directory:
```bash
git clone https://github.com/abhisha02/Hospital-Management-Module-for-Odoo-17.git /path/to/odoo/addons/hospital4

```

2. Update your Odoo configuration file to include the addons path:
```
addons_path = /path/to/odoo/addons,/path/to/odoo/addons/hospital4
```

3. Restart Odoo server:
```bash
service odoo restart
# or if running manually
./odoo-bin -c /path/to/odoo.conf
```

4. Install the module:
   - Go to Apps menu in Odoo
   - Click on "Update Apps List"
   - Search for "Nirmala Hospital"
   - Click Install

### Module Structure
```
hospital4/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── patient.py
├── security/
│   └── ir.model.access.csv
└── views/
    ├── menu.xml
    └── patient.xml
```

### Configuration

After installation, the module will be available under the main menu as "Hospital". No additional configuration is required.

## Usage

1. Navigate to Hospital → Operations → Patients
2. Create new patient records with:
   - Basic patient information
   
## Development

### Key Files

- `models/patient.py`: Contains the patient model definition
- `views/patient.xml`: Contains form and tree views for patient records
- `views/menu.xml`: Contains menu structure
- `security/ir.model.access.csv`: Contains access rights



## License

This module is licensed under LGPL-3.

## Author

- Abhisha devi

