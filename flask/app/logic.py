from flask_restful import Resource
from app import api, app


class Partidos(Resource):
    def get(self):
        return "get Partidos"


class Candidatos(Resource):
    def get(self):
        return "get Candidatos"


class Listas(Resource):
    def get(self):
        return "Select * from usuarios;"


class Lista(Resource):
    def get(self, lista_id):
        result = "Imaginate que me conecto a la base y te devuelvo los datos de la lista $lista_id"
        return result


class Voto(Resource):
    def put(self):
        return "push"


api.add_resource(Listas, '/listas')
api.add_resource(Candidatos, '/candidatos')
api.add_resource(Partidos, '/partidos')
api.add_resource(Voto, '/voto')
api.add_resource(Lista, '/lista/<int:lista_id>')
