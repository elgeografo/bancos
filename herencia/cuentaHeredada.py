from Cliente import Cliente

class CuentaHeredada(Cliente):
    def __init__(self, identificacion, nombre, apellido, direccion, ccc):
        Cliente.__init__(self, identificacion, nombre, apellido,direccion)
        self.ccc = ccc
    def imprimeDatos(self):
        return " %s: %s, %s, %s, %s" %(str(self.identificacion),
                               self.apellido, self.nombre,self.direccion,
                               self.ccc)
