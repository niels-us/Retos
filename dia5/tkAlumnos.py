# from tkinter import Tk
# from _typeshed import Self
from tkinter import *
from tkinter.ttk import Treeview
import sqlite3

class Alumno:    
    
    db_name='database.s3db'
    def ejecutarSql(self,sql,parametros=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor=conn.cursor()
            resultado = cursor.execute(sql,parametros)
            conn.commit()
        return resultado
    
    def readAlumnos(self):
        rsAlumnos = self.trvAlumnos.get_children()
        #limpiando la tabla
        for element in rsAlumnos:
            self.trvAlumnos.delete(element)
            
        sqlAlumnos='SELECT * FROM ALUMNOS ORDER BY NOMBRE DESC'
        resultado=self.ejecutarSql(sqlAlumnos)
        # print(resultado)
        for fila in resultado:
            self.trvAlumnos.insert('',0,text=fila[0],values=(fila[1],fila[2]))
            
    def verificarDatos(self):
        return len(self.nombre.get()) != 0 and len(self.Email.get()) !=0 and len(self.Celular.get()) != 0
            
    def createAlumno(self):
        if self.verificarDatos():
            sqlInsertAlumno='INSERT INTO ALUMNOS VALUES (?,?,?)'
            parametros=(self.nombre.get(),self.Email.get(),self.Celular.get())
            self.ejecutarSql(sqlInsertAlumno,parametros)
            self.readAlumnos()
            self.mensaje['text'] = 'Alumno {} Agregado con Exito'.format(self.nombre.get())
            self.nombre.delete(0,END)
            self.Email.delete(0,END)            
            self.Celular.delete(0,END)
        else:
            self.mensaje['text'] = 'Falta Completar {} Campos'.format(self.nombre.get())
            # print('completar datos')
            
    def deleteAlumno(self):
        self.mensaje['text']=''
        nombre=self.trvAlumnos.item(self.trvAlumnos.selection())['text']
        sqlDeleteAlumno='DELETE FROM ALUMNOS WHERE NOMBRE=?'
        self.ejecutarSql(sqlDeleteAlumno,(nombre,))
        self.mensaje['text']='Alumno {} Eliminado con Exito'.format(nombre)
        self.readAlumnos()         
    
    def updateAlumno(self):        
        self.mensaje['text']=''
        nombre=self.trvAlumnos.item(self.trvAlumnos.selection())['text']
        email=self.trvAlumnos.item(self.trvAlumnos.selection())['values'][0]
        celular=self.trvAlumnos.item(self.trvAlumnos.selection())['values'][1]
        self.edit_wind=Toplevel()       
        self.edit_wind.title = 'Editar Alumno'
        # Antiguo nombre
        Label(self.edit_wind, text = 'Antiguo nombre:').grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = nombre), state = 'readonly').grid(row = 0, column = 2)
        # Nuevo nombre
        Label(self.edit_wind, text = 'Nuevo nombre:').grid(row = 1, column = 1)
        nuevo_nombre = Entry(self.edit_wind)
        nuevo_nombre.grid(row = 1, column = 2)

        # antiguo email
        Label(self.edit_wind, text = 'Antiguo email:').grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = email), state = 'readonly').grid(row = 2, column = 2)
        # Nuevo email
        Label(self.edit_wind, text = 'Nuevo email:').grid(row = 3, column = 1)
        nuevo_email= Entry(self.edit_wind)
        nuevo_email.grid(row = 3, column = 2)        
        
        # antiguo celular
        Label(self.edit_wind, text = 'Antiguo celular:').grid(row = 4, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = celular), state = 'readonly').grid(row = 4, column = 2)
        # Nuevo celular
        Label(self.edit_wind, text = 'Nuevo celular:').grid(row = 5, column = 1)
        nuevo_celular= Entry(self.edit_wind)
        nuevo_celular.grid(row = 5, column = 2)

        Button(self.edit_wind, text = 'Actualizar', command = lambda:self.edit_records(nuevo_nombre.get(), nombre, nuevo_email.get(), email, nuevo_celular.get(), celular)).grid(row = 6, column = 2, sticky = W)
        self.edit_wind.mainloop()
        
    def edit_records(self, nuevo_nombre, nombre, nuevo_email, antiguo_email, nuevo_celular, antiguo_celular):
        query = 'UPDATE alumnos SET nombre = ?, email = ?, celular=? WHERE nombre = ? AND email = ? AND celular = ?'
        parameters = (nuevo_nombre, nuevo_email, nuevo_celular, nombre, antiguo_email,antiguo_celular)
        self.ejecutarSql(query, parameters)
        self.edit_wind.destroy()
        self.mensaje['text'] = 'Record {} updated successfylly'.format(nombre)
        self.readAlumnos()
        
        
        
        # pass
        
        
    
    def __init__(self,window):
        self.wind=window
        self.wind.title('Alumnos')
        
        # CREAMOS UN FRAME
        frame=LabelFrame(self.wind,text="Resgistro de Nuevo Alumno")
        frame.grid(row=0,column=0,columnspan=3,pady=10)
        
        #CAMPOS DEL FORMULARIO NOMBRE
        lbNombre=Label(frame,text='Nombre : ')#CREAMOS LABEL PARA EL NOMBRE DEL ALUMNO
        lbNombre.grid(row=1,column=0)#LO UBICAMOS EN LA PANTALLA
        self.nombre=Entry(frame)#CREAMOS TEXTFIELD PARA CAJA DE TEXTO DEL ALUMNO Y LO ASIGNAMOS AL ATRIBUTO NOMBRE DEL ALUMNO
        self.nombre.grid(row=1,column=1)#Y LO UBICAMOS EN LA PANTALLA
        
        #CAMPOS DEL FORMULARIO EMAIL
        lbEmail=Label(frame,text='Email : ')#CREAMOS LABEL PARA EL NOMBRE DEL ALUMNO
        lbEmail.grid(row=2,column=0)#LO UBICAMOS EN LA PANTALLA
        self.Email=Entry(frame)#CREAMOS TEXTFIELD PARA CAJA DE TEXTO DEL ALUMNO Y LO ASIGNAMOS AL ATRIBUTO NOMBRE DEL ALUMNO
        self.Email.grid(row=2,column=1)#Y LO UBICAMOS EN LA PANTALLA
        
        #CAMPOS DEL FORMULARIO CELULAR
        lbCelular=Label(frame,text='Celular : ')#CREAMOS LABEL PARA EL NOMBRE DEL ALUMNO
        lbCelular.grid(row=3,column=0)#LO UBICAMOS EN LA PANTALLA
        self.Celular=Entry(frame)#CREAMOS TEXTFIELD PARA CAJA DE TEXTO DEL ALUMNO Y LO ASIGNAMOS AL ATRIBUTO NOMBRE DEL ALUMNO
        self.Celular.grid(row=3,column=1)#Y LO UBICAMOS EN LA PANTALLA

        #BOTON PARA CREAR NUEVO ALUMNO
        btnNuevoAlumno=Button(frame,text='Registrar Alumno',command=self.createAlumno)
        btnNuevoAlumno.grid(row=4,columnspan=2,sticky=W+E)#STICKY HACE QUE LE BOTON TOME TODO EL ANCHO

        #BOTON PARA ELIMINAR ALUMNO
        btnNuevoAlumno=Button(frame,text='Eliminar Alumno',command=self.deleteAlumno)
        btnNuevoAlumno.grid(row=6,column=0,sticky=W+E)#STICKY HACE QUE LE BOTON TOME TODO EL ANCHO

        #BOTON PARA EDITAR ALUMNO
        btnNuevoAlumno=Button(frame,text='Actualizar Alumno',command=self.updateAlumno)
        btnNuevoAlumno.grid(row=6,column=1,sticky=W+E)#STICKY HACE QUE LE BOTON TOME TODO EL ANCHO
        
        #MOSTRAR MENSAJE DE ALERTA
        self.mensaje=Label(text='',fg='red')
        self.mensaje.grid(row=3,column=0,columnspan=2,sticky=W+E)
        
        self.trvAlumnos=Treeview(height=10,columns=('#0','#01'))
        self.trvAlumnos.grid(row=3,column=0,columnspan=2)
        self.trvAlumnos.heading('#0',text='Nombre',anchor=CENTER)
        self.trvAlumnos.heading('#1',text='Email',anchor=CENTER)
        self.trvAlumnos.heading('#2',text='Celular',anchor=CENTER)
        
        self.readAlumnos()
        
        
        
        
        
        
        
        

window = Tk()
app=Alumno(window)
window.mainloop()