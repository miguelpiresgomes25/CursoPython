#enviar um email com os detalhes da compra online (maximo 3 tentativas) para compras #confirmadas
compra_confirmada = False
dados_da_compra = 'compra no valor de 10.000 e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_da_compra)
        print('detalhes finais enviados por email')
        break
    else:
        print('falha na compra')
        break