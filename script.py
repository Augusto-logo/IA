"""
1 - Fazer um algoritmo de estratégia gênetica(Trabalha com um único indivíduo e mutação)
2 - Fazer um algoritmo de de programação evolutiava(Usa uma população e mutação)
3 - Algoritmos Genéticos[População](Possuí uma população, trabalha com mutação e 
recombinação)

"""

# import População
# from programaçãoEvolutiva import individuo
import copy

metodo = 1
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
    # Inicialização de algumas variáveis e importação da classe de modelo
    verify = 0
    from Individuo import Individuo
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
    # Criação do individuo base
    funcao = {A,B,C}
    indivi = Individuo(tamanhoGen,funcao,minimo,maximo)
    melhorIndivi = Individuo(tamanhoGen,funcao,minimo,maximo)
    melhorIndivi = copy.deepcopy(indivi)
    Y = indivi.define_variaveis()
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