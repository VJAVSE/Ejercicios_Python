
num=int(input("INGRESA UN NÚMERO ENTERO: "))
divisible3= num%3
divisible5= num%5
if divisible3==0:
    print("EL NÚMERO " + str(num) + " ES DIVISIBLE POR 3")
elif divisible5==0:
    print("EL NÚMERO " + str(num) + " ES DIVISIBLE POR 5")
else:
    print("EL NÚMERO " + str(num) + " NO ES DIVISIBLE NI POR 3 NI POR 5")

