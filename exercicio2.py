"""
2-Implemente um algoritmo de busca binária que, dado um número inteiro alvo e uma lista de
números inteiros ordenada de forma crescente, retorne o índice da primeira ocorrência do
número na lista. Caso o número não esteja presente, retorne -1.
Regras:
● O algoritmo deve utilizar a estratégia de busca binária (divisão da lista em partes
menores).
● A entrada será sempre uma lista já ordenada.
Exemplo de entrada:
Lista: [5, 12, 18, 23, 45, 70, 89]
Alvo: 23
Exemplo de saída: 3
"""

def busca_binaria(lista, numero):
    intervalo = list(enumerate(lista))  

    while intervalo:
        meio = len(intervalo) // 2
        indice, valor = intervalo[meio]

        if valor == numero:
            return indice
        elif valor < numero:
            intervalo = intervalo[meio + 1:]  
        else:
            intervalo = intervalo[:meio]  

    return -1


lista = [5, 12, 18, 23, 45, 70, 89]
numero = int(input("Digite um número: "))

resultado = busca_binaria(lista, numero)

if resultado != -1:
    print(resultado)
else:
    print("-1")

