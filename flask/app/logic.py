import json
import requests
from flask import request, jsonify
from flask_restful import Resource, reqparse
from . import app, api
from .models import Lista as lista_model, Persona as presona_model, Partido as partido_model, Candidato as candidato_model

parser = reqparse.RequestParser()
parser.add_argument("token", type=json)


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
          nombre = ''
          if candidato.persona_id: 
              persona = presona_model.query.filter_by(id=candidato.persona_id).first_or_404()
              nombre = persona.nombre
          candidatos_dict[candidato.id] = {'id': candidato.id, 'nombre':nombre}

        return candidatos_dict, 200
        
class Listas(Resource):
    def get(self):
        listas = lista_model.query.order_by(lista_model.nombre).all()
        listas_dict = {}
        for lista in listas: 
          listas_dict[lista.id] = {'nombre':lista.nombre}

        return  listas_dict, 200

class Personas(Resource):
    def get(self):
        personas = presona_model.query.order_by(presona_model.id).all()
        personas_dict = {}
        for persona in personas: 
            personas_dict[persona.id] = {'nombre': persona.nombre, 'cedula_identidad': persona.cedula_identidad}
         
        return personas_dict, 200


class Lista(Resource):
    def get(self, lista_id):
        lista = lista_model.query.filter_by(id=lista_id).first_or_404()
        if lista: 
            lista = {
              'nombre': lista.nombre,
              'lista_id': lista.id,
            }
            
            return lista, 200
        else: 
            error = json.dumps({"message":"Error"})
            return error, 404

class Persona(Resource):
    def get(self, persona_id: int):
        persona = presona_model.query.filter_by(id=persona_id).first_or_404()
        if persona: 
            persona = {
                'nombre': persona.nombre,
              }
            return persona, 200
        else: 
            error = json.dumps({"message":"Error"})
            return error, 404

class Partido(Resource):
    def get(self, partido_id: int):
        
        partido = partido_model.query.filter_by(id=partido_id).first_or_404()
        partido = {
          'nombre': partido.nombre,
        }
        return partido, 200

class Candidato(Resource):
    def get(self, candidato_id):
        candidato = candidato_model.query.filter_by(id=candidato_id).first_or_404()
        nombreCandidato = ''
        nombrePartido = ''

        if candidato.persona_id: 
            persona = presona_model.query.filter_by(id=candidato.persona_id).first_or_404()
            nombreCandidato = persona.nombre
        if candidato.partido_id: 
            partido = partido_model.query.filter_by(id=candidato.partido_id).first_or_404()
            nombrePartido = partido.nombre
        candidato_dict = {}
        candidato_dict[candidato.id] = {'nombre':nombreCandidato, 'partido': nombrePartido}
        
        return candidato_dict, 200


class Votar(Resource):
    def validateToken(self, token):
          data={"token":token}
          data= json.dumps(data)
          url = "https://accountmanagerucuback.azurewebsites.net/validateToken"
          response = requests.get(url=url,data=data, headers={"Content-Type": "application/json"})
          if response.status_code == 200:
              return True
          return False

    def post(self):
        # content_type = requests.headers.get('Content-Type')
        # if (content_type == 'application/json'):
        
        data =  request.get_json()
        lista_id2 = data["lista_id"]
        token = data["token"]
        valido =  self.validateToken(token)
        if valido:
            voto = {  "list_id": lista_id2,
                      "election_id": "SJDFK324342",
                      "circuit_id": "AHA2019",
                      "user_credential": "jkasjdk"
                    }
            url = "https://us-central1-sufragiapp.cloudfunctions.net/sufragiapp_bc/addVote"

            response = requests.post(url=url,data=voto)
            print("\n\nResponse :",response)
            return response.json(), 200
        else:
            return "Error", 400
      




api.add_resource(Listas, '/listas')
api.add_resource(Candidatos, '/candidatos')
api.add_resource(Partidos, '/partidos')
api.add_resource(Personas, '/personas')

api.add_resource(Lista, '/lista/<lista_id>')
api.add_resource(Persona, '/persona/<persona_id>')
api.add_resource(Partido, '/partido/<partido_id>')
api.add_resource(Candidato, '/candidato/<candidato_id>')

api.add_resource(Votar, '/votar')

api.add_resource(initSession, '/session')



