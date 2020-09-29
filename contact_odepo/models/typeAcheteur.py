# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
import logging
_logger = logging.getLogger(__name__)

"""
class Acheteur 
"""
class typeAcheteur(models.Model):
	_name = 'type.acheteur'
	_description='Type Acheteur'
	name = fields.Char('type Acheteur', required=True)

