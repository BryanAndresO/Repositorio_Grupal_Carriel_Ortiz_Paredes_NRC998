import decimal
numero_decimal = decimal.Decimal(input("Ingrese un número decimal: "))
binario = ""
while numero_decimal > 0:
    binario = str(numero_decimal % 2) + binario
    numero_decimal = numero_decimal // 2
print("El número en binario es:", binario)