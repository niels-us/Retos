notas=[]

for  n in range(4):
    nota= int(input("ingresa las notas nota" + str(n) + ": "))
    notas.append(nota)
print(notas)

prom=0
for i in notas:
    prom+=i

total= prom/len(notas)
print("tu promedio es ", total)

