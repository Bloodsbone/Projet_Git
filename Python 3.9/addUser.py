import csv
import clss

#Ajout dans un fichier CSV en appelant une classe "r" read "a" append "w" write/ecrase
def addUser():
        with open("user.csv", 'a', newline="") as userinfo:
                x = clss.Personne(input("Nom: "), input("prenom: "), input("Sexe: "))
                fieldnames = ["nom", "prenom", "sexe"]
                writer = csv.writer(userinfo)
                writer.writerow({x._nom, x._prenom, x._sexe})

addUser()