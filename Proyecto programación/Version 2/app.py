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
    "Semestre 1": ["Cálculo Diferencial", "Álgebra Lineal", "Química General", "Ingenium for a Better World", "Real Maths", "Ciudadano Global y Ético"],
    "Semestre 2": ["Cálculo Integral", "Física Mecánica", "Química Orgánica", "Algoritmos y Programación", "Biología General", "El Poder de las Probabilidades"],
    "Semestre 3": ["Cálculo Multivariado","Física Electromagnetismo","Bioquímica","Química Analítica","Balance de Masa y Energía","Trend + Tech"],
    "Semestre 4": ["Ecuaciones Diferenciales","Conexión Ambiental y Resiliencia Global","Termodinámica","Probabilidad y Estadística Inferencial","Ser Emprendedor = Actor de Cambio","Idioma I","Formación Integral I"],
    "Semestre 5": ["Métodos Numéricos","Fenómenos de Transporte de Calor y Masa","Mecánica de Fluidos e Hidráulica","Termoquímica","SosTECnibilidad 360","Idioma II"],
    "Semestre 6": ["Operaciones Unitarias","Ingeniería de las Reacciones Químicas","DataXperience","Sandbox para Emprendedores","Power Skills para Potenciar tu Futuro","Idioma III"],
    "Semestre 7": ["Funding Leaders","Control de Procesos","Startup Impacta","Formación Integral II","Idioma IV","Seminario de Investigación","Electiva I"],
    "Semestre 8": ["Gestión de Proyectos","Diseño de Productos y Procesos","Electiva II","Electiva III","Práctica Profesional","Proyecto de Grado"]
}

malla_energias = {
    "Semestre 1": ["Cálculo Diferencial", "Álgebra Lineal", "Biología General", "Ingenium for a Better World", "Real Maths", "Ciudadano Global y Ético"],
    "Semestre 2": ["Cálculo Integral", "Física Mecánica", "Química General", "Energía para Genios", "Conexión Ambiental y Resiliencia Global", "Formación Integral I", "Ser Emprendedor = Actor de Cambio"],
    "Semestre 3": ["Cálculo Multivariado", "Física Electromagnetismo", "Algoritmos y Programación", "Power Skills para Potenciar tu Futuro", "El Poder de las Probabilidades", "Idioma I"],
    "Semestre 4": ["Ecuaciones Diferenciales", "Termodinámica", "Circuitos", "Sandbox para Emprendedores", "SosTECnibilidad 360", "Idioma II"],
    "Semestre 5": ["Métodos Numéricos", "Eficiencia Energética", "Sistemas Automáticos de Control", "Física de Calor y Ondas", "Trend + Tech", "Idioma III"],
    "Semestre 6": ["Matemáticas Especiales", "Mecánica de Fluidos e Hidráulica", "Diseño y Análisis de Sistemas Energéticos", "Fuentes no Convencionales de Energía Renovable", "DataXperience", "Idioma IV"],
    "Semestre 7": ["Funding Leaders", "Mercado Energético Global y Regulación Estratégica", "Grid Management Technologies and Risks", "Startup Impacta", "Formación Integral II", "Seminario de Investigación", "Electiva I"],
    "Semestre 8": ["Gestión de Proyectos", "Gestión de la Energía", "Electiva II", "Electiva III", "Práctica Profesional", "Proyecto de Grado"]
}

