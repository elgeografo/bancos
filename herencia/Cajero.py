from Persona import Persona

class Cajero(Persona):
    "Clase que representa a un Cajero."
    def __init__(self, identificacion, nombre, apellido, oficina):
        "Constructor de AlumnoFIUBA"
        # llamamos al constructor de Persona
        Persona.__init__(self, identificacion, nombre, apellido)
        self.oficina = oficina
        # agregamos el nuevo atributo
        self.clientesAsignados = []

    def addClient(self, client):
        self.clientesAsignados.append(client)

    def imprimeClientesAsignados(self):
        print(" CLIENTES ASIGNADOS")
        for cli in self.clientesAsignados:
            print("    " + cli.imprimeDatos() + ", " + cli.direccion)

