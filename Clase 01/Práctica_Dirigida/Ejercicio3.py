#EJERCICIO3
edad= int(input("¿Cuál es tu edad?"))
if edad < 4:
    print("Entrada gratuita")
elif edad >= 4 and edad <= 18:
    print("El precio de la entrada es de 5€")
else:
    print("El precio de la entrada es de 10€")