malla_ambiental = {
    "Semestre 1": ["Cálculo Diferencial", "Álgebra Lineal", "Ingenium for a Better World", "Biología General", "Real Maths", "Ciudadano Global y Ético"],
    "Semestre 2": ["Cálculo Integral", "Física Mecánica", "Química General", "Conexión Ambiental y Resiliencia Global", "Power Skills para Potenciar tu Futuro", "Formación Integral I", "Ser Emprendedor = Actor de Cambio"],
    "Semestre 3": ["Cálculo Multivariado", "Física Electromagnetismo", "Bioquímica", "Trend + Tech", "El Poder de las Probabilidades", "SosTECnibilidad 360"],
    "Semestre 4": ["Ecuaciones Diferenciales", "Mecánica de Fluidos e Hidráulica", "Algoritmos y Programación", "Tecnologías Geoespaciales", "Probabilidad y Estadística Inferencial", "Sandbox para Emprendedores"],
    "Semestre 5": ["Métodos Numéricos", "Economía Circular", "Gestión del Territorio y del Suelo", "Gestión del Recurso Hídrico", "DataXperience", "Idioma I"],
    "Semestre 6": ["Calidad del Aire", "Termodinámica", "Derecho Ambiental y Licenciamiento Ambiental", "Gestión de la Sostenibilidad", "Startup Impacta", "Idioma II"],
    "Semestre 7": ["Funding Leaders", "Gestión de Proyectos", "Ecología, Regeneración y Restauración", "Acción Climática", "Formación Integral II", "Idioma III", "Seminario de Investigación"],
    "Semestre 8": ["Electiva I", "Electiva II", "Electiva III", "Idioma IV", "Práctica Profesional", "Proyecto de Grado"]
}

malla_industrial = {
    "Semestre 1": ["Ingenium for a Better World", "Química General", "Real Maths", "El Poder de las Probabilidades", "Ciudadano Global y Ético", "Idioma I"],
    "Semestre 2": ["Ecodiseño y Ecoindustria", "Conexión Ambiental y Resiliencia Global", "Cálculo Diferencial", "Álgebra Lineal", "Ser Emprendedor = Actor de Cambio", "Formación Integral I", "Idioma II"],
    "Semestre 3": ["Ciclo de Vida y Manufactura", "Biología General", "Cálculo Integral", "Trend + Tech", "SosTECnibilidad 360", "Idioma III"],
    "Semestre 4": ["Diseño Industrial para Ingenieros", "Factores Humanos y Organización", "Cálculo Multivariado", "Probabilidad y Estadística Inferencial", "Física Mecánica", "Idioma IV"],
    "Semestre 5": ["Revolución en la Gestión de Operaciones", "Calidad y Confiabilidad Operativa", "Smart Factory", "Algoritmos y Programación", "Física Electromagnetismo", "Ecuaciones Diferenciales"],
    "Semestre 6": ["Gestión de la Cadena de Suministro", "Estrategias de Sostenibilidad Económica", "DataXperience", "Investigación de Operaciones", "Métodos Numéricos", "Startup Impacta"],
    "Semestre 7": ["Excelencia Operacional", "Simulación y Optimización de Procesos", "Funding Leaders", "Power Skills para Potenciar tu Futuro", "Sandbox para Emprendedores", "Formación Integral II", "Seminario de Investigación"],
    "Semestre 8": ["Gestión de Proyectos", "Electiva I", "Electiva II", "Electiva III", "Práctica Profesional", "Proyecto de Grado"]
}

malla_industrial = {
    "Semestre 1": ["Ingenium for a Better World", "Química General", "Real Maths", "El Poder de las Probabilidades", "Ciudadano Global y Ético", "Idioma I"],
    "Semestre 2": ["Ecodiseño y Ecoindustria", "Conexión Ambiental y Resiliencia Global", "Cálculo Diferencial", "Álgebra Lineal", "Ser Emprendedor = Actor de Cambio", "Formación Integral I", "Idioma II"],
    "Semestre 3": ["Ciclo de Vida y Manufactura", "Biología General", "Cálculo Integral", "Trend + Tech", "SosTECnibilidad 360", "Idioma III"],
    "Semestre 4": ["Diseño Industrial para Ingenieros", "Factores Humanos y Organización", "Cálculo Multivariado", "Probabilidad y Estadística Inferencial", "Física Mecánica", "Idioma IV"],
    "Semestre 5": ["Revolución en la Gestión de Operaciones", "Calidad y Confiabilidad Operativa", "Smart Factory", "Algoritmos y Programación", "Física Electromagnetismo", "Ecuaciones Diferenciales"],
    "Semestre 6": ["Gestión de la Cadena de Suministro", "Estrategias de Sostenibilidad Económica", "DataXperience", "Investigación de Operaciones", "Métodos Numéricos", "Startup Impacta"],
    "Semestre 7": ["Excelencia Operacional", "Simulación y Optimización de Procesos", "Funding Leaders", "Power Skills para Potenciar tu Futuro", "Sandbox para Emprendedores", "Formación Integral II", "Seminario de Investigación"],
    "Semestre 8": ["Gestión de Proyectos", "Electiva I", "Electiva II", "Electiva III", "Práctica Profesional", "Proyecto de Grado"]
}

