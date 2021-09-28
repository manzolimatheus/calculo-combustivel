def teste(recebeu, esperado):
    if recebeu != esperado:
        print(f'❌ Teste fracassou! Esperava: {esperado} | Recebeu: {recebeu}')
    else:
        print(f'✅ Teste passou! Esperava: {esperado} | Recebeu: {recebeu}')
