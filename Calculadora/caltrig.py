import math
class CalTrig:

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