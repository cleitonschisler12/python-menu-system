while True:
    print('1 - Ver mensagem\n2 - Calcular soma\n3 - Sair')
    select = input('Digite o número da opção desejada:')
    
    if not select.isnumeric():
           print('Digite apenas números.')
           continue

    select = int(select)

    if select == 1:
            print('Você é capaz, acredite em si mesmo!')
    elif select == 2:
            num1 = int(input('Digite o primeiro número:'))
            num2 = int(input('Digite o segundo número:'))
            resultado = num1 + num2
            print(f'Resultado da soma de {num1} e {num2} é = {resultado}')
    elif select == 3:
            print('Encerrando o sistema. . .')
            break
    else:
            print('Opção inválida. Tente novamente digitando o número de uma das opções.')