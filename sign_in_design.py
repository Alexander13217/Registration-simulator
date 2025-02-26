# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign_in_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignIn(object):
    def setupUi(self, SignIn):
        SignIn.setObjectName("SignIn")
        SignIn.resize(579, 516)
        self.groupBox = QtWidgets.QGroupBox(SignIn)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 551, 371))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(28)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.login_bt = QtWidgets.QPushButton(self.groupBox)
        self.login_bt.setGeometry(QtCore.QRect(140, 240, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(24)
        self.login_bt.setFont(font)
        self.login_bt.setStyleSheet("QPushButton {\n"
"    background-color: lightblue;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: lightpink;\n"
"}")
        self.login_bt.setObjectName("login_bt")
        self.username = QtWidgets.QLineEdit(self.groupBox)
        self.username.setGeometry(QtCore.QRect(130, 90, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.username.setFont(font)
        self.username.setStyleSheet("QWidget {\n"
"    border-radius: 14px;\n"
"}")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.groupBox)
        self.password.setGeometry(QtCore.QRect(130, 160, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.password.setFont(font)
        self.password.setStyleSheet("QWidget {\n"
"    border-radius: 14px;\n"
"}")
        self.password.setObjectName("password")
        self.pushButton = QtWidgets.QPushButton(SignIn)
        self.pushButton.setGeometry(QtCore.QRect(460, 470, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.error = QtWidgets.QLabel(SignIn)
        self.error.setGeometry(QtCore.QRect(10, 380, 381, 41))
        self.error.setObjectName("error")

        self.retranslateUi(SignIn)
        QtCore.QMetaObject.connectSlotsByName(SignIn)

    def retranslateUi(self, SignIn):
        _translate = QtCore.QCoreApplication.translate
        SignIn.setWindowTitle(_translate("SignIn", "Dialog"))
        self.groupBox.setTitle(_translate("SignIn", "Sign in"))
        self.login_bt.setText(_translate("SignIn", "Login"))
        self.username.setPlaceholderText(_translate("SignIn", "Input your username"))
        self.password.setPlaceholderText(_translate("SignIn", "Input your password"))
        self.pushButton.setText(_translate("SignIn", "Sign up"))
        self.error.setText(_translate("SignIn", "Error"))
