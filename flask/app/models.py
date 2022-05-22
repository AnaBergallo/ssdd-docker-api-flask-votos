from sqlalchemy import PrimaryKeyConstraint
from .enums import *
from app import db


lista_candidato = db.Table('ListaCandidato',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('lista_id', db.Integer, db.ForeignKey('lista.id')),
    db.Column('candidato_id', db.Integer, db.ForeignKey('candidato.id')),
    db.Column('rol', db.Enum(Roles), default=Roles.otros, nullable=False))


class Persona(db.Model):
    __tablename__ = "persona"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), unique=True)
    cedula_identidad = db.Column(db.Integer, unique=True)
    credencial = db.Column(db.String, unique=True)
    fecha_nacimiento = db.Column(db.Date)
    direccion = db.Column(db.String)



class Usuario(db.Model):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String, nullable=False)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False, unique=True)



class Candidato(db.Model):
    __tablename__ = "candidato"
    __table_args__ = (
        db.UniqueConstraint("persona_id", "partido_id"),
    )

    id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False, unique=True)
    partido_id = db.Column(db.Integer, db.ForeignKey('partido.id'), nullable=False)
    listas_objs = db.relationship('Lista', secondary=lista_candidato, backref='candidato')
    


class Partido(db.Model):
    __tablename__ = "partido"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False, unique=True)
    


class Lista(db.Model):
    __tablename__ = "lista"
   
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False, unique=True)
    partido_id = db.Column(db.Integer, db.ForeignKey('partido.id'), nullable=False)
    eleccion_id = db.Column(db.Integer, db.ForeignKey('eleccion.id'), nullable=False)
    candidatos_objs = db.relationship('Candidato', secondary=lista_candidato, backref='lista')

   

class Eleccion(db.Model):
    __tablename__ = "eleccion"
    __table_args__ = (

    )

    id = db.Column(db.Integer, primary_key=True)
    anio_electoral = db.Column(db.DateTime, nullable=False)


