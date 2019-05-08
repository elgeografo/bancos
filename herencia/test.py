from Cajero import Cajero
from Cliente import Cliente
from cuentaHeredada import CuentaHeredada

'''
cajero1 = Cajero("DNI 45454545C", "Pepe", "Perez","2803")
cliente1 =  Cliente("DNI 676767D", "Juan", "Fernandez","Calle Musgo Nº 5, Madrid")
cliente2 =  Cliente("DNI 989898C", "Luis", "Izquierdo","Calle Seseña Nº 22, Murcia")
cliente3 =  Cliente("DNI 323232X", "Jose", "Ruiz","Calle Musgo Nº 9, Cadiz")
cajero1.addClient(cliente1)
cajero1.addClient(cliente2)
cajero1.addClient(cliente3)

print(cajero1.imprimeDatos())
print(cajero1.imprimeClientesAsignados())

'''

#ch = CuentaHeredada("DNI 45454545C", "Pepe", "Perez","Calle Musgo Nº 9, Cadiz", "0075 2323 78 9876854367")
#print(ch.imprimeDatos())

cli = Cliente("DNI 45454545C", "Pepe", "Perez","Calle Musgo Nº 9, Cadiz")
cc = CuentaComposicion(cli)