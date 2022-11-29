from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return 'Index'

@app.route("/info")
def info():
    argumentos = request.args
    if argumentos != {}:
        return argumentos
    return 'No hay argumentos'


@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/parametros")
def parametros():
    lista_nombres = ['Juan', 'Pedro', 'Ana', 'Maria']
    return render_template('parametros.html', nombres=lista_nombres)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
