"""P5E4 - AUTOR: EYMI PARDO

Escribe un programa que pida un número y calcule su factorial.
Dame un número: 5
El factorial de 5 es: 120"""

numero = int(input("Escriba un número entero mayor que cero: "))
if numero <= 0:
    print("¡Le he pedido un número entero mayor que cero!")
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial = factorial * i
    print(f"El factorial de {numero} es {factorial}.")
