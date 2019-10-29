"""P4E4 - AUTOR: EYMI PARDO
Pida al usuario tres números y un cuarto número,
y compruebe si éste último es divisor de los tres números primeros"""

n1=int(input("dame un número:"))
n2=int(input("dame un número:"))
n3=int(input("dame un número:"))
divisor=int(input("dame un divisor:"))
if n1%divisor == 0:
    print (n1, "es divisor")
else:
    print (n1, "no es divisor")
if n2%divisor == 0:
    print (n2, "es divisor")
else:
    print (n2, "no es divisor")
if n3%divisor == 0:
    print (n3, "es divisor")
else:
    print (n3, "no es divisor")

