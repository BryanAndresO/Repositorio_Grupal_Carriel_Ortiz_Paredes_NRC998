#UNIVERSIDAD DE LAS FUERZAS ARMADAS "ESPE"
#INTEGRANTES: CARRIEL PAMELA, ORTIZ BRYAN, PAREDES CAMILA
#NRC: 9898
#Convertir de un número decimal a Binario
import decimal
numero_decimal = decimal.Decimal(input("Ingrese un número decimal: "))
binario = ""
while numero_decimal > 0:
    binario = str(numero_decimal % 2) + binario
    numero_decimal = numero_decimal // 2
print("El número en binario es:", binario)