malla_industrial = {
    "Semestre 1": ["Ingenium for a Better World", "Química General", "Real Maths", "El Poder de las Probabilidades", "Ciudadano Global y Ético", "Idioma I"],
    "Semestre 2": ["Ecodiseño y Ecoindustria", "Conexión Ambiental y Resiliencia Global", "Cálculo Diferencial", "Álgebra Lineal", "Ser Emprendedor = Actor de Cambio", "Formación Integral I", "Idioma II"],
    "Semestre 3": ["Ciclo de Vida y Manufactura", "Biología General", "Cálculo Integral", "Trend + Tech", "SosTECnibilidad 360", "Idioma III"],
    "Semestre 4": ["Diseño Industrial para Ingenieros", "Factores Humanos y Organización", "Cálculo Multivariado", "Probabilidad y Estadística Inferencial", "Física Mecánica", "Idioma IV"],
    "Semestre 5": ["Revolución en la Gestión de Operaciones", "Calidad y Confiabilidad Operativa", "Smart Factory", "Algoritmos y Programación", "Física Electromagnetismo", "Ecuaciones Diferenciales"],
    "Semestre 6": ["Gestión de la Cadena de Suministro", "Estrategias de Sostenibilidad Económica", "DataXperience", "Investigación de Operaciones", "Métodos Numéricos", "Startup Impacta"],
    "Semestre 7": ["Excelencia Operacional", "Simulación y Optimización de Procesos", "Funding Leaders", "Power Skills para Potenciar tu Futuro", "Sandbox para Emprendedores", "Formación Integral II", "Seminario de Investigación"],
    "Semestre 8": ["Gestión de Proyectos", "Electiva I", "Electiva II", "Electiva III", "Práctica Profesional", "Proyecto de Grado"]
}

malla_industrial = {
    "Semestre 1": ["Ingenium for a Better World", "Química General", "Real Maths", "El Poder de las Probabilidades", "Ciudadano Global y Ético", "Idioma I"],
    "Semestre 2": ["Ecodiseño y Ecoindustria", "Conexión Ambiental y Resiliencia Global", "Cálculo Diferencial", "Álgebra Lineal", "Ser Emprendedor = Actor de Cambio", "Formación Integral I", "Idioma II"],
    "Semestre 3": ["Ciclo de Vida y Manufactura", "Biología General", "Cálculo Integral", "Trend + Tech", "SosTECnibilidad 360", "Idioma III"],
    "Semestre 4": ["Diseño Industrial para Ingenieros", "Factores Humanos y Organización", "Cálculo Multivariado", "Probabilidad y Estadística Inferencial", "Física Mecánica", "Idioma IV"],
    "Semestre 5": ["Revolución en la Gestión de Operaciones", "Calidad y Confiabilidad Operativa", "Smart Factory", "Algoritmos y Programación", "Física Electromagnetismo", "Ecuaciones Diferenciales"],
    "Semestre 6": ["Gestión de la Cadena de Suministro", "Estrategias de Sostenibilidad Económica", "DataXperience", "Investigación de Operaciones", "Métodos Numéricos", "Startup Impacta"],
    "Semestre 7": ["Excelencia Operacional", "Simulación y Optimización de Procesos", "Funding Leaders", "Power Skills para Potenciar tu Futuro", "Sandbox para Emprendedores", "Formación Integral II", "Seminario de Investigación"],
    "Semestre 8": ["Gestión de Proyectos", "Electiva I", "Electiva II", "Electiva III", "Práctica Profesional", "Proyecto de Grado"]
}

