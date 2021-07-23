class clsAlumno:
    
    def __init__(self,nom,ema,cel):
        self.nombre = nom
        self.email = ema
        self.celular = cel
        
    def enviarEjercicio(self):
        pass
    
    
def updateAlumno(alumnos):
    print(" ACTUALIZAR ALUMNO ")
    posAlumno = -1
    alumnoBusqueda = input("INGRESE EL NOMBRE DEL ALUMNO :")
    for i in range(len(alumnos)):
        a = alumnos[i].nombre  
        if a.upper() == alumnoBusqueda.upper():
            print(a)
            posAlumno = i
            print("posición del alumno:" + str(posAlumno))
            break                    
    print("ACTUALIZANDO DATOS DEL ALUMNO:")
    nombre = input("NOMBRE : ")
    email = input("EMAIL : ")
    celular = input("CELULAR : ")   
    nAlumno = clsAlumno(nombre,email,celular)
    print('ACTUALIZANDO ALUMNO')      
    # alumnos[posAlumno].update(nAlumno)        
    del alumnos[posAlumno]   
    alumnos.insert(posAlumno,nAlumno)
    
def deleteAlumno(alumnos):
    print(" ELIMINAR ALUMNO ")
    posAlumno = -1
    alumnoBusqueda = input("INGRESE EL NOMBRE DEL ALUMNO :")
    for i in range(len(alumnos)):
        a = alumnos[i].nombre  
        if a.upper() == alumnoBusqueda.upper():
            print(a)
            posAlumno = i
            print("posición del alumno:" + str(posAlumno))
            break      
    del alumnos[posAlumno]   
    