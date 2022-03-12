import time

class Personne:
    "Ceci est la classe personne"

    def __init__(self, nom, prenom, sexe):
        self._nom=nom
        self._prenom = prenom
        self._sexe = ""


    def getNom(self):
        return self._nom

    def getPrenom(self):
        return self._prenom

    def getSexe(self):
        return self._sexe


    def __str__(self):
        return "Le nom est {}, le prénom est {} et Sexe est {}".format(self._nom, self._prenom, self._sexe)


class Client(Personne):
    "Classe Client"

    def __init__(self, dateInsc, courriel, password):
        self.dateInsc=dateInsc
        self.courriel=courriel
        self.password=password

        def getdateInsc(self):
            return self._dateInsc

        def getcourriel(self):
            return self._courriel

        def getpassword(self):
            return self._password

    def __str__(self):
        return "La date d'inscription est le {}, le courriel est {} et le mot de passe {}".format(self._nom, self._prenom, self._sexe)

class Acteur(Personne):
    "Classe Acteur"

    def __init__(self, personnage, demploi, femploi):
        self.personnage=personnage
        self.demploi=demploi
        self.femploi=femploi

    def getpersonage(self):
        return self._personnage

    def getdemploi(self):
        return self._demploi

    def getfemploi(self):
        return self._femploi

    def __str__(self):
        return "Le personnage est {}, le début d'emploi est {} et la fin d'emploie est {}".format(self._personnage, self._demploi, self._femploi)

class CarteCredit:
    "classe carte de crédit"
    def __init__(self, carte, expiration, code):
        self.carte=carte
        self.expiration=expiration
        self.code=code

    def getcarte(self):
        return self._carte


    def getexpiration(self):
        return self._expiration


    def getcode(self):
        return self._code


    def __str__(self):
        return "Le numero de carte est {}, l'expiration est le  {} et le code secret est {}".format(self._carte, self._expiration, self._code)


class Film:
    "classe de Film"
    def __init__(self, nom, description):
        self.nom=nom
        self.Description=description

    def getnom(self):
            return self._nom

    def getdescription(self):
        return self._description

    def __str__(self):
        return "La classe du film est {} et sa descrition est{}".format(self._nom, self._description)
