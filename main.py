from PyQt5 import QtCore, QtGui, QtWidgets
from sign_in_design import Ui_SignIn
from sign_up_design import Ui_SignUp
from finish_win import Ui_FinishWinow
import sys

app = QtWidgets.QApplication(sys.argv)

SignInW = QtWidgets.QMainWindow()
SignUpW = QtWidgets.QMainWindow()
FinishWinW = QtWidgets.QMainWindow()

signin = Ui_SignIn()
signup = Ui_SignUp()
finishwin = Ui_FinishWinow()

signin.setupUi(SignInW)
signup.setupUi(SignUpW)
finishwin.setupUi(FinishWinW)

SignInW.show()
signin.error.hide()

class Info():
    def __init__(self,username,password):
        self.username = username
        self.password = password

def sign_in():
    username = signin.username.text().strip()
    user_password = signin.password.text().strip()

    if username == '':
        signin.error.setText('Input username')
        signin.error.show()
        return

    if len(username) < 5:
        signin.error.setText('Enter minimum 5 chars in username field')  
        signin.error.show()
        return

    if user_password == '':
        signin.error.setText('Input password')
        signin.error.show()
        return
    
    if len(user_password) < 4:
        signin.error.setText('Enter minimum 4 chars in password field')
        signin.error.show()
        return
    
    signin.error.hide()

    with open('login.txt','r',encoding='utf-8') as file:
        checkbox = False
        for line in file:
            
            if line.strip() != '':
                data = line.strip().split(' ')

            if username == data[0]:
                checkbox = True
                
            else:
                pass
        
        if checkbox == False:
                signin.error.setText('Error. This login does not exist')
                signin.error.show()
                
                return
            
    signin.error.hide()               
                
    with open('login.txt','r',encoding='utf-8') as file:
        for line in file:
            if line.strip() != '':
                data = line.strip().split(' ')
                user = Info(data[0],data[1])

                if username == user.username:
                    if user_password == user.password:
                        SignInW.hide()
                        FinishWinW.show()
   
                    else:
                        signin.error.setText('Error. Incorect password!')
                        signin.error.show()
                          

def to_sign_up():
    signup.error_up.hide()
    SignInW.hide()
    SignUpW.show()         
                
def back_to_sign_in():
    SignUpW.hide()
    SignInW.show()

def sign_up():
    username = signup.username_up.text().strip()
    user_password = signup.password_up.text().strip()

    if username == '':
        signup.error_up.setText('Input username')
        signup.error_up.show()
        return

    if len(username) < 5:
        signup.error_up.setText('Input minimum 5 chars in username field')
        signup.error_up.show()
        return

    if user_password == '':
        signup.error_up.setText('Input password')
        signup.error_up.show()
        return
    
    if len(user_password) < 4:
        signup.error_up.setText('Input minimum 4 chars in password field')
        signup.error_up.show()
        return
    
    signup.error_up.hide()

    with open('login.txt','r',encoding='utf-8') as file:
        for line in file:
            if line.strip() != '':
                data = line.strip().split(' ')

                if username == data[0]:
                    signup.error_up.setText('This username is already use. Enter other username')
                    signup.error_up.show()
                    return

                if user_password == data[1]:
                    signup.error_up.setText('This password is already use. Enter other password')
                    signup.error_up.show()
                    return

    signup.error_up.hide()
    with open('login.txt','a',encoding='utf-8') as file:
        data = ['','']
        data[0] = username
        data[1] = user_password
        file.write(f'{data[0]} ')
        file.write(f'{data[1]}\n')
    
    SignUpW.hide()
    FinishWinW.show()



signin.pushButton.clicked.connect(to_sign_up)
signin.login_bt.clicked.connect(sign_in)
signup.pushButton_2.clicked.connect(back_to_sign_in)
signup.login_bt.clicked.connect(sign_up)
sys.exit(app.exec_())