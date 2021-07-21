# capitales={'peru':'lima','ecuador':'quito'}
# capital = {'usa':'washintong DC'}
# capitales.update(capital)
# print(capitales['peru'])
# print(capitales)

alumnos ={
    'nombre':'cesar mayta',
    'email':'caesarmayta@gmail.com',
    'celular':'986787656'
}

print(alumnos['email'])
alumnosModelo=alumnos.copy()
alumnos['email']='cesar@outlook.com'
print(alumnos['email'])
print(alumnosModelo)
alumnos.pop('celular')
a=alumnos.pop('celular', 'no existe el celular')
print(a)
print(alumnos)
print(alumnos.keys())
print(alumnos.values())


for clave in alumnos:
    print(clave, alumnos[clave])


for clave in alumnos.keys():
    print(clave, alumnos[clave])


for clave, valor in alumnos.items():
    print(clave, valor)
    

alumnos={}
alumnos.clear()