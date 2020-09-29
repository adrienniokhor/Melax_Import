# -*- coding: utf-8 -*-
{
    'name': "Module: Odepo Contact",
    'summary': """
        Module qui s'occupe de la gestion des contacts de la societé Odepo""",
    'description': """
		Module qui s'occupe de la gestion des contacts d'odepo
        Ce module ajoute divers champs qui sont propre à la sociéte Odepo.
	    Il dispose de nouveaux onglets Spéciales:
		-Tab Acheteur|
		-Tab Vendeur|
		-Tab Fournisseur.
    """,
    'author':"" ,
    'website': "Odepo.fr",
    'application': True,
    'installable': True,
    'category':"" ,
    'version': '0.1',
    'depends': ['crm'],
    'data': [
            'views/contact_view.xml',
	        'security/security.xml',
            'security/ir.model.access.csv',
    ],
    'demo': [
        ],
     "js": [
        ],

    "qweb" : [
    ],
}
