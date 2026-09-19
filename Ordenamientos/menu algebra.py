from operaciones import OperacionesMatrices
from ordenamientos import OrdenamientosM


continuar = True
while continuar:
    print("\n--- MENÚ ---")
    print("1. Operaciones con matrices\n2. Algoritmos de ordenamiento\n3. Salir")
    opcion = input("Seleccione: ")

    match opcion:
        case "1":
            OperacionesMatrices.submenu()
        case "2":
            OrdenamientosM.submenu()
        case "3":
                continuar = False
        case _:
            print("Numero no valido")