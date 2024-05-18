#BUCLES
#FOR, WHILE DO-WHILE
#CONDICIONALES IF, SWITCH
#i++ significa incremento en 1
#i+= incremento en 2
#en el for i si por ejemplo quiero que vaya hasta el 10
#le debo sumar 1 más, sería 11.
for i in range (0,11,2): #que parta de 0, llegue a 10 y incremente de 2 en 2.
   print(i)

#a)Escribir un programa que pida al usuario un número entero positivo y
#muestre por pantalla todos los números impares desde 1 hasta 
#ese número seoarados por comas.
n= int(input("Introduce un número entero positivo: "))
#bucles
#como quiero que se muestren los números recorridos
#en este caso separados por comas.
#el end sirve para como quiero que termine al recorrer cada uno.

for i in range(1,n+1,2):
   print(i, end=",")

#b)Escribir un programa que muestre el eco de todo lo que el usuario
#introduzca hasta que el usuario escriba "salir", y así terminar
#el programa.

while True:
    frase= input("Introduce el texto/palabra: ")
    if frase=="salir":
        break
    print(frase) #se pone print(frase) para comparar el texto con "salir" y compararlo.
    



