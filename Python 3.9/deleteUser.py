import csv
#Supression et mise a jour fichier usager
def userdel():
    #1. This code snippet asks the user for a username and deletes the user's record from file.
    updatedlist=[]
    with open("user.csv",newline="") as user:
      reader=csv.reader(user)
      username=input("Entre le nom de l'utilisateur a supprimé:")

      for row in reader: #for every row in the file

                if row[0]!=username: #as long as the username is not in the row .......
                    updatedlist.append(row) #add each row, line by line, into a list called 'udpatedlist'
      print(updatedlist)
      updatefile(updatedlist)

def updatefile(updatedlist):
    with open("user.csv","w",newline="") as user:
        Writer=csv.writer(user)
        Writer.writerows(updatedlist)
        print("Fichier mis a jour")

userdel()

