# Connector.py by Andrew Sosa

class Connector():
    def __init__(self, client):
        self.client = client

    def write(self, string):
        self.client.send(string)

    def readline(self):
        return self.client.recv(15)
