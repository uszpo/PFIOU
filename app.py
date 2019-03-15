from flask import request, Flask, session, render_template
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

@app.route('/')
def get():
    if request.method == 'GET':
        alea = random.randint(1, 100)
        session['aleatoire'] = alea
        return render_template("hello.html")
    else:
        pass # TODO http://flask.pocoo.org/docs/1.0/quickstart/#rendering-templates


app.config['SECRET_KEY'] = "Your_secret_string"


