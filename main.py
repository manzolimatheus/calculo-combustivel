from calculo import calculo


def menu():
    # Mensagem de bem-vindo
    print('''
    
    👋 Bem-vindo à calculadora de combustível! 
    
    👥 Raíne Felix & Matheus Manzoli - 3ºDS
    🔗 Github & Behance: /manzolimatheus

    ''')

    # Verificação da distância
    while True:
        try:
            distancia = float(
                input('🚗 Qual a distância que você irá percorrer em km? -> '))
        except ValueError:
            print('⚡ Valor inválido! Tente novamente.')
        else:
            break

    # Verificação do consumo
    while True:
        try:
            consumo = float(input(
                '⛽ Qual o consumo do seu veículo (Apenas valor)? Ex: 10km por litro => 10: -> '))
        except ValueError:
            print('⚡ Valor inválido! Tente novamente.')
        else:
            break

    # Opções de combustível
    print('''
    👉 Escolha uma das opções de combustível abaixo (Digite o número correspondente).

    [1] - Álcool
    [2] - Diesel
    [3] - Gasolina
    ''')

    # Verificação das opções
    while True:
        try:
            tipo_combustivel = int(input('👉 Escolha sua opção: -> '))
        except ValueError:
            print('⚡ Valor inválido! Tente novamente.')
        else:
            break

    if tipo_combustivel == 1:
        calculo.calcular_gasto(distancia, consumo, 4.497)
    elif tipo_combustivel == 2:
        calculo.calcular_gasto(distancia, consumo, 4.616)
    elif tipo_combustivel == 3:
        calculo.calcular_gasto(distancia, consumo, 7.199)
    else:
        print('Valor inválido! Encerrando')


menu()
