from flask import Flask, render_template, request, g, url_for, redirect
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if(request.method == 'POST'):
        if(request.form['tipo'] == 'dados'):
            return render_template('index.html', active=1, results=1)
        elif(request.form['tipo'] == 'avancado'):
            return render_template('index.html', active=2, results=1)
        else:
            return redirect(url_for('index'))
    else:
        return render_template('index.html', active=1, results=0)


@app.before_request
def before_request():
    g.municipios = pd.read_csv('static/municipios.csv')['municipio']


if(__name__ == '__main__'):
    app.run()
