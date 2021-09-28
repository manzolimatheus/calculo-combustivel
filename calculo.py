from teste import teste

class calculo:
    # Cálculo de gasto para usuário comum
    def calcular_gasto(distancia, consumo, preco):
        if distancia <= 0 or consumo <= 0 or preco <= 0:
            print('⚡ Não posso realizar o cálculo com valores igual ou abaixo de 0!')
        else:
            gasto = (distancia / consumo) * preco
            print(f'💰 O custo total da viagem será de R${round(gasto, 2)}')

    # Cálculo de gasto para testes
    def calcular_gasto_teste(distancia, consumo, preco, esperado):
        if distancia <= 0 or consumo <= 0 or preco <= 0:
            print('⚡ Não posso realizar o cálculo com valores igual ou abaixo de 0!')
        else:
            gasto = (distancia / consumo) * preco
            teste(gasto, esperado)
