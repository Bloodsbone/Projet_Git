class Personne:
    # Ceci est la classe personne

    def __init__(self, nom, prenom, sexe):
        self._nom = nom
        self._prenom = prenom
        self._sexe = sexe

    def get_nom(self):
        return self._nom

    def get_prenom(self):
        return self._prenom

    def get_sexe(self):
        return self._sexe

    # def __str__(self):
    # return "Le nom est {}, le prénom est {} et Sexe est {}".format(self._nom, self._prenom, self._sexe)


# p = Personne("dany","gauthier","masculin")
# print(p._nom, p._prenom, p._sexe)

class Client(Personne):
    "Classe Client"

    def __init__(self, nom, prenom, sexe, dateInsc, courriel, password):
        Personne.__init__(self, nom, prenom, sexe)
        self._dateInsc = dateInsc
        self._courriel = courriel
        self._password = password

        def getdateInsc(self):
            return self._dateInsc

        def getcourriel(self):
            return self._courriel

        def getpassword(self):
            return self._password


# def __str__(self):
# return "La date d'inscription est le {}, le courriel est {} et le mot de passe {}".format(self._nom, self._prenom, self._sexe)

#c = Client("22", "asdf@sdf.com", "patate", 54, 65, 56)
#print(c._nom, c._prenom, c._sexe, c._dateInsc, c._courriel, c._password)


class Acteur(Personne):
    "Classe Acteur"

    def __init__(self, nom, prenom, sexe, personnage, demploi, femploi):
        Personne.__init__(self, nom, prenom, sexe)
        self._personnage = personnage
        self._demploi = demploi
        self._femploi = femploi

    def getpersonage(self):
        return self._personnage

    def getdemploi(self):
        return self._demploi

    def getfemploi(self):
        return self._femploi

#fred = Acteur("fred", "tremblay","Male", "l'étalon noit", "hier", "aujourd'hui")
#print(fred._nom, fred._prenom, fred._sexe, fred._personnage,fred._demploi, fred._femploi)

class CarteCredit:
    "classe carte de crédit"

    def __init__(self, carte, expiration, code):
        self.carte = carte
        self.expiration = expiration
        self.code = code

    def getcarte(self):
        return self._carte

    def getexpiration(self):
        return self._expiration

    def getcode(self):
        return self._code

   # def __str__(self):
       # return "Le numero de carte est {}, l'expiration est le  {} et le code secret est {}".format(self._carte,self._expiration, self._code)


class Film:
    "classe de Film"

    def __init__(self, nom, description):
        self._nom = nom
        self._Description = description

    def getnom(self):
        return self._nom

    def getdescription(self):
        return self._description

    def __str__(self):
        return "La classe du film est {} et sa descrition est{}".format(self._nom, self._description)
