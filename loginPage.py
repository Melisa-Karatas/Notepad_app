from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import *
from login import Ui_Form
from notepadPage import notepadPage
from PyQt5 import QtCore

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.loginform = Ui_Form()
        self.loginform.setupUi(self)
        self.notepadForm = notepadPage()
        self.loginform.pushButton_login.clicked.connect(self.keyPressEvent)
        
    def keyPressEvent(self, qKeyEvent):
        if qKeyEvent.key() == QtCore.Qt.Key_Return or qKeyEvent.key() == QtCore.Qt.Key_Enter :
            username = self.loginform.lineEdit_username.text()
            password = self.loginform.lineEdit_password.text()
            if username == "melisa" and password == "123456":
                self.close()
                self.notepadForm.show()
        elif qKeyEvent.key() == QtCore.Qt.Key_Escape:
            self.close()
            