#PROGRAMA PARA GESTÓN DE ALUMNOS
#CRUD : CREATE , READ, UPDATE, DELETE
#DEFINIR VARIABLES DE ENTRADA Y SALIDA
alumnos = [
           {
            'nombre': 'niels',
            'email': 'niels_us@outlook.com',
            'celular': '980400440'
           },
           {
            'nombre': 'jhon',
            'email': 'jhon_tr@outlook.com',
            'celular': '985555550'
           },
           {
            'nombre': 'juan',
            'email': 'juan_tr@outlook.com',
            'celular': '986666660'
           }
          ]
alumno = {}
salir = 'no'
#LOGICA

def createAlumno(nombre,email,celular):
    nuevoAlumno = {
            'nombre': nombre,
            'email': email,
            'celular': celular
        }
    alumnos.append(nuevoAlumno)
    return 1
def readAlumno():
    print("LISTADO DE ALUNMOS")
    for a in alumnos:
        print("=====================")
        for clave,valor in a.items():
            print(clave + " : " + valor)

def deleteAlumno():    
    print("============================================================")
    try:
      codigoEliminar=int(input('Ingresa el numero del codigo de alumno a ELIMINAR: '))
      alumnoEliminado=alumnos[codigoEliminar]
      alumnos.pop(codigoEliminar) 
      print('Alumno ', alumnoEliminado ,' fue Eliminado con exito!!!!!!!!!!')
      print("============================================================")
    except:
      print("=====> ¡¡¡¡¡¡¡ No existe esa opcion, intentalo nuevamente !!!!!!!!!!!!!!!")
    #   listAlumnosCodigo()
      deleteAlumno()
      
def updateAlumno(): 
    print("============================================================")
    try:
      codigoModificar=int(input('Ingresa el numero del codigo de alumno a ACTUALIZAR: '))
      print("REGISTRE LOS CAMBIOS DEL ALUMNO:")
      nombre = input("NOMBRE : ")
      email = input("EMAIL : ")
      celular = input("CELULAR : ")      
      changeAlumno = {'nombre': nombre,'email': email,'celular': celular}      
      alumnos[codigoModificar].update(changeAlumno)  
      print('Alumno N°', codigoModificar ,' fue Modificado con exito!!!!!!!!!!')
      print ('CODIGO ', codigoModificar, '-', alumnos[codigoModificar] )   
      print("============================================================")
    except:
      print("=====> ¡¡¡¡¡¡¡ No existe esa opcion, intentalo nuevamente !!!!!!!!!!!!!!!")
    #   listAlumnosCodigo()
      updateAlumno()
      
def listAlumnosCodigo():
    print("============================================================")
    x=0
    print("LISTADO DE ALUNMOS")    
    for a in alumnos:
        print('CODIGO ',x,'-', a)
        x+=1
        
    

while(salir == 'no'):
    print("OPCIONES : 1-registrar alumno 2-mostrar alumnos 3-eliminar alumno 4-actualizar alumno")
    opcion = input()
    if(opcion == "1"):
        print("REGISTRO DE NUEVO ALUMNO:")
        nombre = input("NOMBRE : ")
        email = input("EMAIL : ")
        celular = input("CELULAR : ")
        r = createAlumno(nombre,email,celular)
        if r == 1:
            print("REGISTRO EXITOSO")
    elif(opcion == "2"):
        readAlumno()
    elif(opcion == '3'):
        if (len(alumnos)>0):
           listAlumnosCodigo()      
           deleteAlumno()
        else:
            print("============================================================")
            print("=====> ¡¡¡¡¡¡¡ Lista de alumnos se encuentra vacia, intentalo nuevamente !!!!!!!!!!!!!!!")            
    elif(opcion == '4'):
        if (len(alumnos)>0):
           listAlumnosCodigo()      
           updateAlumno()
        else:
            print("============================================================")
            print("=====> ¡¡¡¡¡¡¡ Lista de alumnos se encuentra vacia, intentalo nuevamente !!!!!!!!!!!!!!!")            
    else:
        print("MARCO UNA OPCIÓN INCORRECTA")
        continue
    print("Desea salir del programa? ")
    salir = input()
#MOSTRAR RESULTADOS
