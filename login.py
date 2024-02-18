# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(413, 111)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_username = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_username)
        self.label_password = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_password)
        self.lineEdit_username = QtWidgets.QLineEdit(Form)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_username)
        self.lineEdit_password = QtWidgets.QLineEdit(Form)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_password)
        self.pushButton_login = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setStyleSheet("background-color: rgb(222, 166, 255);")
        self.pushButton_login.setObjectName("pushButton_login")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton_login)
        self.verticalLayout.addLayout(self.formLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.label_username.setText(_translate("Form", "Username:"))
        self.label_password.setText(_translate("Form", "Password:"))
        self.pushButton_login.setText(_translate("Form", "LOGIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())