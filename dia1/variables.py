# variables e python

# name="niels"
# print("hola mi nombre es ada, cual es tu nombre:")
# name=input("ingresa tu nombre")
# print("mucho enn gusto en conocerte " + name)
# print("vamos a sumar 2 numeros")
# n1=input("ingresa el primer numero:")
# n2=input("ingresa el segundo numero:")
# suma= int(n1) + int(n2)
# print("la suma de "+ str(n1) + " mas " + str(n2) + " igula " + str(suma))
# print("====================================")
# n1=float(input("ingresa tu monto en soles "))
# n2=float(input("ingresa el valor del dolar "))
# total = n1 * n2
# print("tu conversion es " , total)
print("====================================")
print("ingrese el valor a dolares:")
moneda=float(input())
print("ingrese la moneda a convertir: ")
monedaConvertir=input()
if monedaConvertir=="soles":
    tipoCambio=3.98
elif monedaConvertir=="euros":
    tipoCambio=0.85
elif monedaConvertir=="bit":
    tipoCambio=100
else:
    tipoCambio=1

valorMonedaConvertir=moneda * tipoCambio

if(valorMonedaConvertir==moneda):
    print("No indico una moneda valida")
else:
    print("el valor en " + monedaConvertir + " es de " + str(valorMonedaConvertir))