malla_ciencias_datos = {
    "Semestre 1": ["Cálculo Diferencial", "Ingenium for a Better World", "Biología General", "Química General", "Real Maths", "Ciudadano Global y Ético"],
    "Semestre 2": ["Cálculo Integral", "Física Mecánica", "Álgebra Lineal", "Algoritmos y Programación", "Trend + Tech", "Idioma I"],
    "Semestre 3": ["Cálculo Multivariado", "Visualización de Datos", "Matemáticas Discretas", "Programación Orientada por Objetos", "El Poder de las Probabilidades", "Idioma II"],
    "Semestre 4": ["Ecuaciones Diferenciales", "Estructura de Datos", "DataXperience", "Probabilidad y Estadística Inferencial", "Startup Impacta", "Idioma III"],
    "Semestre 5": ["Métodos Numéricos", "Big Data e Ingeniería de Datos", "Gobernanza de Datos", "Bases de Datos", "Idioma IV", "Electiva I"],
    "Semestre 6": ["Análisis Multivariado de Datos", "Machine Learning", "Funding Leaders", "Gestión de Proyectos", "Ser Emprendedor = Actor de Cambio", "Formación Integral I", "Electiva II"],
    "Semestre 7": ["Series de Tiempo", "Deep Learning", "Analítica en la Nube", "Conexión Ambiental y Resiliencia Global", "Formación Integral II", "SosTECnibilidad 360", "Seminario de Investigación"],
    "Semestre 8": ["Data Mining e Inteligencia de Negocios", "Sandbox para Emprendedores", "Power Skills para Potenciar tu Futuro", "Electiva III", "Práctica Profesional", "Proyecto de Grado"]
}

malla_produccion = {
    "Semestre 1": ["Ingenium for a Better World", "Química General", "Real Maths", "El Poder de las Probabilidades", "Idioma I", "Ciudadano Global y Ético"],
    "Semestre 2": ["Ingeniería de Materiales", "Cálculo Diferencial", "Conexión Ambiental y Resiliencia Global", "Álgebra Lineal", "Idioma II", "Formación Integral I", "Ser Emprendedor = Actor de Cambio"],
    "Semestre 3": ["Procesos de Manufactura", "Cálculo Integral", "Biología General", "Trend + Tech", "Idioma III", "SosTECnibilidad 360"],
    "Semestre 4": ["Ingeniería de Métodos", "Cálculo Multivariado", "Física Mecánica", "Algoritmos y Programación", "Idioma IV", "Operaciones Unitarias"],
    "Semestre 5": ["Smart Factory", "Física Electromagnetismo", "Ecuaciones Diferenciales", "Probabilidad y Estadística Inferencial", "Gestión de Costos", "Power Skills para Potenciar tu Futuro"],
    "Semestre 6": ["Gestión de Proyectos", "Electricidad y Electrónica", "Métodos Numéricos", "Investigación de Operaciones", "DataXperience", "Startup Impacta"],
    "Semestre 7": ["Mantenimiento y Seguridad Industrial", "Automatización y Control", "Diseño de Sistemas de Producción", "Funding Leaders", "Sandbox para Emprendedores", "Formación Integral II", "Seminario de Investigación"],
    "Semestre 8": ["Gestión de Calidad", "Manufactura Asistida por Computador", "Ergonomía y Diseño de Puestos de Trabajo", "Diseño con Polímeros - Manufactura y Partes", "Práctica Profesional", "Proyecto de Grado"]
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
    return render_template("malla.html", nombre="Ingeniería Química", malla=malla_quimica)

@app.route("/malla/energias")
def malla_energias_view():
    return render_template("malla.html", nombre="Ingeniería en Energías", malla=malla_energias)

@app.route("/malla/ambiental")
def malla_ambiental_view():
    return render_template("malla.html", nombre="Ingeniería Ambiental", malla=malla_ambiental)

@app.route("/malla/industrial")
def malla_industrial_view():
    return render_template("malla.html", nombre="Ingeniería Industrial", malla=malla_industrial)

@app.route("/malla/ciencias_datos")
def malla_ciencias_datos_view():
    return render_template("malla.html", nombre="Ingeniería en Ciencias de Datos", malla=malla_ciencias_datos)

@app.route("/malla/produccion")
def malla_produccion_view():
    return render_template("malla.html", nombre="Ingeniería de Producción", malla=malla_produccion)

if __name__ == "__main__":
    app.run(debug=True)
