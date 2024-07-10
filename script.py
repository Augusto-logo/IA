"""
1 - Fazer um algoritmo de estratégia gênetica(Trabalha com um único indivíduo e mutação)
2 - Fazer um algoritmo de de programação evolutiava(Usa uma população e mutação)
3 - Algoritmos Genéticos[População](Possuí uma população, trabalha com mutação e 
recombinação)

"""

# import População
# from programaçãoEvolutiva import individuo
# import copy

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
    import Individuo
    tamanhoGen = int
    A = int
    B = int
    C = int
    print("=-" * 20)
    tamanhoGen = int(input("Tamanho Genótipo:"))
    print("Digite o ABC de uma Função do 2º: ex(x2+2x+1)")
    A = str(input("A: "))
    B = str(input("B: "))
    C = str(input("C: "))
    print(f"Sua função é {A} X² {B} X {C} ")
    funcao = {A,B,C}
    gen1 = Individuo(tamanhoGen,funcao)
    print("=-" * 20)
