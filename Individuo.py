from random import randint
from bitstring import BitArray


class Individuo:
    def __init__(self, tamanhoGen, funcao):
        self.gene = {}
        self.tamanhoGen = tamanhoGen
        self.decimal = 0
        self.normalizado = 0
        self.FuncaoDeX = 0
        self.define_variaveis()

    def define_variaveis(self):
        if self.gene is None:
            self.gene = []
        for i in range(self.tamanhoGen):
            self.gene.append(str(randint(0, 1)))
        gene_string = ''.join(self.gene)
        self.decimal = BitArray(bin=gene_string).uint
        self.normalizado = (self.decimal/((2 ** self.tamanhoGen) - 1)) * 6
        self.FuncaoDeX = self.normalizado**2 - 5 * self.normalizado + 6

    # def define_variaveis(self):
    #     if not self.gene:
    #         for i in range(self.tamanhoGen):
    #             self.gene.append(str(randint(0, 1)))
    #     gene_string = ''.join(self.gene)
    #     self.decimal = BitArray(bin=gene_string).uint
    #     self.normalizado = (self.decimal/((2 ** self.tamanhoGen) - 1)) * 6
    #     self.FuncaoDeX = self.normalizado**2 - 5 * self.normalizado + 6

    def mutacao(self):
        novoGene = list(self.gene)
        valorMudar = randint(0, self.tamanhoGen - 1)
        if novoGene[valorMudar] == "1":
            novoGene[valorMudar] = '0'
        else:
            novoGene[valorMudar] = '1'
        self.gene = "".join(novoGene)
        self.define_variaveis()

    def mostrarDados(self):
        print("Gene: ", self.gene)
        print("tamanhoGen: ", self.tamanhoGen)
        print("Decimal: ", self.decimal)
        print("Normalizado: ", self.normalizado)
        print("Funcao de X: ", self.FuncaoDeX)

