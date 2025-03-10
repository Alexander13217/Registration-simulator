# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign_up_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignUp(object):
    def setupUi(self, SignUp):
        SignUp.setObjectName("SignUp")
        SignUp.resize(583, 514)
        self.groupBox = QtWidgets.QGroupBox(SignUp)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 561, 371))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(28)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.username_up = QtWidgets.QLineEdit(self.groupBox)
        self.username_up.setGeometry(QtCore.QRect(120, 70, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.username_up.setFont(font)
        self.username_up.setStyleSheet("QWidget {\n"
"    border-radius: 14px;\n"
"}")
        self.username_up.setObjectName("username_up")
        self.password_up = QtWidgets.QLineEdit(self.groupBox)
        self.password_up.setGeometry(QtCore.QRect(120, 140, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.password_up.setFont(font)
        self.password_up.setStyleSheet("QWidget {\n"
"    border-radius: 14px;\n"
"}")
        self.password_up.setObjectName("password_up")
        self.login_bt = QtWidgets.QPushButton(self.groupBox)
        self.login_bt.setGeometry(QtCore.QRect(130, 230, 241, 71))
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
        self.pushButton_2 = QtWidgets.QPushButton(SignUp)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 460, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.error_up = QtWidgets.QLabel(SignUp)
        self.error_up.setGeometry(QtCore.QRect(10, 390, 381, 41))
        self.error_up.setObjectName("error_up")

        self.retranslateUi(SignUp)
        QtCore.QMetaObject.connectSlotsByName(SignUp)

    def retranslateUi(self, SignUp):
        _translate = QtCore.QCoreApplication.translate
        SignUp.setWindowTitle(_translate("SignUp", "Dialog"))
        self.groupBox.setTitle(_translate("SignUp", "Sign up"))
        self.username_up.setPlaceholderText(_translate("SignUp", "Input your username"))
        self.password_up.setPlaceholderText(_translate("SignUp", "Input your password"))
        self.login_bt.setText(_translate("SignUp", "Sign up"))
        self.pushButton_2.setText(_translate("SignUp", "Sign in"))
        self.error_up.setText(_translate("SignUp", "Error"))
