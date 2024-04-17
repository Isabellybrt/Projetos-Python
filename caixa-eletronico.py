saldo = 0.0
repete = True
while repete: 
    
    print('Bem vindo ao caixa eletrônico!')
    print('Qual operação deseja fazer?')
    print('1-> Saldo')
    print('2-> Depósito')
    print('3-> Saque')
    operacao = int(input())
    
    if operacao == 1:
         print('Você tem R$', saldo)
         print('------------------------------------------')
         
    if operacao == 2:
         print('Qual o valor do depósito?')
         valor = float(input())
         saldo += valor
         print('Seu depósito foi realizado')
         print('------------------------------------------')
    
    if operacao == 3:
        print('Quanto você deseja sacar?')
        valor = float(input())
        if valor > 0:
            if saldo < valor:
                print('Operação indisponível')
                print('------------------------------------------')
            else:
                saldo -= valor
                print('Saque realizado com sucesso')
                print('------------------------------------------')
        else:
            print('Operação indisponível!')
    
    print('Deseja realizar outra operação?')
    print('1-> Sim')
    print('2-> Não')
    resposta = int(input())

    if resposta != 1:
        repete = False
        print('------------------------------------------')
    
    print('\n'*50)
    
print('Operação encerrada. Obrigado! Até a próxima.')        
