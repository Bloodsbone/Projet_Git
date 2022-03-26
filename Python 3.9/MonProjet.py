import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3


class Ui_Login(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def login(self):
        uname = self.usagerEdit.text()
        passw = self.mdpEdit.text()
        connection = sqlite3.connect("db.db")
        result = connection.execute("SELECT * FROM Login WHERE UserCode = ? AND Password = ?", (uname, passw))
        if result.fetchall():
            print("connexion réussi")
            self.switch_window.emit()

        else:
            QtWidgets.QMessageBox.question(self, 'Erreur', 'Utilisateur ou mot de passe incorect!',
                                           QMessageBox.Close)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("Login")
        self.resize(531, 256)
        self.loginButton = QtWidgets.QPushButton(self)
        self.loginButton.setGeometry(QtCore.QRect(240, 150, 75, 23))
        self.loginButton.setObjectName("loginButton")
        self.loginButton.clicked.connect(self.login)
        self.usager_label = QtWidgets.QLabel(self)
        self.usager_label.setGeometry(QtCore.QRect(150, 60, 47, 13))
        self.usager_label.setObjectName("usager_label")
        self.mdp_label = QtWidgets.QLabel(self)
        self.mdp_label.setGeometry(QtCore.QRect(120, 90, 71, 16))
        self.mdp_label.setObjectName("mdp_label")
        self.Login_Label = QtWidgets.QLabel(self)
        self.Login_Label.setGeometry(QtCore.QRect(170, 10, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Login_Label.setFont(font)
        self.Login_Label.setObjectName("Login_Label")
        self.usagerEdit = QtWidgets.QLineEdit(self)
        self.usagerEdit.setGeometry(QtCore.QRect(210, 60, 113, 20))
        self.usagerEdit.setObjectName("usagerEdit")
        self.mdpEdit = QtWidgets.QLineEdit(self)
        self.mdpEdit.setGeometry(QtCore.QRect(210, 90, 113, 20))
        self.mdpEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mdpEdit.setObjectName("mdpEdit")
        self.setWindowTitle("Login")
        self.loginButton.setText("Connexion")
        self.usager_label.setText("Usager:")
        self.mdp_label.setText("Mot de passe:")
        self.Login_Label.setText("Fenêtre de Connexion")


class Ui_Principal(QtWidgets.QWidget):

    switch_login = QtCore.pyqtSignal()
    switch_newUser = QtCore.pyqtSignal()
    switch_modUser = QtCore.pyqtSignal()


    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("Principal")
        self.resize(1363, 483)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushLogoffButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushLogoffButton.setGeometry(QtCore.QRect(520, 390, 75, 23))
        self.pushLogoffButton.setObjectName("pushLogoffButton")
        self.pushLogoffButton.clicked.connect(self.switch_login.emit)
        self.pushLogoffButton.clicked.connect(self.close)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(221, 11, 46, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(910, 10, 34, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(220, 40, 601, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(880, 40, 341, 321))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 30, 83, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushNewButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushNewButton.setObjectName("pushNewButton")
        self.pushNewButton.clicked.connect(self.switch_newUser.emit)
        self.verticalLayout.addWidget(self.pushNewButton)
        self.pushClientModButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushClientModButton.setObjectName("pushClientModButton")
        self.pushClientModButton.clicked.connect(self.switch_modUser.emit)
        self.verticalLayout.addWidget(self.pushClientModButton)
        self.pushDelButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushDelButton.setObjectName("pushDelButton")
        self.pushDelButton.clicked.connect(self.messageSuppression)
        self.verticalLayout.addWidget(self.pushDelButton)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setWindowTitle("RAC")
        self.pushLogoffButton.setText("Deconnexion")
        self.label.setText("Client")
        self.label_2.setText("Film")
        self.item = self.tableWidget.horizontalHeaderItem(0)
        self.item.setText("ID")
        self.item = self.tableWidget.horizontalHeaderItem(1)
        self.item.setText("Nom")
        self.item = self.tableWidget.horizontalHeaderItem(2)
        self.item.setText("New Column")
        self.item = self.tableWidget.horizontalHeaderItem(3)
        self.item.setText("Prenom")
        self.item = self.tableWidget.horizontalHeaderItem(4)
        self.item.setText("Date_Inscription")
        self.item = self.tableWidget.horizontalHeaderItem(5)
        self.item.setText("Courriel")
        self.item = self.tableWidget.horizontalHeaderItem(6)
        self.item.setText("Mot de Passe")
        self.item = self.tableWidget_2.horizontalHeaderItem(0)
        self.item.setText("Nom")
        self.item = self.tableWidget_2.horizontalHeaderItem(1)
        self.item.setText("Durée")
        self.item = self.tableWidget_2.horizontalHeaderItem(2)
        self.item.setText("Description")
        self.pushNewButton.setText("Nouveau Client")
        self.pushClientModButton.setText("Modifier")
        self.pushDelButton.setText("Suprimer")
        self.pushRefreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushRefreshButton.setGeometry(QtCore.QRect(220, 390, 75, 23))
        self.pushRefreshButton.setObjectName("pushLogoffButton")
        self.pushRefreshButton.clicked.connect(self.getData)
        self.pushRefreshButton.setText("Rafraichir")
        self.getData()
        self.getDataFilm()

    def getData(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.setRowCount(0)
        conn = sqlite3.connect('db.db')
        cur = conn.cursor()
        content = 'SELECT * FROM Client'
        res = cur.execute(content)
        self.tableWidget.setRowCount(0)
        for row_index, row_data in enumerate(res):
            self.tableWidget.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, colm_index, QtWidgets.QTableWidgetItem(str(colm_data)))
        conn.close()

    def delData(self):
        conn = sqlite3.connect('db.db')
        cur = conn.cursor()
        client = 'SELECT * FROM Client'
        res = cur.execute(client)
        for row in enumerate(res):
            if row[0]  == self.tableWidget.currentRow():
                data = row[1]
                Nom = data[1]
                Prenom = data[2]
                Sexe = data[3]
                Date_Inscription = data[4]
                Courriel = data[5]
                Mot_de_passe = data[6]
                cur.execute("DELETE FROM Client WHERE Nom=? AND Prenom=? AND Sexe=? AND Date_Inscription=? AND Courriel=? AND Mot_de_passe=?",(Nom,Prenom,Sexe,Date_Inscription,Courriel,Mot_de_passe))
                conn.commit()
        self.getData()

    def getDataFilm(self):
        while self.tableWidget_2.rowCount() > 0:
            self.tableWidget_2.setRowCount(0)
        conn = sqlite3.connect('db.db')
        cur = conn.cursor()
        content = 'SELECT * FROM Film'
        res = cur.execute(content)
        self.tableWidget_2.setRowCount(0)
        for row_index, row_data in enumerate(res):
            self.tableWidget_2.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget_2.setItem(row_index, colm_index, QtWidgets.QTableWidgetItem(str(colm_data)))
        conn.close()

    def messageSuppression(self):
        res = QtWidgets.QMessageBox.question(self, 'sure?', 'êtes-vous sur de vouloir supprimer?', QMessageBox.Yes | QMessageBox.No)
        if res == QtWidgets.QMessageBox.Yes:
            print("yes")
            self.delData()

class Ui_NewClient(QtWidgets.QWidget):


    def newCustFonction(self):
        prenom = self.lineEditPrenom.text()
        nom = self.lineEditNom.text()
        sexe = self.lineEditSexe.text()
        dateInsc = self.lineEditDateInscription.text()
        courriel = self.lineEditCourriel.text()
        password = self.lineEditMdp.text()
        user_info = [prenom, nom, sexe, dateInsc, courriel, password]
        conn = sqlite3.connect("db.db")
        c = conn.cursor()
        c.execute('SELECT * FROM Client WHERE Courriel = ?', [courriel])
        result = c.fetchone()

        if result:
            QtWidgets.QMessageBox.question(self, 'Erreur', 'Courriel déja existant!',
                                                 QMessageBox.Close)

        elif len(password) < 8:
            QtWidgets.QMessageBox.question(self, 'Erreur', 'Mot de passe trop court!',
                                                 QMessageBox.Close)

        else:
            conn = sqlite3.connect("db.db")
            c = conn.cursor()
            c.execute(
                'INSERT INTO Client (Nom, Prenom, Sexe, Date_Inscription, Courriel, Mot_de_passe) VALUES (?,?,?,?,?,?)',
                user_info)
            conn.commit()
            self.close()



    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("MainWindow")
        self.resize(541, 362)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(210, 40, 135, 152))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEditPrenom = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditPrenom.setObjectName("lineEditPrenom")
        self.verticalLayout.addWidget(self.lineEditPrenom)
        self.lineEditNom = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditNom.setObjectName("lineEditNom")
        self.verticalLayout.addWidget(self.lineEditNom)
        self.lineEditSexe = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditSexe.setObjectName("lineEditSexe")
        self.verticalLayout.addWidget(self.lineEditSexe)
        self.lineEditDateInscription = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditDateInscription.setObjectName("lineEditDateInscription")
        self.verticalLayout.addWidget(self.lineEditDateInscription)
        self.lineEditCourriel = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditCourriel.setObjectName("lineEditCourriel")
        self.verticalLayout.addWidget(self.lineEditCourriel)
        self.lineEditMdp = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditMdp.setObjectName("lineEditMdp")
        self.verticalLayout.addWidget(self.lineEditMdp)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 40, 117, 151))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 210, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.newCustFonction)
        self.label.setText("Prénom")
        self.label_2.setText("Nom")
        self.label_3.setText("Sexe")
        self.label_4.setText("Date d\'incription")
        self.label_5.setText("Courriel")
        self.label_6.setText("Mot de Passe")
        self.pushButton.setText("Créer")
        self.setWindowTitle("MainWindow")


class Ui_ModClient(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("MainWindow")
        self.resize(948, 362)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(220, 260, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.updateData)
        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 40, 135, 178))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineIdEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineIdEdit.setObjectName("lineIdEdit")
        self.verticalLayout.addWidget(self.lineIdEdit)
        self.lineEditPrenom = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditPrenom.setObjectName("lineEditPrenom")
        self.verticalLayout.addWidget(self.lineEditPrenom)
        self.lineEditNom = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditNom.setObjectName("lineEditNom")
        self.verticalLayout.addWidget(self.lineEditNom)
        self.lineEditSexe = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditSexe.setObjectName("lineEditSexe")
        self.verticalLayout.addWidget(self.lineEditSexe)
        self.lineEditDateInscription = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditDateInscription.setObjectName("lineEditDateInscription")
        self.verticalLayout.addWidget(self.lineEditDateInscription)
        self.lineEditCourriel = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditCourriel.setObjectName("lineEditCourriel")
        self.verticalLayout.addWidget(self.lineEditCourriel)
        self.lineEditMdp = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditMdp.setObjectName("lineEditMdp")
        self.verticalLayout.addWidget(self.lineEditMdp)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(100, 40, 124, 181))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(420, 40, 501, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.setWindowTitle("MainWindow")
        self.pushButton.setText("Confirmer")
        self.label_7.setText("Id Obligatoire*")
        self.label.setText("Prénom")
        self.label_2.setText("Nom")
        self.label_3.setText("Sexe")
        self.label_4.setText("Date d\'inscription")
        self.label_5.setText("Courriel")
        self.label_6.setText("Mot de Passe")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("ID")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("Nom")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText("New Column")
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText("Prenom")
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText("Date_Inscription")
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText("Courriel")
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText("Mot de Passe")
        self.fillTable()

    def fillTable(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.setRowCount(0)
        conn = sqlite3.connect('db.db')
        cur = conn.cursor()
        content = 'SELECT * FROM Client'
        res = cur.execute(content)
        self.tableWidget.setRowCount(0)
        for row_index, row_data in enumerate(res):
            self.tableWidget.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, colm_index, QtWidgets.QTableWidgetItem(str(colm_data)))
        conn.close()

    def updateData(self):
        id = self.lineIdEdit.text()
        prenom = self.lineEditPrenom.text()
        nom = self.lineEditNom.text()
        sexe = self.lineEditSexe.text()
        dateInsc = self.lineEditDateInscription.text()
        courriel = self.lineEditCourriel.text()
        password = self.lineEditMdp.text()
        user_info = [prenom, nom, sexe, dateInsc, courriel, password]
        conn = sqlite3.connect("db.db")
        c = conn.cursor()
        c.execute('SELECT * FROM Client WHERE Courriel = ?', [courriel])
        result = c.fetchone()

        if result:
            QtWidgets.QMessageBox.question(self, 'Erreur', 'Courriel déja existant!',
                                                 QMessageBox.Close)

        elif len(password) < 8:
            QtWidgets.QMessageBox.question(self, 'Erreur', 'Mot de passe trop court!',
                                                 QMessageBox.Close)

        else:
            conn = sqlite3.connect("db.db")
            c = conn.cursor()
            c.execute(
                'UPDATE Client set Nom = ?, Prenom = ?, Sexe = ?, Date_Inscription = ?, Courriel = ?, Mot_de_passe = ? WHERE ID = ?',
                (nom, prenom, sexe, dateInsc, courriel, password, id))
            conn.commit()
            self.close()






class Controller:
    def __init__(self):
        pass

    def showLogin(self, *args):
        self.windowLogin = Ui_Login()
        self.windowLogin.switch_window.connect(self.showPrincipal)
        self.windowLogin.show()

    def showPrincipal(self, *args):
        self.windowPrincipal = Ui_Principal()
        self.windowPrincipal.switch_login.connect(self.showLogin)
        self.windowPrincipal.switch_newUser.connect(self.showNewUser)
        self.windowPrincipal.switch_modUser.connect(self.showModUser)
        self.windowLogin.close()
        self.windowPrincipal.show()

    def showNewUser(self, *args):
        self.windowNewClient = Ui_NewClient()
        self.windowNewClient.show()

    def showModUser(self, *args):
        self.windowModClient = Ui_ModClient()
        self.windowModClient.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.showLogin()
    sys.exit((app.exec_()))

if __name__ == "__main__":
    main()
