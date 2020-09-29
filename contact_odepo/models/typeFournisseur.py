# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
import logging
_logger = logging.getLogger(__name__)

"""
class typeFournisseur pour la gestion des Types Fournisseurs
"""
class typeFournissuer(models.Model):
	_name = 'type.fournisseur'
	_description = 'Type Fournisseur'
	name = fields.Char('Type Fournisseur', required=True)
