class Definitiva():

    promedio = 0
    pga = 0
    definitiva = 0

    def __init__(self):
        pass

    def notaMateria(self, nota, porcentaje):
        self.definitiva += nota * porcentaje/100

    def getNotaMateria(self):
        return self.definitiva

    def prom_semestre(self, nota, creditos):
        sum_credit = 0
        sumaPuntos = 0
        sum_credit += creditos
        sumaPuntos += nota * creditos
        promedio = sumaPuntos / sum_credit

    def getPromSemestre(self):
        return self.promedio

    def PGA(self, totalPuntos, totalCreditos):
        self.pga = totalPuntos/totalCreditos

    def getPGA(self):
        return self.pga


