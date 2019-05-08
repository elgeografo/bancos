class Persona(object):
    "Clase que representa una persona."
    def __init__(self, identificacion, nombre, apellido):
        "Constructor de Persona"
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido
    def imprimeDatos(self):
        return " %s: %s, %s" %(str(self.identificacion), self.apellido, self.nombre)