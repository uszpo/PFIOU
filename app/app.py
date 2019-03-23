from flask import request, Flask, session, render_template
import random
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        alea = random.randint(1, 100)
        session['aleatoire'] = alea
        return render_template("hello.html")
    elif request.method == 'POST':
        valeur_test = request.form['valeur_test']
        return render_template("test.html", valeur_test = int(valeur_test))


app.config['SECRET_KEY'] = "Your_secret_string"


