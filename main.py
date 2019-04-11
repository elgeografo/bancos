import sys
from PySide2.QtWidgets import QApplication


from Banco import Banco
from ClienteBanco import ClienteBanco
from MainUI import MainUi

banco = Banco()

cliente = ClienteBanco()
cliente.nombre = "Luis"
cliente.apellido = "Izquierdo"
cliente.saldo = 50

cliente2 = ClienteBanco()
cliente2.nombre = "Pepe"
cliente2.apellido = "Perez"
cliente2.saldo = 60

cliente3 = ClienteBanco()
cliente3.nombre = "Juan"
cliente3.apellido = "Pe"
cliente3.saldo = 70

banco.addClient(cliente)
banco.addClient(cliente2)
banco.addClient(cliente3)

#banco.imprimeClientes()
#banco.saveClientsToFile()

app = QApplication(sys.argv)
formUi = MainUi()

formUi.editName.setText(banco.clients[0].nombre)
formUi.editLastName.setText(banco.clients[0].apellido)
formUi.show()
sys.exit(app.exec_())

