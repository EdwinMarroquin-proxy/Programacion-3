import tkinter as tk
from documento import Documento
from cola_impresion import ColaImpresion
class VentanaImpresion:
    def __init__(self):
        self.cola = ColaImpresion()
        self.documento_actual = None
        self.pagina_actual = 0
        self.imprimiendo = False
        self.ventana = tk.Tk()
        self.ventana.title("Impresora")
        self.ventana.geometry("700x600")
        tk.Label(
            self.ventana,
            text="IMPRESORA",
            font=("Arial", 16, "bold")
        ).pack(pady=10)
        tk.Label(
            self.ventana,
            text="Nombre del documento"
        ).pack()
        self.caja_nombre = tk.Entry(self.ventana)
        self.caja_nombre.pack()
        tk.Label(
            self.ventana,
            text="Numero de paginas"
        ).pack()
        self.caja_paginas = tk.Entry(self.ventana)
        self.caja_paginas.pack()
        tk.Label(
            self.ventana,
            text="Tiempo por pagina"
        ).pack()
        self.caja_tiempo = tk.Entry(self.ventana)
        self.caja_tiempo.pack()
        tk.Button(
            self.ventana,
            text="Agregar Documento",
            command=self.agregar_documento
        ).pack(pady=10)
        tk.Label(
            self.ventana,
            text="Cola de Impresion"
        ).pack()
        self.lista_cola = tk.Listbox(
            self.ventana,
            width=60,
            height=8
        )
        self.lista_cola.pack()
        tk.Button(
            self.ventana,
            text="Iniciar Impresion",
            command=self.iniciar_impresion
        ).pack(pady=5)
        tk.Button(
            self.ventana,
            text="Detener Impresion",
            command=self.detener_impresion
        ).pack(pady=5)
        self.estado = tk.Label(
            self.ventana,
            text="Estado: Sin documentos"
        )
        self.estado.pack(pady=10)
        tk.Label(
            self.ventana,
            text="Registro"
        ).pack()
        self.area_texto = tk.Text(
            self.ventana,
            width=60,
            height=10
        )

        self.area_texto.pack()

    def agregar_documento(self):

        nombre = self.caja_nombre.get()
        paginas = self.caja_paginas.get()
        tiempo = self.caja_tiempo.get()

        if nombre == "":
            self.estado.config(text="Error: Ingrese un nombre")
            return

        if paginas == "":
            self.estado.config(text="Error: Ingrese las paginas")
            return

        if tiempo == "":
            self.estado.config(text="Error: Ingrese el tiempo")
            return

        if paginas.isdigit() == False:
            self.estado.config(text="Error: Paginas invalidas")
            return

        if tiempo.isdigit() == False:
            self.estado.config(text="Error: Tiempo invalido")
            return

        documento = Documento(
            nombre,
            int(paginas),
            int(tiempo)
        )

        self.cola.encolar(documento)

        self.lista_cola.insert(
            tk.END,
            str(documento)
        )

        self.area_texto.insert(
            tk.END,
            "Documento agregado: " + nombre + "\n"
        )

        self.estado.config(
            text="Estado: Documento agregado"
        )

        self.caja_nombre.delete(0, tk.END)
        self.caja_paginas.delete(0, tk.END)
        self.caja_tiempo.delete(0, tk.END)

    def iniciar_impresion(self):
        if self.imprimiendo:
            return
        if self.cola.esta_vacia():
            self.estado.config(
                text="Estado: No hay documentos"
            )
            return
        self.imprimiendo = True
        self.documento_actual = self.cola.desencolar()
        self.lista_cola.delete(0)
        self.pagina_actual = 0
        self.imprimir_pagina()
    def imprimir_pagina(self):
        if self.imprimiendo == False:
            return
        self.pagina_actual += 1
        self.area_texto.insert(
            tk.END,
            self.documento_actual.nombre
            + " - pagina "
            + str(self.pagina_actual)
            + " de "
            + str(self.documento_actual.numero_paginas)
            + "\n"
        )
        self.estado.config(
            text="Imprimiendo " + self.documento_actual.nombre
        )
        if self.pagina_actual >= self.documento_actual.numero_paginas:

            self.area_texto.insert(
                tk.END,
                "Documento terminado: "
                + self.documento_actual.nombre
                + "\n"
            )

            self.imprimiendo = False

            self.estado.config(
                text="Estado: Documento terminado"
            )

            return

        self.ventana.after(
            self.documento_actual.tiempo_por_pagina * 1000,
            self.imprimir_pagina
        )

    def detener_impresion(self):

        self.imprimiendo = False

        self.estado.config(
            text="Estado: Impresion detenida"
        )

    def arrancar(self):
        self.ventana.mainloop()
ventana = VentanaImpresion()
ventana.arrancar()