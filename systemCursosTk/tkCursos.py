from tkinter import *
from tkinter.ttk import Treeview
import sqlite3

class Curso:    
    
    db_name='database.s3db'
    def ejecutarSql(self,sql,parametros=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor=conn.cursor()
            resultado = cursor.execute(sql,parametros)
            conn.commit()
        return resultado
    
    def readCursos(self):
        rsCursos = self.trvCursos.get_children()
        #limpiando la tabla
        for element in rsCursos:
            self.trvCursos.delete(element)
            
        sqlCursos='SELECT * FROM CURSOS ORDER BY NOMBRE DESC'
        resultado=self.ejecutarSql(sqlCursos)
        # print(resultado)
        for fila in resultado:
            self.trvCursos.insert('',0,text=fila[0],values=(fila[1],fila[2]))
            
    def verificarDatos(self):
        return len(self.nombre.get()) != 0 and len(self.nota.get()) !=0 and len(self.codigo.get()) != 0
            
    def createCurso(self):
        if self.verificarDatos():
            sqlInsertCurso='INSERT INTO CURSOS VALUES (?,?,?)'
            parametros=(self.nombre.get(),self.nota.get(),self.codigo.get())
            self.ejecutarSql(sqlInsertCurso,parametros)
            self.readCursos()
            self.mensaje['text'] = 'Curso {} Agregado con Exito'.format(self.nombre.get())
            self.nombre.delete(0,END)
            self.nota.delete(0,END)            
            self.codigo.delete(0,END)
        else:
            self.mensaje['text'] = 'Falta Completar {} Campos'.format(self.nombre.get())
            # print('completar datos')
            
    def deleteCurso(self):
        self.mensaje['text']=''
        nombre=self.trvCursos.item(self.trvCursos.selection())['text']
        sqlDeleteCurso='DELETE FROM CURSOS WHERE NOMBRE=?'
        self.ejecutarSql(sqlDeleteCurso,(nombre,))
        self.mensaje['text']='Curso {} Eliminado con Exito'.format(nombre)
        self.readCursos()         
    
    def updateCurso(self):        
        self.mensaje['text']=''
        nombre=self.trvCursos.item(self.trvCursos.selection())['text']
        nota=self.trvCursos.item(self.trvCursos.selection())['values'][0]
        codigo=self.trvCursos.item(self.trvCursos.selection())['values'][1]
        self.edit_wind=Toplevel()       
        self.edit_wind.title = 'Editar Curso'
        # Antiguo nombre
        Label(self.edit_wind, text = 'Antiguo nombre:').grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = nombre), state = 'readonly').grid(row = 0, column = 2)
        # Nuevo nombre
        Label(self.edit_wind, text = 'Nuevo nombre:').grid(row = 1, column = 1)
        nuevo_nombre = Entry(self.edit_wind)
        nuevo_nombre.grid(row = 1, column = 2)

        # antiguo nota
        Label(self.edit_wind, text = 'Antiguo nota:').grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = nota), state = 'readonly').grid(row = 2, column = 2)
        # Nuevo nota
        Label(self.edit_wind, text = 'Nuevo nota:').grid(row = 3, column = 1)
        nuevo_nota= Entry(self.edit_wind)
        nuevo_nota.grid(row = 3, column = 2)        
        
        # antiguo codigo
        Label(self.edit_wind, text = 'Antiguo codigo:').grid(row = 4, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = codigo), state = 'readonly').grid(row = 4, column = 2)
        # Nuevo codigo
        Label(self.edit_wind, text = 'Nuevo codigo:').grid(row = 5, column = 1)
        nuevo_codigo= Entry(self.edit_wind)
        nuevo_codigo.grid(row = 5, column = 2)

        Button(self.edit_wind, text = 'Actualizar', command = lambda:self.edit_records(nuevo_nombre.get(), nombre, nuevo_nota.get(), nota, nuevo_codigo.get(), codigo)).grid(row = 6, column = 2, sticky = W)
        self.edit_wind.mainloop()
        
    def edit_records(self, nuevo_nombre, nombre, nuevo_nota, antiguo_nota, nuevo_codigo, antiguo_codigo):
        query = 'UPDATE CURSOS SET nombre = ?, nota = ?, codigo=? WHERE nombre = ? AND nota = ? AND codigo = ?'
        parameters = (nuevo_nombre, nuevo_nota, nuevo_codigo, nombre, antiguo_nota,antiguo_codigo)
        self.ejecutarSql(query, parameters)
        self.edit_wind.destroy()
        self.mensaje['text'] = 'Record {} updated successfylly'.format(nombre)
        self.readCursos()
    
    def __init__(self,window):
        self.wind=window
        self.wind.title('Cursos')
        
        # CREAMOS UN FRAME
        frame=LabelFrame(self.wind,text="Resgistro de Nuevo Curso")
        frame.grid(row=0,column=0,columnspan=3,pady=10)
        
        #CAMPOS DEL FORMULARIO NOMBRE
        lbNombre=Label(frame,text='Nombre : ')#CREAMOS LABEL PARA EL NOMBRE DEL Curso
        lbNombre.grid(row=1,column=0)#LO UBICAMOS EN LA PANTALLA
        self.nombre=Entry(frame)#CREAMOS TEXTFIELD PARA CAJA DE TEXTO DEL Curso Y LO ASIGNAMOS AL ATRIBUTO NOMBRE DEL Curso
        self.nombre.grid(row=1,column=1)#Y LO UBICAMOS EN LA PANTALLA
        
        #CAMPOS DEL FORMULARIO nota
        lbnota=Label(frame,text='nota : ')#CREAMOS LABEL PARA EL NOMBRE DEL Curso
        lbnota.grid(row=2,column=0)#LO UBICAMOS EN LA PANTALLA
        self.nota=Entry(frame)#CREAMOS TEXTFIELD PARA CAJA DE TEXTO DEL Curso Y LO ASIGNAMOS AL ATRIBUTO NOMBRE DEL Curso
        self.nota.grid(row=2,column=1)#Y LO UBICAMOS EN LA PANTALLA
        
        #CAMPOS DEL FORMULARIO codigo
        lbcodigo=Label(frame,text='codigo : ')#CREAMOS LABEL PARA EL NOMBRE DEL Curso
        lbcodigo.grid(row=3,column=0)#LO UBICAMOS EN LA PANTALLA
        self.codigo=Entry(frame)#CREAMOS TEXTFIELD PARA CAJA DE TEXTO DEL Curso Y LO ASIGNAMOS AL ATRIBUTO NOMBRE DEL Curso
        self.codigo.grid(row=3,column=1)#Y LO UBICAMOS EN LA PANTALLA

        #BOTON PARA CREAR NUEVO Curso
        btnNuevoCurso=Button(frame,text='Registrar Curso',command=self.createCurso)
        btnNuevoCurso.grid(row=4,columnspan=2,sticky=W+E)#STICKY HACE QUE LE BOTON TOME TODO EL ANCHO

        #BOTON PARA ELIMINAR Curso
        btnNuevoCurso=Button(frame,text='Eliminar Curso',command=self.deleteCurso)
        btnNuevoCurso.grid(row=6,column=0,sticky=W+E)#STICKY HACE QUE LE BOTON TOME TODO EL ANCHO

        #BOTON PARA EDITAR Curso
        btnNuevoCurso=Button(frame,text='Actualizar Curso',command=self.updateCurso)
        btnNuevoCurso.grid(row=6,column=1,sticky=W+E)#STICKY HACE QUE LE BOTON TOME TODO EL ANCHO
        
        #MOSTRAR MENSAJE DE ALERTA
        self.mensaje=Label(text='',fg='red')
        self.mensaje.grid(row=7,column=0,columnspan=2,sticky=W+E)
        
        self.trvCursos=Treeview(height=10,columns=('#0','#01'))
        self.trvCursos.grid(row=3,column=0,columnspan=2)
        self.trvCursos.heading('#0',text='Nombre',anchor=CENTER)
        self.trvCursos.heading('#1',text='nota',anchor=CENTER)
        self.trvCursos.heading('#2',text='codigo',anchor=CENTER)
        
        self.readCursos()      
        
window = Tk()
app=Curso(window)
window.mainloop()