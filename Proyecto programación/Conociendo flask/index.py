#aprendiendo a usar flask para mi proyecto
from flask import Flask, render_template

app = Flask(__name__)

"""
@app.route('/') #definiendo la ruta
def principal():
    return "esta es mi primera prueba con python flask para usar html" #enviar un resultado/respuesta desde la ruta que se coloco

@app.route('/contacto') #definiendo otra ruta
def contacto():
    return "esta es la pagina de contacto" #al colocaar en la pagina /contacto esta enviara a esta ruta
"""
@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/lenguajes')
def lenguajes():
    return render_template('lenguajes.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True) #debug=True para que se reinicie el servidor cada vez que se haga un cambio en el codigo
