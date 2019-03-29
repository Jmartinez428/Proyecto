from flask import Flask, render_template
from flask import request
from flask import redirect
from database import BaseDatos
from calcular import Definitiva

app = Flask(__name__)

@app.route('/notaMateria', methods=['GET', 'POST'])
def notaMateria():

    definitiva = Definitiva()
    if request.method == 'POST':
        porcentaje = int(request.form['porcentaje'])
        nota = int(request.form['nota'])
        definitiva.notaMateria(nota, porcentaje)

        return redirect('/inicio')
        
    if request.method == 'GET':
        
        return "<h1>Tu nota es: </h1>" + str(definitiva.getNotaMateria())
   
    #db = BaseDatos()
    #db.crearTabla()
    #db.insertar(porcentaje, nota)
    #porcentaje, nota = db.leer()
    #definitiva += nota * porcentaje/100      
    # nota = request.form['nota']
    # porcentaje = request.form['porcentaje']
    # defin = (porcentaje/100)*nota
    # return defin

@app.route('/promSemestre', methods=['GET', 'POST'])
def promSemestre():

    definitiva = Definitiva()
    if request.method == 'POST':
        nota = int(request.form['nota'])
        creditos = int(request.form['creditos'])
        definitiva.prom_semestre(nota, creditos)
        return redirect('/inicio')
    else:
        return "<h1>Tu promedio es:</h1>" +str(definitiva.getPromSemestre())

@app.route('/PGA' , methods=['GET', 'POST'])
def PGA():
    
    if request.method == 'POST':
        pga = Definitiva()
        totPuntos = int(request.form['totPuntos'])
        totCreditos = int(request.form['totCreditos'])
        pga.PGA(totPuntos, totCreditos)
        return "<h1>Tu PGA es:</h1>" + str(pga.getPGA())

@app.route('/inicio', methods=['GET', 'POST'])
def metodo():

    return render_template('inicio.html')


app.run(debug=True)