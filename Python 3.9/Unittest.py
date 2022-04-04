import unittest

from clss import Personne
from clss import Client
from clss import Acteur
from clss import Employe
from clss import CarteCredit
from clss import Film
from clss import Categorie
from MonProjet import Ui_Login

class testPersonne(unittest.TestCase):


    def test_user(self):
        print ('test nom')
        p1 = Personne('Dany', 'Gauthier', 'Male')
        self.assertEqual(p1.get_nom(), 'Dany')
        self.assertEqual(p1.get_prenom(), 'Gauthier')
        self.assertEqual(p1.get_sexe(),'Male')

    def test_Client(self):
        print('test client')
        c1 = Client('Dany', 'Gauthier', 'Male', '11 decembre', 'test@test.test', '123456')
        self.assertEqual(c1.get_nom(), 'Dany')
        self.assertEqual(c1.get_prenom(), 'Gauthier')
        self.assertEqual(c1.get_sexe(),'Male')
        self.assertEqual(c1.getdateInsc(), '11 decembre')
        self.assertEqual(c1.getcourriel(), 'test@test.test')
        self.assertEqual(c1.getpassword(),'123456')

    def test_Acteur(self):
        print('test Acteur')
        a1 = Acteur('Dany', 'Gauthier', 'Male', 'clown', '11 decembre', '12 decembre')
        self.assertEqual(a1.get_nom(), 'Dany')
        self.assertEqual(a1.get_prenom(), 'Gauthier')
        self.assertEqual(a1.get_sexe(), 'Male')
        self.assertEqual(a1.getpersonage(), 'clown')
        self.assertEqual(a1.getdemploi(), '11 decembre')
        self.assertEqual(a1.getfemploi(), '12 decembre')

    def test_Employe(self):
        print('test Employe')
        e1 = Employe('Dany', 'Gauthier', 'Male', '11 decembre', 'noir', 'bleu')
        self.assertEqual(e1.get_nom(), 'Dany')
        self.assertEqual(e1.get_prenom(), 'Gauthier')
        self.assertEqual(e1.get_sexe(), 'Male')
        self.assertEqual(e1.getdateEmbauche(), '11 decembre')
        self.assertEqual(e1.getcodeUser(), 'noir')
        self.assertEqual(e1.getmdp(), 'bleu')

    def test_CarteCredit(self):
        print('test Carte de crédit')
        c1 = CarteCredit('Dany', 'Gauthier', 'Male', '234789756123', '10 juin', '89341')
        self.assertEqual(c1.get_nom(), 'Dany')
        self.assertEqual(c1.get_prenom(), 'Gauthier')
        self.assertEqual(c1.get_sexe(), 'Male')
        self.assertEqual(c1.getcarte(), '234789756123')
        self.assertEqual(c1.getexpiration(), '10 juin')
        self.assertEqual(c1.getcode(), '89341')

    def test_Film(self):
        print('test Carte de film')
        f1 = Film('Dany', 'Gauthier', 'Male', 'clown', '11 decembre', '12 decembre', 'Sable rouge', 'plate')
        self.assertEqual(f1.get_nom(), 'Dany')
        self.assertEqual(f1.get_prenom(), 'Gauthier')
        self.assertEqual(f1.get_sexe(), 'Male')
        self.assertEqual(f1.getpersonage(), 'clown')
        self.assertEqual(f1.getdemploi(), '11 decembre')
        self.assertEqual(f1.getfemploi(), '12 decembre')
        self.assertEqual(f1.getnom_film(), 'Sable rouge')
        self.assertEqual(f1.get_description(), 'plate')

    def test_Categorie(self):
        print('test Carte de film')
        cat = Categorie('Dany', 'Gauthier', 'Male', 'clown', '11 decembre', '12 decembre', 'Sable rouge', 'plate', 'Comedie', 'un peu drole')
        self.assertEqual(cat.get_nom(), 'Dany')
        self.assertEqual(cat.get_prenom(), 'Gauthier')
        self.assertEqual(cat.get_sexe(), 'Male')
        self.assertEqual(cat.getpersonage(), 'clown')
        self.assertEqual(cat.getdemploi(), '11 decembre')
        self.assertEqual(cat.getfemploi(), '12 decembre')
        self.assertEqual(cat.getnom_film(), 'Sable rouge')
        self.assertEqual(cat.get_description(), 'plate')
        self.assertEqual(cat.getcat_nom(), 'Comedie')
        self.assertEqual(cat.getcat_description(), 'un peu drole')

    def test_login(self, Ui_Login):
        print ('test loggin)
        user = Ui_Login.login()






