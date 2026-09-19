import tkinter as tk
from tarea import Tarea
from pila_tareas import PilaTareas
class VentanaRobot:

    def __init__(self):
        self.pila = PilaTareas()
        self.tarea_actual = None
        self.ejecutando = False
        self.terminadas = 0
        self.ventana = tk.Tk()
        self.ventana.title("Robot")
        self.ventana.geometry("700x600")
        tk.Label(
            self.ventana,
            text="ROBOT",
            font=("Arial", 16, "bold")
        ).pack(pady=10)
        tk.Label(
            self.ventana,
            text="Tiempo sensores"
        ).pack()
        self.caja_ts = tk.Entry(self.ventana)
        self.caja_ts.pack()
        tk.Label(
            self.ventana,
            text="Tiempo movimiento"
        ).pack()
        self.caja_tm = tk.Entry(self.ventana)
        self.caja_tm.pack()
        tk.Label(
            self.ventana,
            text="Nombre de la tarea"
        ).pack()
        self.caja_nombre = tk.Entry(self.ventana)
        self.caja_nombre.pack()
        self.tipo = tk.StringVar()
        self.tipo.set("sensores")
        tk.OptionMenu(
            self.ventana,
            self.tipo,
            "sensores",
            "movimiento"
        ).pack()
        tk.Button(
            self.ventana,
            text="Apilar Tarea",
            command=self.agregar_tarea
        ).pack(pady=10)
        tk.Label(
            self.ventana,
            text="Pila de Tareas"
        ).pack()
        self.lista_pila = tk.Listbox(
            self.ventana,
            width=60,
            height=8
        )
        self.lista_pila.pack()
        tk.Button(
            self.ventana,
            text="Iniciar Tareas",
            command=self.iniciar_simulacion
        ).pack(pady=5)
        tk.Button(
            self.ventana,
            text="Detener Tareas",
            command=self.detener_simulacion
        ).pack(pady=5)
        self.estado = tk.Label(
            self.ventana,
            text="Estado: Sin tareas"
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
    def agregar_tarea(self):
        nombre = self.caja_nombre.get()
        if nombre == "":
            self.estado.config(
                text="Error: Ingrese un nombre"
            )
            return
        if self.tipo.get() == "sensores":
            tiempo = self.caja_ts.get()
        else:
            tiempo = self.caja_tm.get()
        if tiempo == "":
            self.estado.config(
                text="Error: Ingrese un tiempo"
            )
            return
        if tiempo.isdigit() == False:
            self.estado.config(
                text="Error: Tiempo inválido"
            )
            return
        tarea = Tarea(
            nombre,
            self.tipo.get(),
            int(tiempo)
        )
        self.pila.apilar(tarea)
        self.lista_pila.insert(
            0,
            str(tarea)
        )
        self.area_texto.insert(
            tk.END,
            "Tarea agregada: " + nombre + "\n"
        )
        self.estado.config(
            text="Estado: Tarea agregada"
        )
        self.caja_nombre.delete(0, tk.END)
    def iniciar_simulacion(self):
        if self.ejecutando:
            return
        if self.pila.esta_vacia():
            self.estado.config(
                text="Estado: No hay tareas"
            )

            return
        self.ejecutando = True
        self.tarea_actual = self.pila.desapilar()
        self.lista_pila.delete(0)
        self.area_texto.insert(
            tk.END,
            "Ejecutando: "
            + self.tarea_actual.nombre
            + "\n"
        )
        self.estado.config(
            text="Ejecutando: "
            + self.tarea_actual.nombre
        )
        self.ventana.after(
            self.tarea_actual.tiempo_ejecucion * 1000,
            self.terminar_tarea
        )
    def terminar_tarea(self):
        if self.ejecutando == False:
            return
        self.area_texto.insert(
            tk.END,
            "Tarea terminada: "
            + self.tarea_actual.nombre
            + "\n"
        )
        self.terminadas += 1
        self.estado.config(
            text="Tareas terminadas: "
            + str(self.terminadas)
        )
        self.ejecutando = False
        self.tarea_actual = None
    def detener_simulacion(self):
        self.ejecutando = False
        self.estado.config(
            text="Estado: Tareas detenidas"
        )
    def arrancar(self):
        self.ventana.mainloop()
ventana = VentanaRobot()
ventana.arrancar()