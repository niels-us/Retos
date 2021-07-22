alumnos=[]
alumno={}
salir='no'

def leerDatos():
    
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
         return lstAlumnosData
    #  print(lstAlumnosData)
     
     fr.close

def createAlumno(nombre,email,celular):
     nuevoAlumno={
            'nombre': nombre,
            'email':email,
            'celular': celular
        }     
     alumnos.append(nuevoAlumno)
     return 1
    
def readAlumno():
    print('listado de alumnos')
    print(alumnos)
    for a in alumnos:            
        print('alumno: ')
        for clave,valor in a.items():
            print(clave , " : " , valor)   
            
def updateAlumno():
    print("ACTUALIZAR ALUMNO")
    posAlumno=0
    alumnoBusqueda = input("Ingrese el nombre del alumno")
    for a in alumnos:
        for clave,valor in a.items():
            if valor==alumnoBusqueda:
                         
    
    

while(salir=='no'):
    print("opciones: 1-registrar_alumno 2-mostrar_alumno 3-eliminar_alumno")
    opcion=input()
    if(opcion=='1'):
        print('registro de nuevo alumno:')
        nombre=input("nombre: ")
        email=input("email: ")
        celular=input("celular: ")        
        r=createAlumno(nombre,email,celular)
        if r==1:
            print('resgistro existoso')
        
    elif(opcion=='2'):
        leerDatos()
        # readAlumno()
    elif(opcion=='3'):
        
    else:
        print('opcion incorrecta')
        
    print('desea salir del programa?')
    salir= input()