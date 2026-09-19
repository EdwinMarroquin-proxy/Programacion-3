class PilaTareas:

    def __init__(self):
        self.tareas = []

    def apilar(self, tarea):
        self.tareas.append(tarea)

    def desapilar(self):

        if self.esta_vacia():
            return None

        return self.tareas.pop()

    def esta_vacia(self):
        return len(self.tareas) == 0

    def cantidad(self):
        return len(self.tareas)

    def lista_desde_la_cima(self):
        return self.tareas[::-1]