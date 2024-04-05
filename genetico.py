from random import randint
from bitstring import BitArray
class individuo:
    def __init__(self, gene = 0,bits = -1, decimal = 0, normalizado = 0, FuncaoDeX = 0, melhorGene = 0):
        self.gene = gene
        self.bits = bits
        self.decimal = decimal
        self.normalizado = normalizado
        self.FuncaoDeX = FuncaoDeX
        self.melhorGene = melhorGene
        self.defineVariaveis()

    def defineVariaveis(self):
        if self.bits == -1:
            self.bits = randint(1,8)
            self.gene = str()
            for i in range(self.bits):
                self.gene += str(randint(0,1))
            self.melhorGene = self.gene
        self.decimal = BitArray(bin = self.gene).uint
        self.normalizado = (self.decimal/((2 ** self.bits) - 1)) * 6 
        self.FuncaoDeX = self.normalizado**2 - 5 * self.normalizado + 6
    
    def verificaMelhorGene(self,funcaoAntiga):
        self.defineVariaveis()
        if self.FuncaoDeX < funcaoAntiga:
            self.melhorGene = self.gene

    def mutacao(self):
        funcaoAntiga = self.FuncaoDeX
        antigoGene = self.gene
        novoGene = list(self.gene)
        valorMudar = randint(0, self.bits - 1)
        if novoGene[valorMudar] == "1":
            novoGene[int(valorMudar)] = '0'
        else:
            novoGene[int(valorMudar)] = '1'
        self.gene = "".join(novoGene)    
        self.verificaMelhorGene(funcaoAntiga)

    def mostrarDados(self):
        print("Gene: ", self.gene)
        print("Bits: ", self.bits)
        print("Decimal: ", self.decimal)
        print("normalizado: ", self.normalizado)
        print("Funcao de X: ", self.FuncaoDeX)
        print("O melhor gene até o momento é: ", self.melhorGene)
    
    def mostrarMelhorGene(self):
        self.decimal = BitArray(bin = self.melhorGene).uint
        self.normalizado = (self.decimal/((2 ** self.bits) - 1)) * 6 
        self.FuncaoDeX = self.normalizado**2 - 5 * self.normalizado + 6
        print("=-" * 30)
        print("O melhor gene encontrado foi o :", self.melhorGene)
        print("Decimal: ", self.decimal)
        print("normalizado: ", self.normalizado)
        print("Funcao de X: ", self.FuncaoDeX)

print("=-" * 30)
print("Algoritmo evolutivo")
print("=-" * 30)
g1 = individuo()
g1.mostrarDados()
for i in range(0,100):
    g1.mutacao()
g1.mostrarMelhorGene()