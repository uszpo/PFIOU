from flask import request, Flask, session
from flask_restful import Resource, Api
from flask import jsonify
import random

app = Flask(__name__)
api = Api(app)


class Test(Resource):
    def get(self, valeur_test):
        if int(valeur_test) == session.get('aleatoire'):
            return True
        else:
            return False


class Home(Resource):
    def get(self):
        alea = random.randint(1, 100)
        session['aleatoire'] = alea
        return str(alea)


app.config['SECRET_KEY'] = "Your_secret_string"
api.add_resource(Home, '/')
api.add_resource(Test, '/Test/<valeur_test>')
