
{
    'name': 'Ecole Management 2020',
    'version': '14.0.1',
    'category': 'Extra Tools',
    'description': """Ecole management tool system""",
    'summary': """Ecole management tool system""",
    'website': 'N/A',
    'sequence': '10',
    'license': 'AGPL-3',
    'author': "michael",
    'maintainer': 'michael',
    'depends': ['mail', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/school.xml',
        'reports/report.xml',
        'reports/patient_card.xml',
        'reports/check_print_card.xml',

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
