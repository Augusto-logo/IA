import Individuo

class Populacao:
    def __init__(self, tamanhoPopulação,tamanhoIndividuo):
        self.tamanhoPopulação = tamanhoPopulação
        self.tamanhoIndividuo = tamanhoIndividuo
        self.individuos = list()

    def addIndividuo(self, individuo):
        self.individuos.append(individuo)

    def mostrarPopulação(self):
        for i in range (0,self.tamanhoPopulação):
            print("Individuo: ", self.individuos[i].gene)

