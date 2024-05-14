import math
oper1=int(input("INGRESA EL NÚMERO 1: "))
oper2=int(input("INGRESA EL NÚMERO 2: "))
suma= oper1+oper2
resta=oper1-oper2
multiplicacion=oper1*oper2
division= oper1/oper2
operacion= (oper1+oper2-suma)*multiplicacion
num1_redondeado= round(division,2)
num2_redodneadosindecimal= round(division)
potencia= oper1**2
potencia2= math.pow(oper1,3)
raiz_cuadrada= math.sqrt(oper1)
residuo=oper1%oper2
print("La suma es: ",suma)
print("La resta es: ",resta)
print("La multiplicación es: ",multiplicacion)
print("La division es: ",division)
print("La operacion es: ",operacion)
print("El número redondeado es: ",num1_redondeado)
print("El número redondeado sin decimal es: ",num2_redodneadosindecimal)
print("la potencia primera es: ",potencia)
print("La potencia es: ",potencia2)
print("La raíz es: ",raiz_cuadrada)
print("El residuo es: ", residuo)