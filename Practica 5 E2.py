"""P5E2 - AUTOR: EYMI PARDO

Escribe un programa que pida dos números y escriba qué números
entre ese par de números son pares y cuáles impares"""

num=int(input("Dame un número:"))
num2=int(input("Dame otro número mayor que num1:"))
for num in (range(num2+1)):
    if (num%2==0):
        print ("el número", num, "es par")
    else:
        print ("el número", num, "es impar")
          
          
