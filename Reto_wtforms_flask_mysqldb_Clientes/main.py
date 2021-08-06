from flask import Flask,render_template,request,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,HiddenField,SelectField
from wtforms.validators import DataRequired

#CREAMOS OBJETO DE CLASE FLASK PARA INICIAR LA APLICACIÓN
app = Flask(__name__)

#Configuracion de BASE DE DATOS
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pk_dia5'

#AGREGAR CONEXIÓN A BASE DE DATOS DE NUESTRA APP
mysql = MySQL(app)

#VALOR SECRETO PARA FORMULARIOS
app.secret_key = "mysecretkey"

#AÑADIMOS BOOTSTRAP A NUESTRO APP
Bootstrap(app)


############################# FORMULARIOS ################################
class frmProducto(FlaskForm):
    id = HiddenField("hdnId")
    categoria = StringField('Categoria :',validators=[DataRequired()])
    nombre = StringField('Nombre :',validators=[DataRequired()])
    marca = StringField('Marca :',validators=[DataRequired()])
    modelo = StringField('Modelo :',validators=[DataRequired()])
    serie = StringField('Nro Serie :',validators=[DataRequired()])
    ram = StringField('Memoria RAM :',validators=[DataRequired()])
    procesador = StringField('Procesador :',validators=[DataRequired()])
    discoduro = StringField('Disco Duro :',validators=[DataRequired()])
    precio = StringField('Precio :',validators=[DataRequired()])
    stock = StringField('Stock :',validators=[DataRequired()])
    submit = SubmitField('Guardar')

class frmCliente(FlaskForm):
    
    id = HiddenField("hdnId")    
    categoria = SelectField("Categoria :", coerce=str,validators=[DataRequired()])
    # module_list=[('1','DNI'),('2','RUC'),('3','CARNET EXTRANJERIA')]
    # categoria = SelectField('Categoria', choices=module_list,validators=[DataRequired()])
    # categoria = StringField('Categoria :',validators=[DataRequired()])
    nombre = StringField('Nombre :',validators=[DataRequired()])
    telefono = StringField('Telefono :',validators=[DataRequired()])
    email = StringField('Email :',validators=[DataRequired()])
    nro_doc = StringField('Nro Documento :',validators=[DataRequired()])    
    submit = SubmitField('Guardar')


################################# RUTAS ###################################
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT c.id,t.nombre AS tipo,c.nro_doc AS nro,c.nombre AS cliente,c.telefono,c.email FROM clientes c JOIN tipo_doc_ide t ON c.tipo_doc_ide_id = t.id ')
    data = cur.fetchall()
    cur.close()

    print(data)
    context = {
        'data':data
    }
    return render_template('index.html',**context)


