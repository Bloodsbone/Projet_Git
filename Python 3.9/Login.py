import getpass

granted = False


def grant():
    global granted
    granted = True


def log(nom, mdp):
    success = False
    file = open("usager.txt", "r")
    for i in file:
        a, b = i.split(",")
        b = b.strip()
        if (a == nom and b == mdp):
            success = True
            break
    file.close()
    if (success):
        print("Connexion réussie")
        grant()
    else:
        print("Information incorect")


def register(nom, mdp):
    file = open("usager.txt", "a")
    file.write("\n" + nom + "," + mdp)
    grant()


def access(option):
    global name
    if (option == "log"):
        name = input("Nom: ")
        password = getpass.getpass(prompt="Password: ")
        login(name, password)
    else:
        print("Nouvel Utilisateur")
        name = input("Nom: ")
        password = getpass.getpass(prompt="Password: ")
        register(name, password)


def begin():
    global option
    print("welcome to Victor's programming club")
    option = input("Login or Register (Log,Reg): ")
    if (option != "log" and option != "reg"):
        begin()


begin()
access(option)

if (granted):
    print("Bienvenue au club")
    print("### USER DETAILS ###")
    print("Username: ", name)
