# -*- coding: utf-8 -*-

from odoo.tests import common
from symbol import try_stmt

class TestRes_partner(common.TransactionCase):
    def setUp(self):
        #
        super(TestRes_partner, self).setUp()
        
        self.contactOdepo=self.env['res.partner'].create({
            'name' : 'Adrien Niokhor SENE',
            'type' : 'contact',
            'phone2' : '+221 33 799 45 34',
            'mobile2' : '+221 77 777 77 77',
            'email2' : 'dev5@gmail.com',
            'skype' : '@dev',
            'rencontre_lors' : 'voyage',
            'don' : True,
            'vendeur' : True,
            'fournisseur' : True,
            'acheteur' : True,
            'backOffice' : False})
        
        self.contactOdepo_Vendeur=self.env['res.partner'].create({
            'name' : 'Adrien Niokhor SENE',
            'vendeur' : True})
        
        self.contactOdepo_backOffice=self.env['res.partner'].create({
            'name' : 'Adrien Niokhor SENE',
            'backOffice' : True})
    
    # Fonction pour tester les champs classique ajoutes par l'heritage au modele res_partner
    
    def test_contactOdepo_Simple(self):
        #Test global
        self.assertEqual(self.contactOdepo.phone2,'+221 33 799 45 34');
        self.assertEqual(self.contactOdepo.mobile2,'+221 77 777 77 77');
        self.assertEqual(self.contactOdepo.email2,'dev5@gmail.com');
        self.assertEqual(self.contactOdepo.skype,'@dev');
        self.assertEqual(self.contactOdepo.rencontre_lors,'voyage');
        self.assertTrue(self.contactOdepo.don);
        self.assertTrue(self.contactOdepo.vendeur);
        self.assertTrue(self.contactOdepo.fournisseur);
        self.assertTrue(self.contactOdepo.acheteur);
        self.assertFalse(self.contactOdepo.backOffice);
        #Test :changement BackOffice <=> changement Vendeur,Fournisseur et Acheteur
        self.contactOdepo.write({
            'backOffice' : True,})
        self.assertTrue(self.contactOdepo.backOffice);
        self.assertFalse(self.contactOdepo.vendeur); # Erreur "AssertionError: True is not false"
        self.assertFalse(self.contactOdepo.fournisseur); # Erreur "AssertionError: True is not false"
        self.assertFalse(self.contactOdepo.acheteur); # Erreur "AssertionError: True is not false"
        #Test :changement vendeur <=> changement BackOffice
        self.contactOdepo.write({
            'vendeur' : True,})
        self.assertFalse(self.contactOdepo.backOffice); # Erreur "AssertionError: True is not false"
        
        # Test sur la valeur par defaut de backOffice si vendeur est True
        self.assertFalse(self.contactOdepo_Vendeur.backOffice);
        
        #Test sur les valeurs par defaut de vendeur,acheteur et fournisseur si backOffice est True
        self.assertFalse(self.contactOdepo_backOffice.vendeur or self.contactOdepo_backOffice.fournisseur or self.contactOdepo_backOffice.acheteur)
    
    #
    def test_ContactOdepo_Complex(self):
        
        self.typeVendeurA=self.env["type.vendeur"].create({
            'name' : 'Vendeur A'});
        self.typeVendeurB=self.env["type.vendeur"].create({
            'name' : 'Vendeur B'});
        self.typeFournisseurA=self.env["type.fournisseur"].create({
            'name' : 'Fournisseur A'});
        self.typeFournisseurB=self.env["type.fournisseur"].create({
            'name' : 'Fournisseur B'})
        self.typeAcheteurA=self.env["type.acheteur"].create({
            'name' : 'Acheteur A'})
        self.typeAcheteurB=self.env["type.acheteur"].create({
            'name' : 'Acheteur B'})
        self.contactOdepo_plus=self.env["res.partner"].create({
            'name' : 'Adrien Niokhor SENE',
            'type_vendeur' : self.typeVendeurA,
            'type_fournisseur' : self.typeFournisseurA,
            'type_acheteur' : self.typeAcheteurA
            })
        
        #Test sur l'attribut type_vendeur
        self.assertEqual(self.contactOdepo_plus.type_vendeur.name,self.typeVendeurA.name)
        self.contactOdepo_plus.write({
            'type_vendeur' : self.typeVendeurB})
        self.assertEqual(self.contactOdepo_plus.type_vendeur.name,self.typeVendeurB.name)
        
        #Test sur l'attribut type_fournisseur
        self.assertEqual(self.contactOdepo_plus.type_fournisseur.name,self.typeFournisseurA.name)
        self.contactOdepo_plus.write({
            'type_fournisseur' : self.typeFournisseurB})
        self.assertEqual(self.contactOdepo_plus.type_fournisseur.name,self.typeFournisseurB.name)
        
        #Test sur l'attribut type_acheteur
        self.assertEqual(self.contactOdepo_plus.type_acheteur.name,self.typeAcheteurA.name)
        self.contactOdepo_plus.write({
            'type_acheteur' : self.typeAcheteurB})
        self.assertEqual(self.contactOdepo_plus.type_acheteur.name,self.typeAcheteurB.name)