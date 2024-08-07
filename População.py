import Individuo
import copy
from random import randint,choice

class Populacao:
    def __init__(self, tamanhoPopulação,tamanhoIndividuo):
        self.tamanhoPopulação = tamanhoPopulação
        self.tamanhoIndividuo = tamanhoIndividuo
        self.individuos = list()
        self.individuosCombinados = list()
        self.melhorIndividuo = None

    def addIndividuo(self, individuo):
        self.individuos.append(individuo)
        if self.melhorIndividuo == None:
            self.melhorIndividuo = self.individuos[0]
            return
        if individuo.FuncaoDeX < self.melhorIndividuo.FuncaoDeX:
            self.melhorIndividuo = copy.deepcopy(individuo)
    
    def addIndividuoCombinado(self, individuo):
        taxa = randint(0,100)
        if taxa < 10:
            novoY = individuo.mutacao()
        self.individuosCombinados.append(individuo)
        if novoY < self.melhorIndividuo.FuncaoDeX:
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
        print(f"Valor de X: {self.melhorIndividuo.normalizado:.2f}")
        print("-=" * 20)

    def mutarPopulacao(self):
        for i in range(self.tamanhoPopulação):
            novoY = self.individuos[i].mutacao()
            if novoY < self.melhorIndividuo.FuncaoDeX:
                self.melhorIndividuo = copy.deepcopy(self.individuos[i])
    
    def recombinaPopulacao(self):
        bufferLista = list()
        repetidor = int(self.tamanhoPopulação/2)

        for i in range(self.tamanhoPopulação):
            bufferLista.append(i)
        
        for i in range(repetidor):
            geno1 = choice(bufferLista)
            bufferLista.remove(geno1)
        
            geno2 = choice(bufferLista)
            bufferLista.remove(geno2)
        
            fatiamento = randint(1, self.tamanhoPopulação - 1)
        
            novoIndividuo1 = self.individuos[geno1].genotipo[:fatiamento] + self.individuos[geno2].genotipo[fatiamento:]
            novoIndividuo2 = self.individuos[geno2].genotipo[:fatiamento] + self.individuos[geno1].genotipo[fatiamento:]
        
            # Cria uma nova instância de bufferIndividuo para o primeiro indivíduo combinado
            bufferIndividuo1 = copy.deepcopy(self.individuos[0])
            bufferIndividuo1.genotipo = copy.deepcopy(novoIndividuo1)
            self.addIndividuoCombinado(bufferIndividuo1)
        
            # Cria uma nova instância de bufferIndividuo para o segundo indivíduo combinado
            bufferIndividuo2 = copy.deepcopy(self.individuos[0])
            bufferIndividuo2.genotipo = copy.deepcopy(novoIndividuo2)
            self.addIndividuoCombinado(bufferIndividuo2)

        if not bufferLista:
            return
        else:
            fatiamento = randint(0,self.tamanhoPopulação - 1)
            novoIndividuo = self.individuos[bufferLista[0]].genotipo[:fatiamento]
            novoIndividuo += self.individuos[bufferLista[0]].genotipo[fatiamento:]
            self.addIndividuoCombinado(novoIndividuo)
    


    def mostrarPopulaçãoCombinada(self):
        for i in range (self.tamanhoPopulação):
            print("Individuo: ", i)
            print(f"genotipo: {self.individuosCombinados[i].genotipo}")
            print(f"FunçãoDeX:  {self.individuosCombinados[i].FuncaoDeX:.2f}")
