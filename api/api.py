from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

contato = [
    {
        "name": "Mariana",
        "telefone": 987654321
    }, 
    {
        "name": "Paloma",
        "telefone": 912345678
    },
     {
        "name": "Giulia",
        "telefone": 987651234
    }, 
     {
        "name": "Karlos",
        "telefone": 912348765
    }
]

class Users(Resource): 
    def get(self, name):
        for users in contato:
            if(name == users["name"]):
                return users, 200
        return "Usuario nao encontrado", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("telefone")
        args = parser.parse_args()
        
        for users in contato:
            if(name == users["name"]):
                return "Usuario com esse nome "+name+" ja existe", 400
        users = {
            "name": name,
            "telefone": args["telefone"],
        }
        contato.append(users)
        return users, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("telefone")
        args = parser.parse_args()
        
        for users in contato:
            if(name == users["name"]):
                users["telefone"] = args["telefone"]
                return users, 200
        users = {
            "name": name,
            "telefone": args["telefone"],
        }
        contato.append(users)
        return users, 201

    def delete(self, name):
        global contato
        contato = [users for users in contato if users["name"] != name]
        return name+" foi deletado com sucesso.", 200

api.add_resource(Users, "/users/<string:name>")

app.run(port=5000, debug=True)