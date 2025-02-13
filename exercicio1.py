"""
1-Crie um programa que, dado um número inteiro n, retorne os primeiros n números da sequência de Fibonacci.
Exemplo de entrada: n = 6
Exemplo de saída: [0, 1, 1, 2, 3, 5]
"""
def fibonacci():
    numero = int(input("Informe um número:"))
    num1 = 0
    num2 = 1
    for i in range(numero):
        print(num1)
        num3= num1 + num2
        num1 = num2
        num2 = num3
fibonacci()