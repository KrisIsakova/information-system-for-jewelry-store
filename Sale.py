# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Прода1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1430, 900)
        self.pushButtonGlavnaya2 = QtWidgets.QPushButton(Form)
        self.pushButtonGlavnaya2.setGeometry(QtCore.QRect(70, 30, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonGlavnaya2.setFont(font)
        self.pushButtonGlavnaya2.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButtonGlavnaya2.setObjectName("pushButtonGlavnaya2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(750, 30, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.polosa2 = QtWidgets.QLabel(Form)
        self.polosa2.setGeometry(QtCore.QRect(-20, 80, 1621, 20))
        self.polosa2.setObjectName("polosa2")
        self.pushButtonIzmenSale = QtWidgets.QPushButton(Form)
        self.pushButtonIzmenSale.setGeometry(QtCore.QRect(1140, 120, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButtonIzmenSale.setFont(font)
        self.pushButtonIzmenSale.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButtonIzmenSale.setObjectName("pushButtonIzmenSale")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 120, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButtonSupp2 = QtWidgets.QPushButton(Form)
        self.pushButtonSupp2.setGeometry(QtCore.QRect(420, 30, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonSupp2.setFont(font)
        self.pushButtonSupp2.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButtonSupp2.setObjectName("pushButtonSupp2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(800, 200, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_5.setObjectName("label_5")
        self.pushButton4 = QtWidgets.QPushButton(Form)
        self.pushButton4.setGeometry(QtCore.QRect(1110, 30, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton4.setFont(font)
        self.pushButton4.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButton4.setObjectName("pushButton4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 200, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setObjectName("label_2")
        self.Fon = QtWidgets.QLabel(Form)
        self.Fon.setGeometry(QtCore.QRect(-4, -8, 1431, 911))
        self.Fon.setText("")
        self.Fon.setPixmap(QtGui.QPixmap("fonn.png"))
        self.Fon.setObjectName("Fon")
        self.pushButtonDobSale = QtWidgets.QPushButton(Form)
        self.pushButtonDobSale.setGeometry(QtCore.QRect(940, 120, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButtonDobSale.setFont(font)
        self.pushButtonDobSale.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButtonDobSale.setObjectName("pushButtonDobSale")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(980, 200, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(310, 200, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(570, 200, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_4.setObjectName("label_4")
        self.polosa2_2 = QtWidgets.QLabel(Form)
        self.polosa2_2.setGeometry(QtCore.QRect(-10, 160, 1621, 20))
        self.polosa2_2.setObjectName("polosa2_2")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(50, 260, 1270, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.Fon.raise_()
        self.pushButtonGlavnaya2.raise_()
        self.pushButton.raise_()
        self.pushButtonDobSale.raise_()
        self.polosa2.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButtonIzmenSale.raise_()
        self.pushButtonSupp2.raise_()
        self.polosa2_2.raise_()
        self.pushButton4.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.tableWidget.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButtonGlavnaya2.setText(_translate("Form", "Товары"))
        self.pushButton.setText(_translate("Form", "Продажи"))
        self.polosa2.setText(_translate("Form", "___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________"))
        self.pushButtonIzmenSale.setText(_translate("Form", "Изменить"))
        self.label.setText(_translate("Form", "Продажи"))
        self.pushButtonSupp2.setText(_translate("Form", "Поставщики"))
        self.label_5.setText(_translate("Form", "Артикул"))
        self.pushButton4.setText(_translate("Form", "Отчеты"))
        self.label_2.setText(_translate("Form", "Номер продажи"))
        self.pushButtonDobSale.setText(_translate("Form", "Добавить"))
        self.label_6.setText(_translate("Form", "Количество проданных изделий"))
        self.label_3.setText(_translate("Form", "Сумма продажи"))
        self.label_4.setText(_translate("Form", "Дата и время"))
        self.polosa2_2.setText(_translate("Form", "___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________"))