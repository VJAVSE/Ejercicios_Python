#if (SI) elif cuando agrego otra condicion, sintaxis: if-elif-else
nota= float(input("Ingresa una calificación entre (0-100): "))

if nota >=90 and nota<=100:
    print("LA CALIFICACIÓN ES: A")
elif nota>=80 :
    print("LA CALIFICACIÓN ES: B")
elif nota>=70:
    print("LA CALIFICACIÓN ES: C")
elif nota>60:
    print("LA CALIFICACION ES: D")
else:
    print("LA CALIFICACIÓN ES: F")