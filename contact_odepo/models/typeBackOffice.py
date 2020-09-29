# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
import logging
_logger = logging.getLogger(__name__)

"""
class typeBackOffice
"""
class typeBackOffice(models.Model):
        _name = 'type.backoffice'
        _description = 'Type BackOffice'
        type_backoffice = fields.Char('Type BackOffice', required=True)

