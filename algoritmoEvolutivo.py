from random import randint
from bitstring import BitArray
import copy

class Individuo:
    def __init__(self,gene = list(), bits=5):
        self.gene = gene
        self.bits = bits
        self.decimal = 0
        self.normalizado = 0
        self.FuncaoDeX = 0
        self.define_variaveis()

    def define_variaveis(self):
        if not self.gene:
            for i in range(self.bits):
                self.gene.append(str(randint(0, 1)))
        gene_string = ''.join(self.gene)
        self.decimal = BitArray(bin=gene_string).uint
        self.normalizado = (self.decimal/((2 ** self.bits) - 1)) * 6
        self.FuncaoDeX = self.normalizado**2 - 5 * self.normalizado + 6

    def mutacao(self):
        novoGene = list(self.gene)
        valorMudar = randint(0, self.bits - 1)
        if novoGene[valorMudar] == "1":
            novoGene[valorMudar] = '0'
        else:
            novoGene[valorMudar] = '1'
        self.gene = "".join(novoGene)
        self.define_variaveis()

    def mostrarDados(self):
        print("Gene: ", self.gene)
        print("Bits: ", self.bits)
        print("Decimal: ", self.decimal)
        print("Normalizado: ", self.normalizado)
        print("Funcao de X: ", self.FuncaoDeX)

print("=-" * 30)
print("Algoritmo evolutivo")
print("=-" * 30)
#TamanhoPopulacao = input(int("Digite o tamanho da população: "))
TamanhoPopulacao = int(5)
geneAtual = Individuo(bits = TamanhoPopulacao)
melhorGene = copy.deepcopy(geneAtual)
geneAtual.mostrarDados()
print("=-" * 30)
for i in range(0, 1000):
    geneAtual.mutacao()
    if geneAtual.FuncaoDeX < melhorGene.FuncaoDeX:
        melhorGene = copy.deepcopy(geneAtual)
melhorGene.mostrarDados()
print("=-" * 30)

"""
1 - Criar o algoritmo genético
    1.1 - Criar a classe individuo !!
    1.2 - Criar a função de definiri variaveis !!
    1.3 - Criar a função de mutação !!
    1.4 - Achar o melhor gene pela F(X) !!
2 - Melhorar algoritmo genético
    2.1 - Trocar a F(X) 
    2.2 - 
    2.3 -
    2.4 -

"""