"""
1 - Fazer um algoritmo de estratégia gênetica(Trabalha com um único indivíduo e mutação)
2 - Fazer um algoritmo de de programação evolutiava(Usa uma população e mutação)
3 - Algoritmos Genéticos[População](Possuí uma população, trabalha com mutação e 
recombinação)

"""
# Imports
from População import Populacao
from Individuo import Individuo
import copy

# Função de inicialização das variáveis para a estrutura do individuo
def inicializaVariaveis():
    # Inicialização de algumas variáveis
    tamanhoGen = int
    A,B,C = 1,-5,6
    minimo,maximo = 0,6
    # Prompt pedindo as informações para a equação de 2 grau e o tamanho do genotipo(lista de binarios) do modelo
    print("=-" * 20)
    # tamanhoGen = int(input("Tamanho Genótipo:"))
    tamanhoGen = 5
    print("Digite o ABC de uma Função do 2º: ex(x2+2x+1)")
    # A = str(input("A: "))
    # B = str(input("B: "))
    # C = str(input("C: "))
    print(f"Sua função é {A} X² {B} X {C} ")
    print()
    funcao = {A,B,C}
    return tamanhoGen, funcao, minimo,maximo

metodo = 3
# HUD para escolher o algoritmo
# while True:
#     print("=-" * 20)
#     print("1 - Estratégia Evolutiva")
#     print("2 - Programação Evolutiva")
#     print("3 - Algoritmo Genético")
#     print("=-" * 20)
#     metodo = int(input("Escolha o algoritmo: "))
#     if metodo < 1 or metodo > 3:
#         print("Digite um valor válido")
#     else:
#         break

if metodo == 1:
    tamanhoGen, funcao, minimo,maximo = inicializaVariaveis()

    # Criação do individuo base
    indivi = Individuo(tamanhoGen,funcao,minimo,maximo)
    Y = indivi.define_variaveis()
    melhorIndivi = copy.deepcopy(indivi)
    indivi.mostrarDados()

    # Loop fazendo mutações e verificando o melhor individuo.
    print("-="*20)
    contadorMutacao = 0
    cont = int(input("Digite quantas mutações: "))
    for i in range(cont):
        novoY = indivi.mutacao()
        indivi.mostrarDados(contadorMutacao)
        contadorMutacao += 1
        if novoY < Y:
            melhorIndivi = copy.deepcopy(indivi)
            Y = novoY
    print("melhor resultado:")
    melhorIndivi.mostrarDados()

elif metodo == 2:
    tamanhoGen, funcao, minimo,maximo = inicializaVariaveis()
    # Criação da população
    # tamanhoPop = int(input("Tamanho População: "))
    tamanhoPop = 10
    populacao1 = Populacao(tamanhoPop, tamanhoGen)
    # Preencher a população
    for i in range(tamanhoPop):
        indivi = Individuo(tamanhoGen,funcao,minimo,maximo)
        indivi.define_variaveis()
        populacao1.addIndividuo(indivi)
    populacao1.mostrarPopulação()
    populacao1.mostrarMelhorIndividuo()

    # Faz mutação na população
    
    verify = int(input("Digite o número de vezes para mutar a população: "))
    print("-="*20)
    for i in range(verify):
        populacao1.mutarPopulacao()
    print("Ultima população:")
    populacao1.mostrarPopulação()
    populacao1.mostrarMelhorIndividuo()
elif metodo == 3:
    tamanhoGen, funcao, minimo,maximo = inicializaVariaveis()
    # Criação da população
    # tamanhoPop = int(input("Tamanho População: "))
    tamanhoPop = 10
    populacao1 = Populacao(tamanhoPop, tamanhoGen)

    # Preencher a população
    for i in range(tamanhoPop):
        indivi = Individuo(tamanhoGen,funcao,minimo,maximo)
        indivi.define_variaveis()
        populacao1.addIndividuo(indivi)
    populacao1.mostrarPopulação()
    populacao1.mostrarMelhorIndividuo()

    verify = int(input("Digite o número de vezes para recombinar a população: "))
    print("-="*20)
    for i in range(verify):
        populacao1.individuosCombinados.clear()
        populacao1.recombinaPopulacao()
    print("Ultima população:")
    populacao1.mostrarPopulaçãoCombinada()
    populacao1.mostrarMelhorIndividuo()