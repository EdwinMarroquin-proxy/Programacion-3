class Tarea:
    def __init__(self, nombre, tipo, tiempo_ejecucion):
        self.nombre = nombre
        self.tipo = tipo
        self.tiempo_ejecucion = tiempo_ejecucion
    def __str__(self):
        return (
            self.nombre
            + " - "
            + self.tipo
            + " - "
            + str(self.tiempo_ejecucion)
            + " s"
        )