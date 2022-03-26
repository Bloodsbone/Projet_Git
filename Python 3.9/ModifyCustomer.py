import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_modCustomer(QtWidgets.QWidget):


    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("MainWindow")
        self.resize(847, 362)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 210, 111, 41))
        self.pushButton.setObjectName("pushButton")
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
        #table widget
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(470, 40, 256, 192))
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

        self.setWindowTitle("MainWindow")
        self.pushButton.setText("Confirmer")
        self.label.setText("Prénom")
        self.label_2.setText("Nom")
        self.label_3.setText("Sexe")
        self.label_4.setText("Date d\'incription")
        self.label_5.setText("Courriel")
        self.label_6.setText("Mot de Passe")
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






class Controller:
    def __init__(self):
        pass

    def showLogin(self, *args):
        self.windowLogin = Ui_modCustomer()
        self.windowLogin.show()
        #self.windowLogin.switch_modUser.connect(self.showModUser)





def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.showLogin()
    sys.exit((app.exec_()))

if __name__ == "__main__":
    main()
