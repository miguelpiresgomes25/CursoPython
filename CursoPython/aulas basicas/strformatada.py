""""
aula string formatada 
"""
#string normal
nome = 'Miguel'
sobrenome = 'Pires' 
curso = 'programacao'
texto = nome +' ' + sobrenome + ' e estudante de ' + curso
print(texto)
#string formatada
texto2= f'{nome} {sobrenome} e um estudante de {curso}'
print(texto2)


# Miguel Pires e um estudante de programação