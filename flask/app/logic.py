import json
from flask_restful import Resource
from . import app, api
from .models import Lista as lista_model, Persona as presona_model, Partido as partido_model, Candidato as candidato_model



class Partidos(Resource):
    def get(self):
        partidos = partido_model.query.order_by(partido_model.nombre).all()

        partidos_dict = {}
        for partido in partidos: 
          partidos_dict[partido.id] = {'id': partido.id, 'nombre':partido.nombre}

        partidos_json = json.dumps(partidos_dict)
        return partidos_dict, 200
        


class Candidatos(Resource):
   def get(self):
        candidatos = candidato_model.query.order_by(candidato_model.id).all()
        candidatos_dict = {}
        for candidato in candidatos: 
          candidatos_dict[candidato.id] = {'id': candidato.id, 'nombre':candidato.persona_id.nombre}

        candidatos_json = json.dumps(candidatos_dict)
        return candidatos_json, 200
        


class Listas(Resource):
    def get(self):
      listas = lista_model.query.order_by(lista_model.nombre).all()
      listas_dict = {}
      for lista in listas: 
        listas_dict[lista.id] = {'nombre':lista.nombre, 'candidatos': lista.candidatos_objs}

      listas_json = json.dumps(listas_dict)
      return listas_json, 200



class Lista(Resource):
    def get(self, lista_id:int):
        lista = lista_model.query.filter_by(id=lista_id).first_or_404()
        lista = {
          'nombre': lista.nombre,
          'lista_id': lista.lista_id,
        }
        lista_json = json.dumps(lista)
        return lista_json, 200



class Persona(Resource):
    def get(self, persona_id: int):
        persona = presona_model.query.filter_by(id=persona_id).first_or_404()
        persona = {
          'nombre': persona.nombre,
        }
        return persona, 200

class Partido(Resource):
    def get(self, partido_id: int):
        
        partido = partido_model.query.filter_by(id=partido_id).first_or_404()
        partido = {
          'nombre': partido.nombre,
        }
        return partido, 200


api.add_resource(Listas, '/listas')
api.add_resource(Candidatos, '/candidatos')
api.add_resource(Partidos, '/partidos')
api.add_resource(Lista, '/lista/<lista_id>')
api.add_resource(Persona, '/persona/<persona_id>')
api.add_resource(Partido, '/partido/<partido_id>')


