#Escribir programa en el que se pregunta al usuario por una frase
#y una letra, y muestre por pantalla el número de veces que aparece
#la letra en la frase.
#contadores

frase= input("Introduce una frase: ")
letra= input("Introduce una letra: ")
contador=0
print(contador)
fraseminuscula= frase.lower()

for i in fraseminuscula:
    if i==letra:
        contador+=1
print("La letra",letra,"aparece",contador, "en la frase: ",frase)
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra,contador,frase))
#%2i ese 2 indica el número de espacios que aparezca.    