import random

class OrdenamientosM:
    def __init__(self, cantidad):
        self.lista = [random.randint(0,20) for _ in range(cantidad)]
        self.resultado = None

    def burbuja(self):
        arr = self.lista[:]
        for i in range(len(arr)):
            for j in range(0, len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        self.resultado = arr

    def insercion(self):
        arr = self.lista[:]
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        self.resultado = arr

    def seleccion(self):
        arr = self.lista[:]
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        self.resultado = arr

    def mergesort(self):
        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr)//2
                L = arr[:mid]
                R = arr[mid:]
                merge_sort(L)
                merge_sort(R)
                i = j = k = 0
                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        arr[k] = L[i]; i += 1
                    else:
                        arr[k] = R[j]; j += 1
                    k += 1
                while i < len(L):
                    arr[k] = L[i]; i += 1; k += 1
                while j < len(R):
                    arr[k] = R[j]; j += 1; k += 1
        arr = self.lista[:]
        merge_sort(arr)
        self.resultado = arr

    def sort_python(self):
        self.resultado = sorted(self.lista)

        
    def get_resultado(self):        
        return self.resultado
    def submenu():
        continuar = True
        while continuar:
            cantidad = int(input("¿Cuántos números aleatorios desea generar?: "))
            ord = OrdenamientosM(cantidad)
            print("Lista original:", ord.lista)
            ord.burbuja(); print("Burbuja:", ord.get_resultado())
            ord.insercion(); print("Inserción:", ord.get_resultado())
            ord.seleccion(); print("Selección:", ord.get_resultado())
            ord.mergesort(); print("Mergesort:", ord.get_resultado())
            ord.sort_python(); print("Sort Python:", ord.get_resultado())

            respuesta = input("¿Desea continuar en este apartado? (s/n): ").lower()
            continuar = (respuesta == "s")
