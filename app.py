from flask import Flask, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Blueprint, render_template


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/tarefas_db"
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tarefa')
def tarefa():
    return render_template('tarefa.html')


@app.route('/tarefa', methods=['POST'])
def tarefa_post():
    titulo = request.form.get('titulo')
    descricao = request.form.get('descricao')
    tarefa = TarefaModel(titulo, descricao, 1, 1)
    db.session.add(tarefa)
    db.session.commit()
    return {"message": f"tarefa {tarefa.titulo} criada com sucesso."}
    # return render_template('tarefa.html')

##################### PARTILHAR TAREFA #################### 
@app.route('/partilhar_tarefa')
def tarefa():
    return render_template('partilhar_tarefa.html')


@app.route('/partilhar_tarefa', methods=['POST'])
def tarefa_post():
    titulo = request.form.get('titulo')
    descricao = request.form.get('descricao')
    tarefa = TarefaModel(titulo, descricao, 1, 1)
    db.session.add(tarefa)
    db.session.commit()
    return {"message": f"tarefa {tarefa.titulo} criada com sucesso."}
    # return render_template('tarefa.html')

@app.route('/profile')
def profile():
    return 'Profile'

#################### LOGIN ################################


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

   # user = User.query.filter_by(email=email).first()
    usuarioModel = UsuarioModel.query.filter_by(
        usuario=usuario, senha=senha).first()

    if not usuarioModel:
        flash('Please check your login details and try again.')
        # return redirect('auth.login')
        return 'Usuário não encontrado'
    else:
        return 'Nome do Usuário: ' + usuarioModel.nome
    # return 'Teste login post'


@app.route('/signup')
def signup():
    return 'Signup'


@app.route('/logout')
def logout():
    return 'Logout'


if __name__ == '__main__':
    app.run(debug=True)


class UsuarioModel(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String())
    usuario = db.Column(db.String())
    senha = db.Column(db.String())

    def __init__(self, nome, usuario, senha):
        self.nome = nome
        self.usuario = usuario
        self.senha = senha

    def __repr__(self):
        return f"<Usuario {self.nome}>"


class EstadoTarefaModel(db.Model):
    __tablename__ = 'estados_tarefa'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String())

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f"<EstadoTarefa {self.nome}>"


class TarefaModel(db.Model):
    __tablename__ = 'tarefas'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String())
    descricao = db.Column(db.String())
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    estado_id = db.Column(db.Integer, db.ForeignKey('estados_tarefa.id'))

    def __init__(self, titulo, descricao, usuario_id, estado_id):
        self.titulo = titulo
        self.descricao = descricao
        self.usuario_id = usuario_id
        self.estado_id = estado_id

    def __repr__(self):
        return f"<Usuario {self.titulo}>"


student_course = db.Table(
    'tarefa_usuario',
    db.Column('tarefa_id', db.Integer, db.ForeignKey('tarefas.id')),
    db.Column('usuario_id', db.Integer, db.ForeignKey('usuarios.id'))
)

