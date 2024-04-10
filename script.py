import População
import Individuo
import copy

print("=-" * 30)
print("Algoritmo evolutivo")
print("=-" * 30)
#TamanhoPopulacao = input(int("Digite o tamanho da população: "))
#TamanhoGene = input(int("Digite o tamanho do gene: "))
TamanhoGene = int(8)
tamanhoPopulação = int(10)

populacao1 = População.Populacao(tamanhoPopulação, TamanhoGene)

for i in range (0, tamanhoPopulação):
    individuo1 = Individuo.Individuo()
    populacao1.addIndividuo(individuo1)
    individuo1 = None

populacao1.mostrarPopulação()
# melhorIndividuo = copy.deepcopy(individuo1)


# individuo1.mostrarDados()
# print("=-" * 30)

# for i in range(0, 1000):
#     geneAtual.mutacao()
#     if geneAtual.FuncaoDeX < melhorGene.FuncaoDeX:
#         melhorGene = copy.deepcopy(geneAtual)
# melhorGene.mostrarDados()
# print("=-" * 30)

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