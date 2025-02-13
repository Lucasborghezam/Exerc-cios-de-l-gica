"""
3-Cálculo de Números Perfeitos
Um número perfeito é um número inteiro positivo que é igual à soma de todos os seus
divisores positivos, excluindo ele mesmo. Implemente um programa que verifique se um
número dado é perfeito.
Exemplo de entrada: n = 28
Exemplo de saída: True
"""

def numero_perfeito(numero):
    divisores = []
    contador = 1 

    while contador <= numero // 2:  
        if numero % contador == 0: 
            divisores.append(contador)  
        contador += 1  

  
    print(f"Divisores de {numero}: {divisores}")

    soma_divisores = sum(divisores)
    return soma_divisores == numero  

numero = int(input("Digite um número positivo: "))
resultado = numero_perfeito(numero)
print(f"{numero} é um número perfeito? {resultado}")

