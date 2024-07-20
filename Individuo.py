from random import randint

class Individuo:
    def __init__(self,  tamanhoGeno, funcao, minimo, maximo):
        self.genotipo = []  # Lista vazia, pronta para ser preenchida
        self.posicaoMelhorGenotipo = 0  # Posição do melhor genotipo
        self.tamanhoGeno = tamanhoGeno  # AutoExplicativo
        self.funcao = funcao if isinstance(funcao, list) else list(funcao)  # Garante que funcao seja uma lista
        self.min = minimo
        self.max = maximo
        self.decimal = 0  # O valor binário do genotipo convertido para decimal
        self.normalizado = 0  # Valor decimal normalizado para usar na função, utilizando MIN e MAX
        self.FuncaoDeX = 0  # Achar a função de X(y) em função do valor em NORMALIZADO
        
    def define_genotipo(self, genotipo=None): # Função que cria um genotipo
        if genotipo is None:
            self.genotipo = list()
        else:
            self.genotipo = genotipo
        for i in range(self.tamanhoGeno):
            self.genotipo.append(randint(0,1))

    def define_decimal(self, genotipo):
        genotipoString = ''.join(str(bit) for bit in genotipo)
        self.decimal = int(genotipoString, 2)

    def define_normalizado(self, decimal, min, max, tamanhoGeno):
        self.normalizado = min + (max - min) * (decimal/((2 ** tamanhoGeno)-1))
    
    def define_funcaoDeX(self, normalizado, funcao):
        A = funcao[0]
        B = funcao[1]
        C = funcao[2]
        self.FuncaoDeX = (A  * (normalizado ** 2)) + (B * normalizado) + C
    
    def mutacao(self):
        novoGenotipo = self.genotipo
        indexRandom = randint(0, self.tamanhoGeno - 1)
        if novoGenotipo[indexRandom] == "1":
            novoGenotipo[indexRandom] = 0
        else:
            novoGenotipo[indexRandom] = 1
        self.genotipo.clear()
        self.genotipo = novoGenotipo.copy()
        Y = self.define_variaveis()
        return Y

    def define_variaveis(self):
        self.define_genotipo(self.genotipo)
        self.define_decimal(self.genotipo)
        self.define_normalizado(self.decimal, self.min, self.max, self.tamanhoGeno)
        self.define_funcaoDeX(self.normalizado, self.funcao)
        return self.FuncaoDeX

    def mostrarDados(self, contadorMutacoes = None):
        print("-="*20)
        print("Nº Mutação: ", contadorMutacoes)
        print("Genótipo: ", self.genotipo)
        print("tamanhoGeno: ", self.tamanhoGeno)
        print("Função:", self.funcao)
        print("Decimal: ", self.decimal)
        print(f"Normalizado: {self.normalizado:.2f}")
        print(f"Funcao de X: {self.FuncaoDeX:.2f}")

class Populacao:
    def __init__(self, tamanho, tamanhoGen):
        """
        Inicializa a população com um tamanho específico e tamanho de genoma para os indivíduos.
        """
    
    def addIndividuo(self, individuo):
        """
        Adiciona um novo indivíduo à população.
        """
    
    def mostrarPopulação(self):
        """
        Imprime todos os indivíduos da população.
        """
    
    def mostrarMelhorIndividuo(self):
        """
        Identifica e mostra o indivíduo com o melhor fitness na população.
        """
    
    def mutarPopulacao(self):
        """
        Aplica mutação em indivíduos da população com uma certa probabilidade.
        """

