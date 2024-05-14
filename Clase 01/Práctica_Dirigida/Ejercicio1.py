#EJERCICIO 1
nombre = input("¿Cuál es tu nombre?")
sexo = input("¿Cuál es tu sexo,(H o M)?")
if (sexo== "M" and nombre.lower()<"m") or (sexo== "H" and nombre.lower()>"n"):
    grupo= "A"
else:
    grupo = "B"
print("Tu grupo es: ",grupo)