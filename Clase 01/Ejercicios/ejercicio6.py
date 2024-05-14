
A = int(input("INGRESA UN NÚMERO: "))
B = int(input("INGRESA UN NÚMERO: "))
C = int(input("INGRESA UN NÚMERO: "))

if A>B and A>C:
    print("EL NÚMERO MAYOR ES ",A)
elif B>A and B>C:
    print("EL NÚMERO MAYOR ES ",B)
elif C>A and C>B:
    print("EL NÚMERO MAYOR ES ",C)
else:
    print("NO SE PUEDE DETERMINAR EL CUAL ES EL NÚMERO MAYOR")
