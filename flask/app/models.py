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
    persona_id = db.Column(db.Integer, db.ForeignKey(
        'persona.id'), nullable=False, unique=True)
    cedula = db.Column(db.Integer, nullable=False)
    credencial = db.Column(db.String, nullable=False)


class Candidato(db.Model):
    __tablename__ = "candidato"

    id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey(
        'persona.id'), nullable=False, unique=True)
    partido_id = db.Column(db.Integer, db.ForeignKey('partido.id'))
    rol = db.Column(db.Enum(Roles), default=Roles.otros, nullable=False)


class Usuario(db.Model):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey(
        'persona.id'), nullable=False, unique=True)


class Partido(db.Model):
    __tablename__ = "partido"

    id = db.Column(db.Integer, primary_key=True)


# class Lista(db.Model):
#     __tablename__ = "partido"
#     __table_args__ = (

#     )


# class Eleccion(db.Model):
#     __tablename__ = "partido"
#     __table_args__ = (

#     )


# class Padron(db.Model):
#     __tablename__ = "partido"
#     __table_args__ = (

#     )


# class Circuito(db.Model):
#     __tablename__ = "partido"
#     __table_args__ = (

#     )
