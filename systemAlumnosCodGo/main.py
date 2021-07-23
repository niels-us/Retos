
import os
from libAlumnosCodiGo import clsAlumno
from libAlumnosCodiGo import updateAlumno
from libAlumnosCodiGo import deleteAlumno
#PROGRAMA PARA GESTÓN DE ALUMNOS
#CRUD : CREATE , READ, UPDATE, DELETE
#DEFINIR VARIABLES DE ENTRADA Y SALIDA
alumnos = []
alumno = {}
salir = 'no'

def menuopciones():
    print("*" * 20)
    print("[1] REGISTRAR ALUMNO")
    print("[2] MOSTRAR ALUMNOS")
    print("[3] ACTUALIZAR ALUMNO")
    print("[4] ELIMINAR ALUMNO")
    print("*" * 20)
    
def cargarAlumnos(strAlumnos):
        lstAlumnosData = []
        lstAlumnos = strAlumnos.splitlines()
        del lstAlumnos[0]
        for objAlumno in lstAlumnos:
            lstObjAlumno = objAlumno.split(',')
            nombre = lstObjAlumno[0]
            email = lstObjAlumno[1]
            celular = lstObjAlumno[2]
            #intancia de clase clsAlumno
            nuevoAlumno = clsAlumno(nombre,email,celular)
            # print(type(nuevoAlumno), type(nuevoAlumno.nombre))
            lstAlumnosData.append(nuevoAlumno)
            # print(lstAlumnos, type(lstAlumnos))
        return lstAlumnosData

def mostrarAlumnos():
    print("=====================")
    print("LISTADO DE ALUNMOS")
    print("=====================")
    for a in alumnos:
        print(a.nombre +" | " + a.email + " | " + a.celular)
        print("=====================")

def grabarAlumnos():
    strAlumnos = ""
    for a in alumnos:
        strAlumnos += "\n" + a.nombre + "," + a.email + "," + a.celular
    return strAlumnos  
        
fileName = r"alumnos.txt"
if(os.path.isfile(fileName)): #Evalua si el archivo existe
    fr = open(fileName,'r')
    fAlumnos = fr.read()
    # print(fAlumnos, type(fAlumnos))
    alumnos = cargarAlumnos(fAlumnos)
    # print(alumnos, alumnos[1].nombre)
    fr.close()
else:
    fr = open(fileName,'w')
    fr.write("\n")
    alumnos = []
    print(alumnos)
    fr.close()

while(salir == 'no'):
    menuopciones()
    opcion = input("INGRESE OPCIÓN: ")
    if(opcion == "1"):
        print("REGISTRO DE NUEVO ALUMNO:")
        nombre = input("NOMBRE : ")
        email = input("EMAIL : ")
        celular = input("CELULAR : ")
        nAlumno = clsAlumno(nombre,email,celular)
        # print(nAlumno.nombre)
        alumnos.append(nAlumno)
    elif(opcion == "2"):
        mostrarAlumnos()
    elif(opcion == "3"):    
        updateAlumno(alumnos)
    elif(opcion == "3"):    
        updateAlumno(alumnos)    
    elif(opcion == "4"):           
        deleteAlumno(alumnos)
        
    else:
        print("MARCO UNA OPCIÓN INCORRECTA")
        continue
    print("Desea salir del programa? ")
    salir = input()
    if(salir == "si"):
        print("ADIOS!!!!")
        strAlumnosGrabar = grabarAlumnos()
        fw = open(fileName,'w')
        fw.write(strAlumnosGrabar)
        # fw.write('')#Limpiar
        fw.close()