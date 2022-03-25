import sys
import sqlite3
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5 import QTableWidgetItem


class Ui_Principal(QtWidgets.QWidget):

    switch_modUser = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        #self.readUser()
        self.setObjectName("Principal")
        self.resize(1363, 483)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushRefreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushRefreshButton.setGeometry(QtCore.QRect(220, 390, 75, 23))
        self.pushRefreshButton.setObjectName("pushLogoffButton")
        self.pushRefreshButton.clicked.connect(self.getData)
        self.pushLogoffButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushLogoffButton.setGeometry(QtCore.QRect(520, 390, 75, 23))
        self.pushLogoffButton.setObjectName("pushLogoffButton")
        #self.pushLogoffButton.clicked.connect(self.switch_login.emit)
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
        self.tableWidget.setColumnCount(6)
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
        #self.pushNewButton.clicked.connect(self.switch_newUser.emit)
        self.verticalLayout.addWidget(self.pushNewButton)
        self.pushClientModButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushClientModButton.setObjectName("pushClientModButton")
        self.pushClientModButton.clicked.connect(self.switch_modUser.emit)
        self.verticalLayout.addWidget(self.pushClientModButton)
        self.pushDelButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushDelButton.setObjectName("pushDelButton")
        self.pushDelButton.clicked.connect(self.delData)
        self.verticalLayout.addWidget(self.pushDelButton)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setWindowTitle("RAC")
        self.pushLogoffButton.setText("Deconnexion")
        self.pushRefreshButton.setText("Rafraichir")
        self.label.setText("Client")
        self.label_2.setText("Film")
        self.item = self.tableWidget.horizontalHeaderItem(0)
        self.item.setText("Prénom")
        self.item = self.tableWidget.horizontalHeaderItem(1)
        self.item.setText("Nom")
        self.item = self.tableWidget.horizontalHeaderItem(2)
        self.item.setText("Sexe")
        self.item = self.tableWidget.horizontalHeaderItem(3)
        self.item.setText("Courriel")
        self.item = self.tableWidget.horizontalHeaderItem(4)
        self.item.setText("Mot de Passe")
        self.item = self.tableWidget.horizontalHeaderItem(5)
        self.item.setText("Date d\'inscription")
        self.item = self.tableWidget_2.horizontalHeaderItem(0)
        self.item.setText("Nom")
        self.item = self.tableWidget_2.horizontalHeaderItem(1)
        self.item.setText("Durée")
        self.item = self.tableWidget_2.horizontalHeaderItem(2)
        self.item.setText("Description")
        self.pushNewButton.setText("Nouveau Client")
        self.pushClientModButton.setText("Modifier")
        self.pushDelButton.setText( "Suprimer")
        self.getData()

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
                Nom = data[0]
                Prenom = data[1]
                Sexe = data[2]
                Date_Inscription = data[3]
                Courriel = data[4]
                Mot_de_passe = data[5]
                cur.execute("DELETE FROM Client WHERE Nom=? AND Prenom=? AND Sexe=? AND Date_Inscription=? AND Courriel=? AND Mot_de_passe=?",(Nom,Prenom,Sexe,Date_Inscription,Courriel,Mot_de_passe))
                conn.commit()
        self.getData()



class Ui_ModClient(QtWidgets.QWidget):


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
        self.label.setText("Prénom")
        self.label_2.setText("Nom")
        self.label_3.setText("Sexe")
        self.label_4.setText("Date d\'incription")
        self.label_5.setText("Courriel")
        self.label_6.setText("Mot de Passe")
        self.pushButton.setText("Confirmer")
        self.setWindowTitle("MainWindow")




class Controller:
    def __init__(self):
        pass

    def showLogin(self, *args):
        self.windowLogin = Ui_Principal()
        self.windowLogin.show()
        self.windowLogin.switch_modUser.connect(self.showModUser)

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
