""""
metodos para string
"""
mensagem = 'eu gosto de comida Brasieira'
#tudo em maiusculo
print(mensagem.upper())
#tudo em minusculo
print(mensagem.lower())
#função de achar a posição de uma letra ou a palavra
print(mensagem.find('g'))
#Funçao de colocar a primera letra maiscula 
print(mensagem.capitalize())
#função de colocar a primeira letra de cada palavra maiscula
print(mensagem.title())
#função de substituir uma palavra por outra
print(mensagem.replace('a', 'e'))
#função de remover espaços em branco antes da primeira letra
print(mensagem.strip())