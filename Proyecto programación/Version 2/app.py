from flask import Flask, render_template

app = Flask(__name__)

malla_mecatronica = {
    "Semestre 1": ["Cálculo Diferencial", "Álgebra Lineal", "Algoritmos y Programación", "Ingenium for a Better World", "Real Maths", "Ciudadano global y ético"],
    "Semestre 2": ["Cálculo Integral", "Física Mecánica", "Química General", "Programacion orientada por objetos", "Circuitos", "Idioma I"],
    "Semestre 3": ["Cálculo Multivariado", "Biología General", "Fisica Electromagnetismo", "Electronica", "El poder de las probabilidades", "Idioma II"],
    "Semestre 4": ["Ecuaciones Diferenciales", "Conexión ambiental y resiliencia global", "Estática y dinámica", "Sistemas Digitales", "Ser Emprendedor = Actor de cambio", "Idioma III", "Formación Integral I"],
    "Semestre 5": ["Metodos Numericos", "Sistemas automáticos de control", "Análisis y simulación de mecanismos", "Probabilidad y estadística inferencial", "SosTECnibilidad 360", "Idioma IV"],
    "Semestre 6": ["DataXperience", "Automatización de procesos y control distribuido", "Sistemas Embebidos", "Sandbox para emprendedores", "Trend + Tech", "Electiva I"],
    "Semestre 7": ["Diseño Mecatronico", "Inteligencia Artificial", "Robótica Industrial", "Funding leaders", "Power skills para potenciar tu futuro", "Formacion Integral II", "Seminario de investigacion"],
    "Semestre 8": ["Gestión de proyectos", "Startup impacta", "Electiva II", "Electiva III", "Práctica Profesional", "Proyecto de grado"]
}

malla_sistemas = {
    "Semestre 1": ["Cálculo Diferencial", "Álgebra Lineal", "Algoritmos y Programación", "Ingenium for a Better World", "Real Maths", "Ciudadano global y ético"],
    "Semestre 2": ["Cálculo Integral", "Física Mecánica", "Química General", "Programacion orientada por objetos", "El poder de las probabilidades", "Idioma I"],
    "Semestre 3": ["Cálculo Multivariado", "Biología General", "Estructura de datos", "Arquitectura de Computadores y Sistemas operativos", "Trend + Tech", "Idioma II"],
    "Semestre 4": ["Ecuaciones Diferenciales", "Fisica Electromagnetismo", "Bases de Datos", "Probabilidad y estadística inferencial", "DataXperience", "Idioma III"],
    "Semestre 5": ["Metodos Numericos", "Matemáticas Discretas", "Seguridad Integral TI", "Redes I", "Power skills para potenciar tu futuro", "Idioma IV"],
    "Semestre 6": ["Sistemas de Información", "Desarrollo web y movil", "Conexión ambiental y resiliencia global", "Redes II", "Funding leaders", "Ser Emprendedor = Actor de cambio","Electiva I"],
    "Semestre 7": ["Arquitectura de Software", "Tecnologías Disruptivas", "Gestión de Proyectos", "Sandbox para emprendedores", "Formacion Integral I", "Formacion Integral II", "Seminario de investigacion"],
    "Semestre 8": ["SosTECnibilidad 360", "Startup impacta", "Electiva II", "Electiva III", "Práctica Profesional", "Proyecto de grado"]
}

malla_quimica = {
    "Semestre 1": ["Cálculo Diferencial", "Química General", "Biología General", "Física Mecánica"],
    "Semestre 2": ["Cálculo Integral", "Termodinámica I", "Química Orgánica", "Física Eléctrica"],
    "Semestre 3": ["Ecuaciones Diferenciales", "Máquinas Térmicas", "Electrónica I", "Economía"],
    "Semestre 4": ["Energías Renovables I", "Mecánica de Fluidos", "Electrónica II", "Estadística"],
    "Semestre 5": ["Sistemas Fotovoltaicos", "Control Automático", "Instrumentación", "Electiva I"],
    "Semestre 6": ["Energía Eólica", "Redes Eléctricas", "Electiva II", "Electiva III"],
    "Semestre 7": ["Gestión Energética", "Almacenamiento de Energía", "Electiva IV", "Electiva V"],
    "Semestre 8": ["Proyecto de Grado", "Legislación Energética", "Electiva VI"]
}

@app.route("/")
def index():
    return render_template("inicio.html")

@app.route("/malla/mecatronica")
def malla_mecatronica_view():
    return render_template("malla.html", nombre="Ingeniería Mecatrónica", malla=malla_mecatronica)

@app.route("/malla/sistemas")
def malla_sistemas_view():
    return render_template("malla.html", nombre="Ingeniería de Sistemas", malla=malla_sistemas)

@app.route("/malla/quimica")
def malla_quimica_view():
    return render_template("malla.html", nombre="Ingeniería en Química", malla=malla_quimica)

if __name__ == "__main__":
    app.run(debug=True)