from flask import Flask, render_template

app = Flask(__name__)

@app.route('/notaMateria', methods=['GET'])
def formulario():
    
    return render_template('inicio.html')   

@app.route('/notaMateria', methods=['POST'])
def notaMateria():
    # db = BaseDatos()
    # db.crearTabla()
    # definitiva = db.leer()
    # return definitiva
    nota = request.form['nota']
    porcentaje = request.form['porcentaje']
    defin = (porcentaje/100)*nota
    return defin


@app.route('/inicio')
def metodo():

    return render_template('inicio.html')


app.run(debug=True)