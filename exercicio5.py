"""
5-Simulação de Saque em Caixa Eletrônico

Implemente um programa que receba um valor monetário inteiro e retorne a quantidade
mínima de notas e moedas necessárias para compor esse valor. O programa deve sempre
priorizar as notas de maior valor primeiro.
Notas e moedas disponíveis:
● Notas: 100, 50, 20, 10, 5, 2
● Moedas: 1
Regras:
● O valor sempre será inteiro e positivo.
● Deve-se minimizar a quantidade de cédulas e moedas utilizadas.
Exemplo de entrada:valor = 130
Exemplo de saída:
1 nota de 100
1 nota de 20
1 nota de 10
"""
def saque(valor):
    notas = [100, 50, 20, 10, 5, 2]  
    moedas = [1]  

    i = 0  
    while valor > 0:
        if i < len(notas) and valor >= notas[i]:  
            qtd = valor // notas[i]  
            valor %= notas[i]  
            print(f"{qtd} nota(s) de R$ {notas[i]}")
        elif i == len(notas):  
            qtd = valor // moedas[0]
            valor %= moedas[0]
            print(f"{qtd} moeda(s) de R$ {moedas[0]}")
        else:
            i += 1  


valor = int(input("Digite o valor para saque: "))
saque(valor)
