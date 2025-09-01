from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('Inicio.html')

@app.route('/Mallas')
def mallas():
    return render_template('Mallas.html', malla=malla)

malla = {
    "1° Semestre": [
        "Cálculo Diferencial",
        "Ingenium for a Better World",
        "Real Maths",
        "Ciudadano global y ético",
        "Química General",
        "Biología General"
    ],
    "2° Semestre": [
        "Calculo integral",
        "Álgebra Lineal",
        "Algoritmos y Programación",
        "Física Mecanica",
        "El poder de las probabilidades",
        "Ser emprendedor-actor de cambio"
    ],
    "3° Semestre": [
        "xs",
        "O",
        "Ngía I",
        "Fis",
        "Inm",
        "n",
        "Inglés II"
    ],
    "4° Semestre": [
        "Calculo integral",
        "Álgebra Lineal",
        "Algoritmos y Programación",
        "Física Mecanica",
        "El poder de las probabilidades",
        "Ser emprendedor-actor de cambio"
    ],
    "5° Semestre": [
        "Calculo integral",
        "Álgebra Lineal",
        "Algoritmos y Programación",
        "Física Mecanica",
        "El poder de las probabilidades",
        "Ser emprendedor-actor de cambio"
    ],
    "6° Semestre": [
        "Calculo integral",
        "Álgebra Lineal",
        "Algoritmos y Programación",
        "Física Mecanica",
        "El poder de las probabilidades",
        "Ser emprendedor-actor de cambio"
    ],
    "7° Semestre": [
        "Calculo integral",
        "Álgebra Lineal",
        "Algoritmos y Programación",
        "Física Mecanica",
        "El poder de las probabilidades",
        "Ser emprendedor-actor de cambio"
    ],
    "8° Semestre": [
        "Calculo integral",
        "Álgebra Lineal",
        "Algoritmos y Programación",
        "Física Mecanica",
        "El poder de las probabilidades",
        "Ser emprendedor-actor de cambio"
    ]
}

if __name__ == '__main__':
    app.run(debug=True)
