#Escribir un programa que almacene las asignaturas de un curos
#por ejemplo Matematicas, Fisica, Quimica, Historia y Lengua
#en una lista, pregunte al usuario la nota que ha sacado en cada
#asignatura y despues las muestre por pantalla con el mensaje 
#En <asignatura> has sacado <nota> donde <asignatura> es cada una
#de las asignaturas de la lista y <nota> cada una de las correspondientes
#notas introducidas por el usuario.

asignaturas= ["Matematicas","Fisica","Quimica","Historia","Lengua"]
notas=[]
for asignatura in asignaturas:
    nota=input("¿Qué nota has sacado en: "+asignatura+"?  ")
    notas.append(nota)

for i in range(len(asignaturas)):
    print("En "+asignaturas[i]+ "has sacado: "+notas[i])