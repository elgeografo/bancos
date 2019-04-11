from ClienteBanco import ClienteBanco

class Banco:
    def __init__(self):
        self.clients = []
    def addClient(self,client):
        self.clients.append(client)

    def imprimeClientes(self):
        for cli in self.clients:
            print(cli.nombre)

    def loadClientsFromFile(self):
        with open('somefile.txt') as the_file:
            for line in the_file:
            #line = the_file.readline()
            #while line:
                self.loadClientFromLine(line)

    def loadClientFromLine(self,line):
        data = line.split(",")
        cliente = ClienteBanco()
        cliente.nombre = data[0]
        cliente.apellido = data[1]
        cliente.ccc = data[2]
        cliente.dni = data[3]
        cliente.saldo = int(data[4])
        self.addClient(cliente)


    def saveClientsToFile(self):
        with open('somefile.txt', 'w') as the_file:
            for client in self.clients:

                texto = client.nombre + "," + \
                    client.apellido + "," + \
                    client.ccc + "," + \
                    client.dni + "," + \
                    str(client.saldo) + "\n"

                the_file.write(texto)
