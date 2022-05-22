from flask_restful import Resource
from . import app, api
from .models import Lista, Persona as persona_model


class Partidos(Resource):
    def get(self):
        return "get Partidos"


class Candidatos(Resource):
    def get(self):
        return "get Candidatos"


class Listas(Resource):
    def get(self):
        return "holi"



class Lista(Resource):
    def get(self, lista_id:int):
        lista = Lista.query.filter_by(id=lista_id).first_or_404()
        lista = {
          'nombre': lista.nombre,
          'lista_id': lista_id,
        }
        return lista, 200


class Voto(Resource):
    def put(self):
        return "put"

class Persona(Resource):
    def get(self, persona_id: int):
        
        persona = persona_model.query.filter_by(id=persona_id).first_or_404()
        persona = {
          'nombre': persona.nombre,
        }
        return persona, 200


api.add_resource(Listas, '/listas')
api.add_resource(Candidatos, '/candidatos')
api.add_resource(Partidos, '/partidos')
api.add_resource(Voto, '/voto')
api.add_resource(Lista, '/lista/<lista_id>')
api.add_resource(Persona, '/persona/<persona_id>')


