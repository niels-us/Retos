from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+libreriamysql://user:pass:@localhost/bdname
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flaskapi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

#CLASES PARA BD

class Curso(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(100),nullable=False)
    nota = db.Column(db.String(100),unique= True)
    
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        
db.create_all()


class CursosSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','nota')
    
curso_schema = CursosSchema()
cursos_schema = CursosSchema(many=True)

@app.route('/')
def index():
    return jsonify({'mensaje':'Bienvenido a mi API'})

@app.route('/setCurso',methods=['POST'])
def setCurso():
    nombre = request.json['nombre']
    nota = request.json['nota']
    
    #EQUIVALENTE A INSERT INTO Curso
    nuevoCurso = Curso(nombre,nota)
    db.session.add(nuevoCurso)
    db.session.commit()
    
    return curso_schema.jsonify(nuevoCurso)

@app.route('/cursos',methods=['GET'])
def getCursos():
    listadoCursos = Curso.query.all() #SELECT * FROM CursoS
    print(listadoCursos)
    dataCursos = cursos_schema.dump(listadoCursos)
    print(dataCursos)
    return jsonify(dataCursos)

@app.route('/getCurso/<id>',methods=['GET'])
def getCurso(id):
    curso = Curso.query.get(id) #select * from Curso where id=
    print(curso)
    
    return curso_schema.jsonify(curso)

@app.route('/updCurso/<id>',methods=['PUT'])
def updateCurso(id):
    curso = Curso.query.get(id) #select * from Curso where id=
    print(curso)
    
    nombre = request.json['nombre']
    nota = request.json['nota']
    #UPDATE Curso SET 
    curso.nombre = nombre
    curso.nota = nota
    
    db.session.commit()
    
    return curso_schema.jsonify(curso)
    
@app.route('/delCurso/<id>',methods=['DELETE'])
def deleteCurso(id):
    curso = Curso.query.get(id)
    #DELETE FROM CursoS WHERE id=
    db.session.delete(curso)
    db.session.commit()
    
    return curso_schema.jsonify(curso)    

if __name__ == "__main__":
    app.run(debug=True)