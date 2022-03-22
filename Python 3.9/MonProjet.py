from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import sys
from PyQt5.QtWidgets import QMessageBox




class Ui_MainWindow(object):

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Principal()
        self.ui.setupUi(self.window, MainWindow)
        self.window.show()
        MainWindow.hide()

    def login(self):
        uname = self.usagerEdit.text()
        passw = self.mdpEdit.text()
        connection = sqlite3.connect("db.db")
        result = connection.execute("SELECT * FROM Login WHERE UserCode = ? AND Password = ?", (uname, passw))
        if result.fetchall():
            print("connexion réussi login")
            self.openWindow()


        else:
            print("invalid login")


    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 256)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(240, 150, 75, 23))
        self.loginButton.setObjectName("loginButton")
        self.loginButton.clicked.connect(self.login)
        self.usager_label = QtWidgets.QLabel(self.centralwidget)
        self.usager_label.setGeometry(QtCore.QRect(150, 60, 47, 13))
        self.usager_label.setObjectName("usager_label")
        self.mdp_label = QtWidgets.QLabel(self.centralwidget)
        self.mdp_label.setGeometry(QtCore.QRect(120, 90, 71, 16))
        self.mdp_label.setObjectName("mdp_label")
        self.Login_Label = QtWidgets.QLabel(self.centralwidget)
        self.Login_Label.setGeometry(QtCore.QRect(170, 10, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Login_Label.setFont(font)
        self.Login_Label.setObjectName("Login_Label")
        self.usagerEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.usagerEdit.setGeometry(QtCore.QRect(210, 60, 113, 20))
        self.usagerEdit.setObjectName("usagerEdit")
        self.mdpEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.mdpEdit.setGeometry(QtCore.QRect(210, 90, 113, 20))
        self.mdpEdit.setObjectName("mdpEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loginButton.setText(_translate("MainWindow", "Connexion"))
        self.usager_label.setText(_translate("MainWindow", "Usager:"))
        self.mdp_label.setText(_translate("MainWindow", "Mot de passe:"))
        self.Login_Label.setText(_translate("MainWindow", "Fenêtre de Connexion"))


class Ui_Principal(object):
    def setupUi(self, Principal, MainWindow):
        Principal.setObjectName("Principal")
        Principal.resize(1012, 351)
        self.centralwidget = QtWidgets.QWidget(Principal)
        self.centralwidget.setObjectName("centralwidget")
        self.tableClientView = QtWidgets.QTableView(self.centralwidget)
        self.tableClientView.setGeometry(QtCore.QRect(170, 40, 371, 201))
        self.tableClientView.setObjectName("tableClientView")
        self.tableFilmView = QtWidgets.QTableView(self.centralwidget)
        self.tableFilmView.setGeometry(QtCore.QRect(570, 40, 371, 201))
        self.tableFilmView.setObjectName("tableFilmView")
        self.pushLogoffButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: logoff())
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
        Principal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1012, 21))
        self.menubar.setObjectName("menubar")
        Principal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Principal)
        self.statusbar.setObjectName("statusbar")
        Principal.setStatusBar(self.statusbar)

        self.retranslateUi(Principal)
        QtCore.QMetaObject.connectSlotsByName(Principal)

    def logoff(self):
        self.closeMain(Principal)
        self.showMain(MainWindow)

    def retranslateUi(self, Principal):
        _translate = QtCore.QCoreApplication.translate
        Principal.setWindowTitle(_translate("Principal", "MainWindow"))
        self.pushLogoffButton.setText(_translate("Principal", "Deconnexion"))
        self.pushClientModButton.setText(_translate("Principal", "Modifier"))
        self.pushNewButton.setText(_translate("Principal", "Nouveau Client"))
        self.pushDelButton.setText(_translate("Principal", "Suprimer"))
        self.labelClient.setText(_translate("Principal", "Client"))
        self.label_Film.setText(_translate("Principal", "Film"))










if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
