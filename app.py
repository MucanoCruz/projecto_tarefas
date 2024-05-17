from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/tarefas_db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def hello():
    return {"hello": "world"}


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
