from calculadora import Calculadora
from CalcEsp import Calculadoraesp
from caltrig import CalTrig
#interaccion usuario
continuar="s"
miCalc= Calculadora(0,0,0)
miCalct= CalTrig(0,0,0)
miCalcEsp = Calculadoraesp(0,0,0)
marcador = "n"
print("----------Bienvenido calculadora--------------")
while (continuar=="s"):
    if marcador == "s":
        miCalc.num1=miCalc.resultado
    print("1. Suma \n2. Resta \n3. Multiplicacion\n4. Division\n5. Seno\n6. Coseno\n7. Tangente\n8. Raiz N-esima\n9. Potencia N-esima\n10. Factorial\n11. MCD\n12. MCM\n13. Fibonacci\n14. IVA")
    opcion=int(input("escoja alguna de las opciones "))
    match opcion:
        case 1:
            if marcador == "n":
                miCalc.num1=int(input("ingrese numero 1: "))
            miCalc.num2=int(input("ingrese numero 2: "))
            miCalc.suma()
            print("El resultado de la operacion es: ", miCalc.resultado)
        case 2:
            if marcador == "n":
                miCalc.num1=int(input("ingrese el minuendo: "))
            miCalc.num2=int(input("ingrese el sustraendo: "))
            miCalc.resta()
            print("La diferencia de la operacion es: ", miCalc.resultado)
        case 3:
            if marcador == "n":
                miCalc.num1=int(input("ingrese numero 1: "))
            miCalc.num2=int(input("ingrese numero 2: "))
            miCalc.multiplicacion()
            print("El producto de la operacion es: ", miCalc.resultado)
        case 4:
            if marcador == "n":
                miCalc.num1=int(input("ingrese dividendo: "))
            miCalc.num2=int(input("ingrese divisor: "))
            miCalc.division()
            print("El cociente de la operacion es: ", miCalc.resultado)
        case 5:
            if marcador == "n":
                angulo=int(input("ingrese el angulo: "))
            else:
                angulo=miCalct.num1
            miCalct.seno(angulo)
        case 6:
            if marcador == "n":
                angulo=int(input("ingrese el angulo: "))
            else:
                angulo=miCalct.num1
            miCalct.coseno(angulo)
        case 7:
            if marcador == "n":
                angulo=int(input("ingrese el angulo: "))
            else:
                angulo=miCalct.num1
            miCalct.tangente(angulo)
        case 8:
            if marcador == "n":
                miCalcEsp.num1=int(input("ingrese el numero: "))
            miCalcEsp.num2=int(input("ingrese el indice de la raiz: "))
            miCalcEsp.raizNesima(miCalcEsp.num1, miCalcEsp.num2)
        case 9:
            if marcador == "n":
                miCalcEsp.num1=int(input("ingrese la base: "))
            miCalcEsp.num2=int(input("ingrese el exponente: "))
            miCalcEsp.potenciaNesima(miCalcEsp.num1, miCalcEsp.num2)
        case 10:
            if marcador == "n":
                miCalcEsp.num1=int(input("ingrese el numero: "))
            miCalcEsp.Factorial(miCalcEsp.num1)
        case 11:
            if marcador == "n":
                miCalcEsp.num1=int(input("ingrese el primer numero: "))
            miCalcEsp.num2=int(input("ingrese el segundo numero: "))
            miCalcEsp.mcd(miCalcEsp.num1, miCalcEsp.num2)
        case 12:
            if marcador == "n":
                miCalcEsp.num1=int(input("ingrese el primer numero: "))
            miCalcEsp.num2=int(input("ingrese el segundo numero: "))
            miCalcEsp.mcm(miCalcEsp.num1, miCalcEsp.num2)
        case 13:
            if marcador == "n":
                miCalcEsp.num1=int(input("ingrese el numero de serie: "))
            miCalcEsp.fibonacci(miCalcEsp.num1)
        case 14:
            miCalcEsp.num1=int(input("ingrese el precio: "))
            miCalcEsp.num2=int(input("ingrese el porcentaje de IVA: "))
            miCalcEsp.iva(miCalcEsp.num1, miCalcEsp.num2)
        case _:
            print("opcion no valida")
    continuar=input("Desea continuar con otra operacion? s/n: ")
    marcador=input("Desea usar el resultado de la operacion anterior como primer numero? s/n: ")