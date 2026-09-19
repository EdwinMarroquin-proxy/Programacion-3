class Documento:

    def __init__(self, nombre, numero_paginas, tiempo_por_pagina):
        self.nombre = nombre
        self.numero_paginas = numero_paginas
        self.tiempo_por_pagina = tiempo_por_pagina
    def tiempo_total(self):
        return self.numero_paginas * self.tiempo_por_pagina

    def __str__(self):
        return f"{self.nombre} - {self.numero_paginas} páginas"
