import sys
import copy
from PySide2.QtWidgets import QLabel, QGroupBox, QVBoxLayout, QHBoxLayout, \
    QApplication, QDialog, QLineEdit, QPushButton
from PySide2.QtCore import QRect,QObject,SIGNAL

class MiBoton(QPushButton):
    def __init__(self, nombre):
        super(MiBoton, self).__init__(nombre)
        self.clicked.connect(lambda: self.AddAnUser(nombre))

        # QObject.connect(btn, SIGNAL("clicked()"), lambda: self.AddAnUser(btn))

        # self.clientList.addWidget(self)

    def AddAnUser(self, nombre):
        print(nombre)



class MainUi(QDialog):

    #Constructor
    def __init__(self, banco):
        super(MainUi, self).__init__()
        self._banco = banco
        self.setWindowTitle("My Form")
        #self.createInterface()
        self.createGeneralLayout()
        self.createClientListLayout()
        self.createClientDataLayout()


    def createGeneralLayout(self):
        self.clientList = QVBoxLayout()
        self.clientData = QVBoxLayout()
        generallayout = QHBoxLayout()
        generallayout.addLayout(self.clientList)
        generallayout.addLayout(self.clientData)
        self.setLayout(generallayout)

    def createClientListLayout(self):
        buttonLoadFile = QPushButton("Load File")
        buttonSaveFile = QPushButton("Save File")
        self.clientList.addWidget(buttonLoadFile)
        self.clientList.addWidget(buttonSaveFile)
        buttonLoadFile.clicked.connect(self.displayClients)

    def createClientDataLayout(self):
        labelNombre = QLabel("Nombre")
        self.clientData.addWidget(labelNombre)

    def displayClients(self):
        counter = -1

        for client in self._banco.clients:
            btn = QPushButton(client.nombre)
            #_foo.append(btn)
            counter += 1
            btn.clicked.connect(lambda: self.AddAnUser(btn))
            self.clientList.addWidget(btn)

            #btn = MiBoton(client.nombre)

            #self.clientList.addWidget(btn)



    def displayClients2(self):
        btns = []
        counter = 0
        for client in self._banco.clients:
            btn = QPushButton(client.nombre)
            self.clientList.addWidget(btn)
            #btn.clicked.connect(lambda: self.AddAnUser(client.nombre))
            btnc = copy.copy(btn)
            btns.append(btnc)
            btns[counter].clicked.connect(lambda: self.AddAnUser(client.nombre))
            counter += 1

    def createLayout(self):
        #self.clientListRect = QRect(5, 5, 200, 600)
        self.buttonLoadFile = QPushButton("Load File")
        self.buttonSaveFile = QPushButton("Save File")
        #self.buttonLoadFile.setAttribute("x", 50)
        generallayout = QHBoxLayout()
        layout = QVBoxLayout()
        layout.addWidget(self.buttonLoadFile)
        layout.addWidget(self.buttonSaveFile)
        generallayout.addLayout(layout)
        layout2 = QVBoxLayout()
        layout3 = QHBoxLayout()
        #layout4 = QHBoxLayout()
        layout2.addLayout(layout3)
        #layout2.addLayout(layout4)
        self.buttonLoadFile2 = QPushButton("Load File2")
        self.buttonLoadFile3 = QPushButton("Load File3")
        layout3.addWidget(self.buttonLoadFile2)
        layout3.addWidget(self.buttonLoadFile3)

        generallayout.addLayout(layout2)
        self.setLayout(generallayout)

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

    def AddAnUser(self, btn):
        #self.editName.setText(user)
        print(btn.text())
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