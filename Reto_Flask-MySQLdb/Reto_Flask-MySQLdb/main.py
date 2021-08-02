from flask import Flask,render_template,request
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL


app = Flask(__name__)

Bootstrap(app)

#configuracion de base de datos
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_sistemapos'

mysql = MySQL(app)

app.secret_key="mysecretkey"

lstProductos = ['LAPTOP','IMPRESORA HP','SILLA GAMER']

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT c.id,t.nombre AS tipo,c.nro_doc,c.nombre,c.telefono,c.email FROM clientes c JOIN tipo_doc_ide t ON c.tipo_doc_ide_id=t.id')
    data = cur.fetchall()
    cur.close
    
    # print (data)
    
    context = {
        'data':data
    }
    return render_template('index.html',**context)

@app.route('/productos')
def productos():
    cur = mysql.connection.cursor()
    cur.execute('SELECT c.id,c.nombre AS tipo,c.precio,c.stock,t.categoria FROM productos c JOIN categorias t ON c.id_categorias=t.id')
    data = cur.fetchall()
    cur.close
    
    # print (data)
    
    context = {
        'data':data
    }
    
    return render_template('productos.html',**context)

if __name__ == '__main__':
    app.run(debug=True,port=5001)


