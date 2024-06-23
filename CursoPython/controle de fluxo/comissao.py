#publicar um produto com comissão de 10% se for acima de R$20
valor=int(input('digite o valor do seu produto em R$: '))
while valor > 20:
  valor = (valor * 0.10) + valor
  print(f'o valor do produto sera de {valor}')
  break