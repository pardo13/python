a=int(input("ingresa un numero\n"))
b=int(input("ingresa un numero\n"))
c=int(input("ingresa un numero\n"))
d=int(input("ingresa un numero\n"))
e=int(input("ingresa un numero\n"))
if(a > b > c > d > e):
    print(a,",",b,",",c,",",d,",",e," Estan en orden decreciente")
elif(a < b < c < d < e):
    print(a,",",b,",",c,",",d,",",e," Estan en orden creciente")
else:
    print(a,",",b,",",c,",",d,",",e," Estan desordenadas")

