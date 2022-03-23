import sys
from PyQt5 import QtCore, QtGui, QtWidgets
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
            print("invalid login")

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

    switch_window = QtCore.pyqtSignal()

    def logout(self):
        self.switch_window.emit()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("Principal")
        self.resize(1012, 351)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.tableClientView = QtWidgets.QTableView(self.centralwidget)
        self.tableClientView.setGeometry(QtCore.QRect(170, 40, 371, 201))
        self.tableClientView.setObjectName("tableClientView")
        self.tableFilmView = QtWidgets.QTableView(self.centralwidget)
        self.tableFilmView.setGeometry(QtCore.QRect(570, 40, 371, 201))
        self.tableFilmView.setObjectName("tableFilmView")
        self.pushLogoffButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushLogoffButton.clicked.connect(self.logout)
        self.pushLogoffButton.clicked.connect(self.close)
        self.pushLogoffButton.setGeometry(QtCore.QRect(520, 270, 75, 23))
        self.pushLogoffButton.setObjectName("pushLogoffButton")
        self.pushClientModButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushClientModButton.setGeometry(QtCore.QRect(40, 180, 91, 23))
        self.pushClientModButton.setObjectName("pushClientModButton")
        self.pushNewButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushNewButton.setGeometry(QtCore.QRect(40, 40, 91, 23))
        self.pushNewButton.setObjectName("pushNewButton")
        self.pushDelButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushDelButton.setGeometry(QtCore.QRect(40, 220, 91, 21))
        self.pushDelButton.setObjectName("pushDelButton")
        self.labelClient = QtWidgets.QLabel(self.centralwidget)
        self.labelClient.setGeometry(QtCore.QRect(310, 10, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelClient.setFont(font)
        self.labelClient.setObjectName("labelClient")
        self.label_Film = QtWidgets.QLabel(self.centralwidget)
        self.label_Film.setGeometry(QtCore.QRect(730, 10, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Film.setFont(font)
        self.label_Film.setObjectName("label_Film")

        self.setWindowTitle("MainWindow")
        self.pushLogoffButton.setText("Deconnexion")
        self.pushClientModButton.setText("Modifier")
        self.pushNewButton.setText("Nouveau Client")
        self.pushDelButton.setText("Suprimer")
        self.labelClient.setText("Client")
        self.label_Film.setText("Film")




class Controller:
    def __init__(self):
        pass

    def showLogin(self, *args):
        self.windowLogin = Ui_Login()
        self.windowLogin.switch_window.connect(self.showPrincipal)
        self.windowLogin.show()

    def showPrincipal(self, *args):
        self.windowPrincipal = Ui_Principal()
        self.windowPrincipal.switch_window.connect(self.showLogin)
        self.windowLogin.close()
        self.windowPrincipal.show()

    #def logOff(self, *args):
        #self.windowLogin = Ui_Login()
        #self.windowPrincipal.close()
        #self.windowLogin.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.showLogin()
    sys.exit((app.exec_()))

if __name__ == "__main__":
    main()
