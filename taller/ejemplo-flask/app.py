from flask import Flask, render_template
import requests
import json
from config import usuario, clave
app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Hello, Worldooooo!</p>"


@app.route("/losedificios")
def los_edificios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/edificios/",
            auth=(usuario, clave))
    edificios = json.loads(r.content)['results']
    numero_edificios = json.loads(r.content)['count']
    return render_template("losedificios.html", edificios=edificios,
    numero_edificios=numero_edificios)


@app.route("/losdepartamentos")
def los_departamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/numerodp/",
            auth=(usuario, clave))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("losdepartamentos.html", datos=datos,
    numero=numero)



# funciones ayuda

def obtener_edificio(url):
    """
    """
    r = requests.get(url, auth=(usuario, clave))
    nombre_edificio = json.loads(r.content)['nombre']
    tipo_edificio = json.loads(r.content)['tipo']
    cadena = "%s %s" %(nombre_edificio, tipo_edificio)
    return cadena
