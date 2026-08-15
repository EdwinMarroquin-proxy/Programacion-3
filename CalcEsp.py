import math
class Calculadoraesp:
    def __init__(self,num1,num2,resultado):
            self.num1=num1
            self.num2=num2
            self.resultado=resultado
    def seno(self,ang):
            self.resultado=math.sin(ang)
            print("el seno es: ",self.resultado)
    def coseno(self,ang):
            self.resultado=math.cos(ang)
            print("el coseno es: ",self.resultado)
    def tangente(self,ang):
            self.resultado=math.tan(ang)
            print("el tangente es: ",self.resultado)
    def raizNesima(self, num, n):
            if n == 0:
                print("Error: El índice de la raíz no puede ser cero.")
            elif num < 0 and (n % 2 == 0):
                print("Error: No existen raíces pares de números negativos en números reales.")    
            else:
                self.resultado = num ** (1/n)
                print("La raíz", n, "de", num, "es:", self.resultado)
    def potenciaNesima(self, base, exponente):
            self.resultado = base ** exponente
            print("El resultado de", base, "elevado a la", exponente, "es:", self.resultado)
    def Factorial(self, num):
            if num < 0:
                print("Error: No se puede calcular el factorial de un número negativo.")
            elif num == 0 or num == 1:
                self.resultado = 1
                print("El factorial de", num, "es:", self.resultado)
            else:
                self.resultado = 1
                for i in range(2, num + 1):
                    self.resultado *= i
                print("El factorial de", num, "es:", self.resultado)
    def mcd(self, a, b):
            if a <= 0 or b <= 0:
                print("Error: Los números deben ser mayores que cero.")
            else:
                while b != 0:
                    a, b = b, a % b
                self.resultado = a
                print("El MCD de es:", self.resultado)
    def mcm(self, a, b):
            if a<=0 or b<=0:
                print("Error: Los números deben ser mayores que cero para calcular el MCM.")
                return None
            else:
                producto = a * b
                while b !=0:
                    a, b = b, a % b
                self.resultado = producto // a
                print("El MCM de es:", self.resultado)
    def fibonacci(self, n):
            if n <= 0:
                print("El numero debe ser mayor que 0")
            else:
                a, b = 0, 1
                for _ in range (1,n):
                    a, b = b, a + b
                self.resultado = b
    def iva(self, precio, porcentaje):
            self.resultado = precio * (porcentaje / 100)
            print("El IVA es:", self.resultado)