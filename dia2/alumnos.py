alumnos=[]
alumno={}
salir='no'

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
            
def deleteAlumno():          
    
    

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
        readAlumno()
    elif(opcion=='3'):
        
    else:
        print('opcion incorrecta')
        
    print('desea salir del programa?')
    salir= input()