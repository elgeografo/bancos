from Persona import Persona

class Cliente(Persona):
    "Clase que representa a un Cajero."
    def __init__(self, identificacion, nombre, apellido, direccion):
        "Constructor de Cliente"
        # llamamos al constructor de Persona
        Persona.__init__(self, identificacion, nombre, apellido)
        self.direccion = direccion