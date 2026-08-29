class OperacionesMatrices:
    def __init__(self, matrizA=None, matrizB=None, vector=None):
        self.matrizA = matrizA
        self.matrizB = matrizB
        self.vector = vector
        self.resultado = None

    def suma(self):
        filas = len(self.matrizA)
        columnas = len(self.matrizA[0])
        self.resultado = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                fila.append(self.matrizA[i][j] + self.matrizB[i][j])
            self.resultado.append(fila)

    def producto(self):
        filasA, colsA = len(self.matrizA), len(self.matrizA[0])
        filasB, colsB = len(self.matrizB), len(self.matrizB[0])
        self.resultado = [[0]*colsB for _ in range(filasA)]
        for i in range(filasA):
            for j in range(colsB):
                for k in range(colsA):
                    self.resultado[i][j] += self.matrizA[i][k] * self.matrizB[k][j]

    def producto_vector(self):
        self.resultado = []
        for i in range(len(self.matrizA)):
            suma = 0
            for j in range(len(self.vector)):
                suma += self.matrizA[i][j] * self.vector[j]
            self.resultado.append(suma)

    def inversa(self):
        # Método Gauss-Jordan
        n = len(self.matrizA)
        M = [row[:] for row in self.matrizA]
        I = [[float(i == j) for j in range(n)] for i in range(n)]
        for i in range(n):
            factor = M[i][i]
            for j in range(n):
                M[i][j] /= factor
                I[i][j] /= factor
            for k in range(n):
                if k != i:
                    factor = M[k][i]
                    for j in range(n):
                        M[k][j] -= factor * M[i][j]
                        I[k][j] -= factor * I[i][j]
        self.resultado = I
        
    def get_resultado(self):
        return self.resultado
    def submenu():
        continuar = True
        while continuar:
            print("\n--- SUBMENÚ MATRICES ---")
            print("1. Suma\n2. Producto\n3. Inversa\n4. Producto por vector")
            opcion = input("Seleccione: ")

            match opcion:
                case "1":
                    filas = int(input("Número de filas: "))
                    columnas = int(input("Número de columnas: "))
                    A = OperacionesMatrices.leer_matriz(filas, columnas)
                    B = OperacionesMatrices.leer_matriz(filas, columnas)
                    op = OperacionesMatrices(A, B)
                    op.suma()
                    print("Resultado:", op.get_resultado())
                case "2":
                    filasA = int(input("Filas de A: "))
                    columnasA = int(input("Columnas de A: "))
                    A = OperacionesMatrices.leer_matriz(filasA, columnasA)
                    filasB = int(input("Filas de B: "))
                    columnasB = int(input("Columnas de B: "))
                    B = OperacionesMatrices.leer_matriz(filasB, columnasB)
                    op = OperacionesMatrices(A, B)
                    op.producto()
                    print("Resultado:", op.get_resultado())
                case "3":
                    n = int(input("Tamaño de la matriz cuadrada: "))
                    A = OperacionesMatrices.leer_matriz(n, n)
                    op = OperacionesMatrices(A)
                    op.inversa()
                    print("Resultado:", op.get_resultado())
                case "4":
                    filas = int(input("Número de filas: "))
                    columnas = int(input("Número de columnas: "))
                    A = OperacionesMatrices.leer_matriz(filas, columnas)
                    v = OperacionesMatrices.leer_vector(columnas)
                    op = OperacionesMatrices(A, vector=v)
                    op.producto_vector()
                    print("Resultado:", op.get_resultado())
                case _:
                    print("Número no válido")

            respuesta = input("¿Desea continuar en este apartado? (s/n): ").lower()
            continuar = (respuesta == "s")

    def leer_matriz(filas, columnas):
        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                valor = float(input(f"Ingrese valor [{i},{j}]: "))
                fila.append(valor)
            matriz.append(fila)
        return matriz

    def leer_vector(longitud):
        vector = []
        for i in range(longitud):
            valor = float(input(f"Ingrese valor del vector[{i}]: "))
            vector.append(valor)
        return vector
