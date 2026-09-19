class ColaImpresion:

    def __init__(self):
        self.documentos = []

    def encolar(self, documento):
        self.documentos.append(documento)

    def desencolar(self):
        if self.esta_vacia():
            return None

        return self.documentos.pop(0)

    def esta_vacia(self):
        return len(self.documentos) == 0

    def cantidad(self):
        return len(self.documentos)

    def lista_de_documentos(self):
        return self.documentos