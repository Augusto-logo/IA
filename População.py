import Individuo
import copy
from random import sample

class Populacao:
    def __init__(self, tamanhoPopulação,tamanhoIndividuo):
        self.tamanhoPopulação = tamanhoPopulação
        self.tamanhoIndividuo = tamanhoIndividuo
        self.individuos = list()
        self.melhorIndividuo = None

    def addIndividuo(self, individuo):
        self.individuos.append(individuo)
        if self.melhorIndividuo == None:
            self.melhorIndividuo = self.individuos[0]
            return
        if individuo.FuncaoDeX < self.melhorIndividuo.FuncaoDeX:
            self.melhorIndividuo = copy.deepcopy(individuo)

    def mostrarPopulação(self):
        for i in range (0,self.tamanhoPopulação):
            print("Individuo: ", i)
            print(f"genotipo: {self.individuos[i].genotipo}")
            print(f"FunçãoDeX:  {self.individuos[i].FuncaoDeX:.2f}")    
    
    def mostrarMelhorIndividuo(self):
        print("-=" * 20)
        print("Melhor Individuo da população:")
        print("Genotipo: ", self.melhorIndividuo.genotipo)
        print(f"FunçãoDeX:  {self.melhorIndividuo.FuncaoDeX:.2f}")
        print("-=" * 20)

    def mutarPopulacao(self, contador):
        for i in range(contador):
            indexes = sample(range(0,self.tamanhoPopulação),contador)
        for i in range(contador):
            self.individuos[indexes[i]].mutacao
