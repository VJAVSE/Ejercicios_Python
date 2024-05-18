#Escribir un programa que almacene el diccionario con los créditos
#de las asignaturas de un curso {Matematicas':6,'Fisica':4 'Quimica':5}
#y despues muestre por pantalla los creditos de cada asignatura en el
#formato <asignatura> tiene <creditos> credito, donde asignatura es cada
#una de las asignaturas del curso y <creditos> son sus creditos.
#Al final debe mostrar tambien el numero total de crerditos del curso.

curso= {'Matematicas': 6, 'Fisica': 4, 'Quimica': 5}
total_creditos=0
for asignatura,credito in curso.items():
    print(asignatura, 'tiene', credito, 'creditos')
    total_creditos+=credito
    print('Numero total de creditos del curso: ',total_creditos)