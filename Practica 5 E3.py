"""P5E3 - AUTOR: EYMI PARDO

Escribe un programa que pida dos números y escriba la suma de enteros
desde el primero hasta el último.
Dame un número: 30
Dame otro número mayor que 30: 32
La suma desde 30 hasta a 32 es: 93
30+31+32 = 93"""

num= int(input("dame un número:"))
num_2= int(input("dame otro número mayor que num:"))
suma=0
for i in range(num,num_2+1):
    suma+=i
    print("la suma desde", num, "hasta", num_2,{i})
               
