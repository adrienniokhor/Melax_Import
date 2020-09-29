# -*- coding: utf-8 -*-


from odoo import models,fields,api, exceptions
import logging
_logger = logging.getLogger(__name__)

class OdepoContact(models.Model):
    _inherit = "res.partner"

    """ Informations generales du Contact """
    #Tel2
    phone2 = fields.Char(string="Telephone 2")
    #Mobile
    mobile2 = fields.Char(string="Mobile 2")
    #Courriel2
    email2 = fields.Char(string="Email 2")
    #Skype
    skype = fields.Char(string="Skype")
    #Meet
    rencontre_lors = fields.Char(string="Rencontré lors de")
    #Donation
    don = fields.Boolean('Don', help="Check this box if this contact make Donation.")

    vendeur = fields.Boolean('Vendeur', help="Check this box if this contact is a Seller.")
    fournisseur = fields.Boolean('Fournisseur', help="Check this box if this contact is a Seller.")
    acheteur = fields.Boolean("Acheteur")
    backOffice= fields.Boolean('BackOffice')

    """Tab Vendeur"""

    type_vendeur = fields.Many2many('type.vendeur',domain=[('name','!=', 0)], string="Type vendeur")
    acheteur_attache = fields.Many2one('res.users', 'Acheteur attaché')
    type_fournisseur = fields.Many2many('type.fournisseur',domain=[('name','!=', 0)], string="Type fournisseur")

    """Tab Acheteur et fournisseur"""
    type_acheteur = fields.Many2many('type.acheteur',domain=[('name','!=', 0 )], string="Type acheteur")
    commercial_attache = fields.Many2one('res.users', 'Commercial attaché')

    export = fields.Boolean('Export')
    nbre_magasin= fields.Integer('Nombre magasin')
    condition_achat = fields.Text('Condition d\'achat')
    societe_transport=fields.Many2one('res.partner','Societe transport')
    contact_transport=fields.Many2one('res.partner','Contact transport')
    pays_vente=fields.Many2one('res.country','Pays vente')
    zone_vente=fields.Many2one('res.country.group','Zone vente')

    """Tab BacOffice"""

    """fonction pour gérer le type backoffice"""
    @api.onchange('backOffice')
    def on_change_backOffice(self):
    	if self.backOffice == True:
	      self.acheteur= False
	      self.vendeur = False
	      self.fournisseur = False
    """fonction pour gérer les acheteurs"""
    @api.onchange('acheteur')
    def on_change_acheteur(self):
        if self.acheteur == True:
            self.backOffice = False
    """fonction pour gérer les vendeurs"""
    @api.onchange('vendeur')
    def on_change_vendeur(self):
        if self.vendeur == True:
            self.backOffice = False
    """fonction pour gérer les fournisseurs"""
    @api.onchange('fournisseur')
    def on_change_fournisseur(self):
        if self.fournisseur == True:
            self.backOffice = False


