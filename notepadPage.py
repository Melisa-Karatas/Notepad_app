from PyQt5.QtWidgets import *
from notepad import Ui_MainWindow
import os
from PyQt5.QtGui import QKeySequence

class notepadPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.notepadForm = Ui_MainWindow()
        self.notepadForm.setupUi(self)
        self.notepadForm.actionOpen.triggered.connect(self.openFileFunction)
        self.notepadForm.actionSave.triggered.connect(self.saveFileFunction)
        self.notepadForm.actionClear.triggered.connect(self.clearTextFunction)
        self.notepadForm.actionExit.triggered.connect(self.closeFileFunction)
        self.notepadForm.actionAbout_me.triggered.connect(self.aboutmeFunciton)
        
        self.shortcut_open = QShortcut(QKeySequence('Ctrl+O'), self)
        self.shortcut_open.activated.connect(self.openFileFunction)
        
        self.shortcut_save = QShortcut(QKeySequence('Ctrl+S'), self)
        self.shortcut_save.activated.connect(self.saveFileFunction)
        
        self.shortcut_clear = QShortcut(QKeySequence('Ctrl+D'), self)
        self.shortcut_clear.activated.connect(self.clearTextFunction)
        
        self.shortcut_exit = QShortcut(QKeySequence('Ctrl+Q'), self)
        self.shortcut_exit.activated.connect(self.closeFileFunction)
        
    def openFileFunction(self):
        file_name = QFileDialog.getOpenFileName(self, "Open File", os.getenv("Home"))
        if len(file_name[0]) != 0:       
            with open(file_name[0], "r") as file:
                self.notepadForm.textEdit_notepad.setText(file.read())
        else:
            QMessageBox.warning(self, "Information", "Please select a file.")
            
    def saveFileFunction(self):
        file_name = QFileDialog.getSaveFileName(self, "Save File", os.getenv("Home"))
        if len(file_name[0]) != 0:
            with open(file_name[0], "w") as file:
                file.write(self.notepadForm.textEdit_notepad.toPlainText())
        else:
            QMessageBox.warning(self, "Information", "Please save the file.")
            
    def clearTextFunction(self):
        answer = QMessageBox.information(self, "Information", "Do you want to clear the page?", QMessageBox.Yes, QMessageBox.No)
        if answer == QMessageBox.Yes:
            self.notepadForm.textEdit_notepad.clear()
            
    def closeFileFunction(self):
        answer = QMessageBox.information(self, "Information", "Do you want to exit the file?", QMessageBox.Yes, QMessageBox.No)
        if answer == QMessageBox.Yes:
            self.close()
        
    def aboutmeFunciton(self):
        QMessageBox().about(self, "About me", "This program is written by me. <br />You can use this freely.")
        
        
        