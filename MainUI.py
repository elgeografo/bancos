import sys
from PySide2.QtWidgets import QLabel, QGroupBox, QVBoxLayout,QApplication, QDialog, QLineEdit, QPushButton
from PySide2.QtCore import QRect

class MainUi(QDialog):

    def __init__(self, parent=None):
        super(MainUi, self).__init__(parent)
        self.setWindowTitle("My Form")
        #self.createInterface()
        self.createLayout()

    def createLayout(self):
        #self.clientListRect = QRect(5, 5, 200, 600)
        self.buttonLoadFile = QPushButton("Load File")
        self.buttonSaveFile = QPushButton("Save File")
        layout = QVBoxLayout()
        layout.addWidget(self.buttonLoadFile)
        layout.addWidget(self.buttonSaveFile)
        self.setLayout(layout)
        self.buttonLoadFile.clicked.connect(self.loadFile)

    def loadFile(self):
        print("Hola Mundo")

    def createInterface(self):
        self.labelName = QLabel("Nombre")
        self.editName= QLineEdit("Write your name here")
        self.labelLastName = QLabel("Apellidos")
        self.editLastName = QLineEdit("Write your last name here")
        self.buttonAdd = QPushButton("Add User")
        layout = QVBoxLayout()
        layout.addWidget(self.labelName)
        layout.addWidget(self.editName)
        layout.addWidget(self.labelLastName)
        layout.addWidget(self.editLastName)
        layout.addWidget(self.buttonAdd)
        self.setLayout(layout)
        # see https://eli.thegreenplace.net/2011/04/25/passing-extra-arguments-to-pyqt-slot/
        self.buttonAdd.clicked.connect(lambda: self.AddAnUser("Luis22"))

    def AddAnUser(self, user):
        self.editName.setText(user)
        print("user")
'''
if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())

'''