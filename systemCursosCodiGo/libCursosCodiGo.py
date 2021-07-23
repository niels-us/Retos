class clsCurso:
    
    def __init__(self,nomb,nota,codi):
        self.nombre = nomb
        self.nota = nota
        self.codigo = codi
        
    def enviarEjercicio(self):
        pass
    
    
def updateCurso(cursos):
    print(" ACTUALIZAR curso ")
    posCurso = -1
    cursoBusqueda = input("INGRESE EL NOMBRE DEL curso :")
    for i in range(len(cursos)):
        a = cursos[i].nombre  
        if a.upper() == cursoBusqueda.upper():
            print(a)
            posCurso = i
            print("posición del curso:" + str(posCurso))
            break
    print("ACTUALIZANDO DATOS DEL curso:")
    nombre = input("NOMBRE : ")
    nota = input("NOTA : ")
    codigo = input("CODIGO : ")   
    ncurso = clsCurso(nombre,nota,codigo)
    print('ACTUALIZANDO curso')      
    # cursos[posCurso].update(ncurso)        
    del cursos[posCurso]   
    cursos.insert(posCurso,ncurso)
    
def deleteCurso(cursos):
    print(" ELIMINAR Curso ")
    posCurso = -1
    CursoBusqueda = input("INGRESE EL NOMBRE DEL CURSO :")
    for i in range(len(cursos)):
        a = cursos[i].nombre  
        if a.upper() == CursoBusqueda.upper():
            print(a)
            posCurso = i
            print("posición del Curso:" + str(posCurso))
            break      
    del cursos[posCurso]   
    