import Individuo
import copy
from random import randint,sample

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
        print("Melhor Individuo das populações:")
        print("Genotipo: ", self.melhorIndividuo.genotipo)
        print(f"FunçãoDeX:  {self.melhorIndividuo.FuncaoDeX:.2f}")
        print("-=" * 20)

    def mutarPopulacao(self):
        for i in range(self.tamanhoPopulação):
            novoY = self.individuos[i].mutacao()
            if novoY < self.melhorIndividuo.FuncaoDeX:
                self.melhorIndividuo = copy.deepcopy(self.individuos[i])
    
    def recombinaPopulacao(self):
        for i in range(self.tamanhoPopulação):
            elemento1, elemento2 = sample(range(self.tamanhoPopulação,2))

            fatiamento = randint(0,self.tamanhoPopulação - 1)

            novoIndividuo1 = self.individuos[elemento1].genotipo[:fatiamento]
            novoIndividuo2 = self.individuos[elemento2].genotipo[:fatiamento]

            novoIndividuo1 += self.individuos[elemento2].genotipo[fatiamento:]
            novoIndividuo2 += self.individuos[elemento1].genotipo[fatiamento:]

            print(novoIndividuo1)
            print(novoIndividuo2)


            


            

            

        


