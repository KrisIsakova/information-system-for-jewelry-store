# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Добавить_категорию1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(386, 258)
        self.pushButton1 = QtWidgets.QPushButton(Dialog)
        self.pushButton1.setGeometry(QtCore.QRect(90, 200, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton1.setFont(font)
        self.pushButton1.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton1_2.setGeometry(QtCore.QRect(90, 150, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton1_2.setFont(font)
        self.pushButton1_2.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 11px;\n"
"    border: 2px solid black;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 192, 203, 100); /* Прозрачно розовый */\n"
"}")
        self.pushButton1_2.setObjectName("pushButton1_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 20, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 85, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(90, 80, 281, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.Fon = QtWidgets.QLabel(Dialog)
        self.Fon.setGeometry(QtCore.QRect(-4, -8, 401, 271))
        self.Fon.setText("")
        self.Fon.setPixmap(QtGui.QPixmap("fon.png"))
        self.Fon.setObjectName("Fon")
        self.Fon.raise_()
        self.pushButton1.raise_()
        self.pushButton1_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton1.setText(_translate("Dialog", "Удалить категорию"))
        self.pushButton1_2.setText(_translate("Dialog", "Сохранить изменения"))
        self.label.setText(_translate("Dialog", "Добавить категорию"))
        self.label_2.setText(_translate("Dialog", "Название"))