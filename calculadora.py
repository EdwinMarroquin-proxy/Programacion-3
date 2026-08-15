import math
class Calculadora:

    def __init__(self,num1,num2,resultado):
        self.num1=num1
        self.num2=num2
        self.resultado=resultado
    def suma(self):
        self.resultado=self.num1+self.num2
    def resta(self):
        self.resultado=self.num1-self.num2
    def multiplicacion(self):
        self.resultado=self.num1*self.num2
    def division(self):
        self.resultado=self.num1/self.num2