@app.route('/productos',methods=['GET','POST'])
def productos():
    print("productos:::::")
    #CURSOR CATEGORIAS
    curCategoria = mysql.connection.cursor()
    curCategoria.execute('SELECT * from cat_producto')
    dataCategoria = curCategoria.fetchall()
    curCategoria.close()
    
    catId = 0
    
    if request.method == 'POST' and int(request.form['categoria']) > 0 :
        catId = request.form['categoria']
        sqlProducto = "SELECT * FROM PRODUCTO where cat_producto_id=" + catId
    else:
        sqlProducto = "SELECT * FROM PRODUCTO"
    
    #CURSOR PRODUCTOS
    curProducto = mysql.connection.cursor()
    curProducto.execute(sqlProducto)
    dataProducto = curProducto.fetchall()
    curProducto.close()

    
    frmNuevoProducto = frmProducto()
    
    
    pId = request.args.get('pid','0')
    
    print("ID DEL PRODUCTO SELECCIONADO = " + pId)
    #CARGAMOS EL PRODUCTO A EDITAR
    if pId != '0' and request.method == 'GET':
        curProductoEditar = mysql.connection.cursor()
        curProductoEditar.execute("select * from producto where id=%s",(pId))
        dataProductoEditar = curProductoEditar.fetchone()
        curProductoEditar.close()
        print("DATOS DEL PRODUCTO A EDITAR :")
        print(dataProductoEditar)
        #llenamos los valores del producto a editar en el formulario
        frmNuevoProducto.id.data = dataProductoEditar[0]
        frmNuevoProducto.categoria.data = dataProductoEditar[1]
        frmNuevoProducto.nombre.data = dataProductoEditar[2]
        frmNuevoProducto.marca.data = dataProductoEditar[3]
        frmNuevoProducto.modelo.data = dataProductoEditar[4] 
        frmNuevoProducto.serie.data = dataProductoEditar[5]
        frmNuevoProducto.ram.data = dataProductoEditar[6]
        frmNuevoProducto.procesador.data = dataProductoEditar[7]
        frmNuevoProducto.discoduro.data = dataProductoEditar[8]
        frmNuevoProducto.precio.data = dataProductoEditar[9]
        frmNuevoProducto.stock.data = dataProductoEditar[10]
    
    context = {
        'dataCategoria':dataCategoria,
        'dataProducto':dataProducto,
        'catId':catId,
        'frmProducto':frmNuevoProducto
    }
    
    if frmNuevoProducto.validate_on_submit():
        
        id = frmNuevoProducto.id.data
        categoriaId = frmNuevoProducto.categoria.data
        nombre = frmNuevoProducto.nombre.data
        marca = frmNuevoProducto.marca.data
        modelo = frmNuevoProducto.modelo.data
        serie = frmNuevoProducto.serie.data
        ram = frmNuevoProducto.ram.data
        procesador = frmNuevoProducto.procesador.data
        discoduro = frmNuevoProducto.discoduro.data
        precio = frmNuevoProducto.precio.data
        stock = frmNuevoProducto.stock.data
        
        print("producto a editar:" + id)
        
        if id != '':
            #actualizar producto
            print("actualizamos")
            curUpdateProducto = mysql.connection.cursor()
            
            sqlActualizarProducto = "UPDATE producto "
            sqlActualizarProducto +="SET cat_producto_id='" + categoriaId + "'" 
            sqlActualizarProducto +=",nombre='" + nombre + "'"
            sqlActualizarProducto +=",marca='" + marca + "'"
            sqlActualizarProducto +=",modelo='" + modelo + "'"
            sqlActualizarProducto +=",nro_serie='" + serie + "'"
            sqlActualizarProducto +=",mem_ram='" + ram + "'"
            sqlActualizarProducto +=",procesador='" + procesador + "'"
            sqlActualizarProducto +=",disco_duro='" + discoduro + "'"
            sqlActualizarProducto +=",precio='" + precio + "'"
            sqlActualizarProducto +=",stock='" + stock + "'"
            sqlActualizarProducto +=" where id=" + id + ""
            
            print("SQL UPDATE:" + sqlActualizarProducto)
            
            #curUpdateProducto.execute(sqlActualizarProducto)
            curUpdateProducto.execute("UPDATE producto SET cat_producto_id=%s,nombre=%s,marca=%s,modelo=%s,nro_serie=%s,mem_ram=%s,procesador=%s,disco_duro=%s,precio=%s,stock=%s WHERE id=%s",(categoriaId,nombre,marca,modelo,serie,ram,procesador,discoduro,precio,stock,id))
            mysql.connection.commit()
        else:
            #registrar producto
            print("registramos")
            curNuevoProducto = mysql.connection.cursor()
            curNuevoProducto.execute("INSERT INTO producto(cat_producto_id,nombre,marca,modelo,nro_serie,mem_ram,procesador,disco_duro,precio,stock) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(categoriaId,nombre,marca,modelo,serie,ram,procesador,discoduro,precio,stock))
            mysql.connection.commit()
        
        return redirect(url_for('productos'))      
    
    
    return render_template('productos.html',**context)

#RUTA PARA ELIMINAR PRODUCTOS
@app.route("/eliminarProducto",methods=['POST'])
def eliminarProducto():
    id = request.form['eid']
    print("ID A ELIMINAR : " + id)
    
    curEliminarProducto = mysql.connection.cursor()
    curEliminarProducto.execute("DELETE FROM producto WHERE id=%s",(id))
    mysql.connection.commit()

    return redirect(url_for('productos'))

@app.route('/clientes',methods=['GET','POST'])
def clientes():
    print("Clientes:::::")
    #CURSOR CATEGORIAS
    curCategoria = mysql.connection.cursor()
    curCategoria.execute('SELECT * from tipo_doc_ide')
    dataCategoria = curCategoria.fetchall()
    curCategoria.close()
    
    catId = 0

    if request.method == 'POST' and int(request.form['categoria']) > 0 :
        catId = request.form['categoria']
        sqlClientes = "SELECT * FROM Clientes where tipo_doc_ide_id=" + catId
    else:
        sqlClientes = "SELECT * FROM Clientes"
    
    #CURSOR ClientesS
    curClientes = mysql.connection.cursor()
    curClientes.execute(sqlClientes)
    dataClientes = curClientes.fetchall()
    curClientes.close()
    
    # frmNuevoCliente = frmCliente()     
    
    frmNuevoCliente=frmCliente()
    frmNuevoCliente.categoria.choices = dataCategoria #carga las categorias en el formulario 
    # frmNuevoCliente.categoria.choices = [('1','DNI'),('2','RUC'),('3','CARNET EXTRANJERIA')]
    # frmNuevoCliente.process()

    pId = request.args.get('pid','0')

    print("ID DEL Clientes SELECCIONADO = " + pId)
    #CARGAMOS EL Cliente A EDITAR
    if pId != '0' and request.method == 'GET':
        curClienteEditar = mysql.connection.cursor()
        curClienteEditar.execute("select * from Clientes where id={0}".format(pId))
        # curClienteEditar.execute("select * from Clientes where id=%s",(pId))
        
        dataClienteEditar = curClienteEditar.fetchone()
        curClienteEditar.close()
        print("DATOS DEL Cliente A EDITAR :")
        print(dataClienteEditar)
        #llenamos los valores del Cliente a editar en el formulario
        frmNuevoCliente.id.data = dataClienteEditar[0]        
        frmNuevoCliente.categoria.process_data(dataClienteEditar[1])#Carga categoria seleccionada
        frmNuevoCliente.nro_doc.data = dataClienteEditar[2]
        frmNuevoCliente.nombre.data = dataClienteEditar[3]
        frmNuevoCliente.telefono.data = dataClienteEditar[4]
        frmNuevoCliente.email.data = dataClienteEditar[5] 

    context = {
        'dataCategoria':dataCategoria,
        'dataCliente':dataClientes,
        'catId':catId,
        'frmClientes':frmNuevoCliente
    }


    if frmNuevoCliente.validate_on_submit():
        id = frmNuevoCliente.id.data
        categoriaId = frmNuevoCliente.categoria.data
        nombre = frmNuevoCliente.nombre.data
        telefono = frmNuevoCliente.telefono.data
        email = frmNuevoCliente.email.data
        nro_doc = frmNuevoCliente.nro_doc.data
             
        print("Cliente a editar::::::::::::::::" + id)

        if id != '':
            #actualizar producto
            print("actualizamos")
            curUpdateCliente = mysql.connection.cursor()
            
            sqlActualizarCliente = "UPDATE Clientes "
            sqlActualizarCliente +="SET tipo_doc_ide_id='" + categoriaId + "'" 
            sqlActualizarCliente +=",nombre='" + nombre + "'"
            sqlActualizarCliente +=",telefono='" + telefono + "'"
            sqlActualizarCliente +=",email='" + email + "'"
            sqlActualizarCliente +=",nro_doc='" + nro_doc + "'"
            sqlActualizarCliente +=" where id=" + id + ""
            
            
            print("SQL UPDATE:" + sqlActualizarCliente)
            
            curUpdateCliente.execute(sqlActualizarCliente)
            curUpdateCliente.execute("UPDATE Clientes SET tipo_doc_ide_id=%s,nombre=%s,telefono=%s,email=%s,nro_doc=%s WHERE id=%s",(categoriaId,nombre,telefono,email,nro_doc,id))
            mysql.connection.commit()
        else:
            #registrar Cliente
            print("registramos")
            curNuevoCliente = mysql.connection.cursor()
            curNuevoCliente.execute("INSERT INTO Clientes (tipo_doc_ide_id,nombre,telefono,email,nro_doc) values (%s,%s,%s,%s,%s)",(categoriaId,nombre,telefono,email,nro_doc))
            mysql.connection.commit()
        
        return redirect(url_for('clientes'))

    return render_template('clientes.html',**context)

#RUTA PARA ELIMINAR ClienteS
@app.route("/eliminarCliente",methods=['POST'])
def eliminarCliente():
    id = request.form['eid']
    print("ID A ELIMINAR : ", id)
    
    curEliminarCliente = mysql.connection.cursor()
    curEliminarCliente.execute("DELETE FROM Clientes WHERE id={0}".format(id))
    mysql.connection.commit()

    return redirect(url_for('clientes'))

#METODO PRINCIPAL
if __name__ == '__main__':
    app.run(debug=True,port=5001)

