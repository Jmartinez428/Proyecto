import sqlite3

class BaseDatos():

def __init__(self):
    pass


def crearTabla(self):
    conn = sqlite3.connect('data.notasdb')
    c = conn.cursor()
    c.execute('CREATE TABLE Notas (materia text, porcentaje real, nota real')
    conn.commit()
    conn.close()


def insertar(porcentaje, nota):
    conn = sqlite3.connect('data.notasdb')
    c = conn.cursor()
    c.execute("INSERT INTO Notas VALUES ('materia', porcentaje, nota)")
    conn.commit()
    conn.close()

def leer(self):
    conn = sqlite3.connect('data.notasdb')
    c = conn.cursor()
    c.execute("SELECT porcentaje, nota FROM Notas")
    u = c.fetchone()
    conn.close()
    return u



