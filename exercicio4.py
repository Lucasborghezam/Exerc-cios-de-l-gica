"""
4-Substring Palindrômica Mais Longa
Implemente um programa que, dada uma string, encontre a maior substring palindrômica
dentro dela.
Regras:
● Uma substring palindrômica é uma sequência de caracteres que pode ser lida da
mesma forma da esquerda para a direita e da direita para a esquerda.
● Caso haja múltiplas substrings de mesmo tamanho, retorne qualquer uma delas.
Exemplo de entrada: "babad"
Exemplo de saída: "bab"`` ou "aba"`
"""




def maior_palindromo(string):
    maior = ""
    
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1] and len(substring) > len(maior):
                maior = substring
                
    return maior

string = input("Digite uma string: ")
print(f"A maior substring palindrômica é: {maior_palindromo(string)}")
