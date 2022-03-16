import csv
import clss


#Ajout dans un fichier CSV en appelant une classe "r" read "a" append "w" write/ecrase
with open("user.csv", 'w', newline="") as dataStor:
    x = clss.Personne(input("Nom: "), input("prenom: "), input("Sexe: "))
    fieldnames = ["nom", "prenom", "sexe"]
    writer = csv.writer(dataStor)
    writer.writerow({x._nom, x._prenom, x._sexe})