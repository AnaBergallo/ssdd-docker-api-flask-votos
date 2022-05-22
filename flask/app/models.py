from sqlalchemy import PrimaryKeyConstraint
from .enums import *
from app import db


class Persona(db.Model):
    __tablename__ = "persona"
    __table_args__ = (
        db.UniqueConstraint("id_user"),
    )

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    documento_id = db.Column(db.Integer, db.ForeignKey('documento.id'), unique=True, nullable=False)
    id_user = db.Column(db.Integer, db.ForeignKey('usuario.id'), unique=True)
    fecha_nacimiento = db.Column(db.Date)
    direccion = db.Column(db.String)


class Documento(db.Model):
    __tablename__ = "documento"
    __table_args__ = (
        db.UniqueConstraint("persona_id", "cedula"),
        db.UniqueConstraint("persona_id", "credencial"),
    )

    id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False, unique=True)
    cedula = db.Column(db.Integer, nullable=False)
    credencial = db.Column(db.String, nullable=False)


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
    


class Partido(db.Model):
    __tablename__ = "partido"
    __table_args__ = (
        db.UniqueConstraint("persona_id", "cedula"),
        db.UniqueConstraint("persona_id", "credencial"),
    )

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False, unique=True)
    



class Lista(db.Model):
    __tablename__ = "lista"
    __table_args__ = (

    )
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    partido_id = db.Column(db.Integer, db.ForeignKey('partido.id'), nullable=False)
    eleccion_id = db.Column(db.Integer, db.ForeignKey('eleccion'), nullable=False)



class ListaCandidato(db.Model):
    __tablename__ : "lista_candidato_rel
    __table_args__ = (
        db.UniqueConstraint("lista_id", "candidato_id"),
    )
    id = db.Column(db.Integer, primary_key=True)
    lista_id = db.Column(db.Integer, db.ForeignKey('lista.id'), nullable=False) 
    candidato_id = db.Column(db.Integer, db.ForeignKey('candidato.id'), nullable=False)
    rol = db.Column(db.Enum(Roles), default=Roles.otros, nullable=False)
   


class Eleccion(db.Model):
    __tablename__ = "eleccion"
    __table_args__ = (

    )

    id = db.Column(db.Integer, primary_key=True)
    ano_electoral = db.Column(db.Integer, nullable=False)


