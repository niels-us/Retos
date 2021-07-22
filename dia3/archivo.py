# f=open('alumnos.txt','a')
# print("REGISTRO ALUMNO")
# nombre=input("NOMBRE: ")
# email=input("EMAIL: ")
# celular=input("CELULAR: ")


# f.write('\n' + nombre + "," + email + "," + celular)
# f.close()

fr= open('alumnos.txt','r')
alumnos= fr.read()
print(alumnos)

lstAlumnosData=[]

lstAlumnos=alumnos.splitlines()
print(lstAlumnos)
del lstAlumnos[0]
for objAlumno in lstAlumnos:
    lstObjAlumno = objAlumno.split(',')
    print(lstObjAlumno)
    nombre=lstObjAlumno[0]
    email=lstObjAlumno[1]
    celular=lstObjAlumno[2]
    dictAlumno={
        'nombre':nombre,
        'email':email,
        'celular':celular
    }
    
    lstAlumnosData.append(dictAlumno)
print(lstAlumnosData)

fr.close
    