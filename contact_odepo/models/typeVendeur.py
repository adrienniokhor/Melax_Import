# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
import logging
_logger = logging.getLogger(__name__)

"""
Class typeVendeur Pour la gestion des Types Vendeurs
"""
class typeVendeur(models.Model):
	_name = 'type.vendeur'
	_description = 'Type Vendeur'
	name = fields.Char('Type Vendeur', required=True)
