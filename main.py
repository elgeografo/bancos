import sys
from PySide2.QtWidgets import QApplication


from Banco import Banco
from ClienteBanco import ClienteBanco
from MainUI import MainUi

banco = Banco()
banco.creaClientesDeMentira()

#banco.imprimeClientes()
#banco.saveClientsToFile()

app = QApplication(sys.argv)
formUi = MainUi()

#formUi.editName.setText(banco.clients[0].nombre)
#formUi.editLastName.setText(banco.clients[0].apellido)
formUi.show()
sys.exit(app.exec_())

