from flask import Flask, render_template

app = Flask(__name__)
  

@app.route('/notaMateria')
def notaMateria(req, nota, porcentaje):

     db = BaseDatos()
     db.crearTabla()
     db.insertar(porcentaje, nota)
     porcentaje, nota = db.leer().split()
     definitiva += nota * porcentaje/100
     return definitiva


    # nota = request.form['nota']
    # porcentaje = request.form['porcentaje']
    # defin = (porcentaje/100)*nota
    # return defin


@app.route('/inicio')
def metodo():

    return render_template('inicio.html')


app.run(debug=True)