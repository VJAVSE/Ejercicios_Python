#UN NUMERO ES PAR SI ES DIVISIBLE POR 2 SIN DEJAR RESIDUO
num= int(input("INGRESA UN NÚMERO: "))
num1= num%2
resultado= num1==0
print(resultado)
if num1==0:
    print("EL NÚMERO " + str(num) + " ES PAR")
elif num1==1:
    print("EL NÚMERO " + str(num) + " ES IMPAR")
else:
    print("NO SE PUEDE DETERMINAR SI EL NÚMERO ES PAR O IMPAR")
