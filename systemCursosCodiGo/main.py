from libCursosCodiGo import clsCurso
import os
from libCursosCodiGo import updateCurso
from libCursosCodiGo import deleteCurso
#PROGRAMA PARA GESTÓN DE CursoS
#CRUD : CREATE , READ, UPDATE, DELETE
#DEFINIR VARIABLES DE ENTRADA Y SALIDA
Cursos = []
Curso = {}
salir = 'no'

def menuopciones():
    print("*" * 20)
    print("[1] REGISTRAR CURSO")
    print("[2] MOSTRAR CURSO")
    print("[3] ACTUALIZAR CURSO")
    print("[4] ELIMINAR CURSO")
    print("*" * 20)
    
def cargarCursos(strCursos):
        lstCursosData = []
        lstCursos = strCursos.splitlines()
        del lstCursos[0]
        for objCurso in lstCursos:
            lstObjCurso = objCurso.split(',')
            nombre = lstObjCurso[0]
            email = lstObjCurso[1]
            celular = lstObjCurso[2]
            #intancia de clase clsCurso
            nuevoCurso = clsCurso(nombre,email,celular)
            # print(type(nuevoCurso), type(nuevoCurso.nombre))
            lstCursosData.append(nuevoCurso)
            # print(lstCursos, type(lstCursos))
        return lstCursosData

def mostrarCursos():
    print("=====================")
    print("LISTADO DE ALUNMOS")
    print("=====================")
    for a in Cursos:
        print(a.nombre +" | " + a.nota + " | " + a.codigo)
        print("=====================")

def grabarCursos():
    strCursos = ""
    for a in Cursos:
        strCursos += "\n" + a.nombre + "," + a.nota + "," + a.codigo
    return strCursos  
        
fileName = r"Cursos.txt"
if(os.path.isfile(fileName)): #Evalua si el archivo existe
    fr = open(fileName,'r')
    fCursos = fr.read()
    # print(fCursos, type(fCursos))
    Cursos = cargarCursos(fCursos)
    # print(Cursos, Cursos[1].nombre)
    fr.close()
else:
    fr = open(fileName,'w')
    fr.write("\n")
    Cursos = []
    print(Cursos)
    fr.close()

while(salir == 'no'):
    menuopciones()
    opcion = input("INGRESE OPCIÓN: ")
    if(opcion == "1"):
        print("REGISTRO DE NUEVO Curso:")
        nombre = input("NOMBRE : ")
        nota = input("NOTA : ")
        codigo = input("CODIGO : ")
        nCurso = clsCurso(nombre,nota,codigo)
        # print(nCurso.nombre)
        Cursos.append(nCurso)
    elif(opcion == "2"):
        mostrarCursos()
    elif(opcion == "3"):    
        updateCurso(Cursos)
    elif(opcion == "3"):    
        updateCurso(Cursos)    
    elif(opcion == "4"):           
        deleteCurso(Cursos)
        
    else:
        print("MARCO UNA OPCIÓN INCORRECTA")
        continue
    print("Desea salir del programa? ")
    salir = input()
    if(salir == "si"):
        print("ADIOS!!!!")
        strCursosGrabar = grabarCursos()
        fw = open(fileName,'w')
        fw.write(strCursosGrabar)
        # fw.write('')#Limpiar
        fw.close()
