def desenha_tabuleiro(simbolos):
    print(' ' + simbolos[0] + '  |  ' + simbolos[1] + '  |  ' + simbolos[2])
    print('________________')
    print(' ' + simbolos[3] + '  |  ' + simbolos[4] + '  |  ' + simbolos[5])
    print('________________')
    print(' ' + simbolos[6] + '  |  ' + simbolos[7] + '  |  ' + simbolos[8])

def verificar_vencedor(simbolos):
    if simbolos[0] == simbolos[1] == simbolos[2] != ' ':
        return simbolos[0]
    if simbolos[3] == simbolos[4] == simbolos[5] != ' ':
        return simbolos[3]
    if simbolos[6] == simbolos[7] == simbolos[8] != ' ':
        return simbolos[6]
    if simbolos[0] == simbolos[3] == simbolos[6] != ' ':
        return simbolos[0]
    if simbolos[1] == simbolos[4] == simbolos[7] != ' ':
        return simbolos[1]
    if simbolos[2] == simbolos[5] == simbolos[8] != ' ':
        return simbolos[2]
    if simbolos[0] == simbolos[4] == simbolos[8] != ' ':
        return simbolos[0]
    if simbolos[2] == simbolos[4] == simbolos[6] != ' ':
        return simbolos[2]
    return ' '

def jogar_velha():
    print('Escolha o nome do jogador 1')
    nome_jogador1 = input()
    print('-----------------------------')
    print('Escolha o nome do jogador 2')
    nome_jogador2 = input()
    print('\n' * 30)

    continuar_jogo = True
    while continuar_jogo:
        simbolos = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        desenha_tabuleiro(simbolos)
        jogador_atual = nome_jogador1
        simbolo_atual = 'X'
        for _ in range(9):
            print(jogador_atual + ', escolha a posição da sua jogada')
            jogada = int(input())

            if simbolos[jogada - 1] != ' ':
                print("Essa posição já está ocupada. Escolha outra.")
                continue

            print('\n' * 130)
            simbolos[jogada - 1] = simbolo_atual
            desenha_tabuleiro(simbolos)
            print('______________________________________')

            vencedor = verificar_vencedor(simbolos)

            if vencedor == 'X':
                print(nome_jogador1 + ' ganhou!')
                break
            elif vencedor == 'O':
                print(nome_jogador2 + ' ganhou!')
                break

            jogador_atual = nome_jogador2 if jogador_atual == nome_jogador1 else nome_jogador1
            simbolo_atual = 'O' if simbolo_atual == 'X' else 'X'
        else:
            if vencedor == ' ':
                print('Velha')

        print('______________________________________')
        print('Deseja jogar novamente?')
        print('1-> Sim')
        print('2-> Não')
        resp = int(input())
        print('\n' * 130)
        if resp == 1:
            continuar_jogo = True
        elif resp == 2:
            continuar_jogo = False
    print('Jogo encerrado!')

jogar_velha()
