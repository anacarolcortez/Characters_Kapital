import random


def get_jogadores():
    try:
        qtde = int(input('Informe o número de jogadores: '))
        if (qtde < 0 or qtde > 5):
            print('A quantidade de jogadores é limitada a 5 pessoas por rodada')
            quit()
    except Exception:
        print('Digite um número inteiro')

    return qtde


def sortear_dominados(numero_jogadores):
    dominados = ['Prof Antunes', 'Dr Rocha', 'Rafinha', 'Seu Pereira', 'Naná', 'Caíque',
                 'Zeca', 'Dona Zilda', 'Cristina', 'Neusa', 'Tonico Malvadeza', 'Emerson']

    print('Jogadores dominados:')

    random.shuffle(dominados)
    for i in range(0, numero_jogadores-1):
        print(dominados[i])


def sortear_dominante():
    dominantes = ['Sr Albuquerque', 'Gen Carvalho',
                  'Nenê Noronha', 'Srta Helena']
    print(
        f'Jogador dominante: {dominantes[random.randrange(0, len(dominantes))]}')


if __name__ == "__main__":
    print('Bem-vinde ao jogo Kapital!')
    try:
        numero_jogadores = get_jogadores()
        sortear_dominante()
        sortear_dominados(numero_jogadores)
    except Exception:
        print('Reinicie o jogo')
