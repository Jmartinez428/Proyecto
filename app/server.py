from flask import Flask, render_template

app = Flask(__name__)


@app.route('/inicio')
def metodo():

    return render_template('inicio.html')


app.run(debug=True)