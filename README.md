# odepov13

### Execution des Tests Odoo avec Docker ########
Aprés l'écriture des tests ,on doit  pouvoir les exécuter. Pour se faire on doit utiliser les drapeaux ci-dessous:

    *	--test-enable, permet d’activer l’exécution des tests
    *	-i {modules_à_tester}, permet de préciser le module sur lequel les tests seront faites,s'il y'a plusieurs modules à tester on doit les séparer avec des virgiles et le tout entre des guillemets simple ou double.
## Exemple d'execution des tests de notre module odoo avec docker
  
     *Installer PostgreSQL server avec docker:
     
     docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name db postgres:10
     
     *Installer Odoo avec docker et ajout des drapeaux pour l'exécution des tests:
     
     docker run -v ~/odoo/modules:/mnt/extra-addons -p 80:8069 --name odoo --link db:db -t odoo --test-enable -i 'contact_odepo'
     
     *Apres l'installation d'Odoo sur Docker ,on  peut toutefois demarrer l'image Odoo et afficher les résultats des tests sur la console avec la commande suivante.
     NB:Il faut d'abord démarrer la base de données s'il n'est pas en marche comme suite: sudo docker start db
     
     sudo docker start odoo && sudo docker attach odoo
     
## Résultats des tests sur la console

	2020-09-18 15:38:33,503 1 INFO db odoo.modules.module: odoo.addons.contact_odepo.tests.test_res_partner running tests. 
	2020-09-18 15:38:33,504 1 INFO db odoo.addons.contact_odepo.tests.test_res_partner: Starting TestRes_partner.test_ContactOdepo_Complex ... 
	2020-09-18 15:38:33,697 1 INFO db odoo.addons.contact_odepo.tests.test_res_partner: Starting TestRes_partner.test_contactOdepo_Simple ... 
	2020-09-18 15:38:33,754 1 INFO db odoo.addons.contact_odepo.tests.test_res_partner: ====================================================================== 
	2020-09-18 15:38:33,755 1 ERROR db odoo.addons.contact_odepo.tests.test_res_partner: FAIL: TestRes_partner.test_contactOdepo_Simple
	Traceback (most recent call last):
	  File "/usr/lib/python3/dist-packages/odoo/modules/registry.py", line 60, in __new__
	    return cls.registries[db_name]
	KeyError: 'db'

	During handling of the above exception, another exception occurred:

	Traceback (most recent call last):
	  File "/mnt/extra-addons/contact_odepo/tests/test_res_partner.py", line 51, in test_contactOdepo_Simple
	    self.assertFalse(self.contactOdepo.vendeur); # Erreur "AssertionError: True is not false"
	AssertionError: True is not false
	 
	2020-09-18 15:38:33,758 1 INFO db odoo.modules.module: Ran 2 tests in 0.255s 
	2020-09-18 15:38:33,759 1 ERROR db odoo.modules.module: Module contact_odepo: 1 failures, 0 errors 
	2020-09-18 15:38:33,775 1 INFO db odoo.modules.loading: 31 modules loaded in 2.01s, 98 queries 
	2020-09-18 15:38:33,989 1 ERROR db odoo.modules.loading: At least one test failed when loading the modules. 
	
##

