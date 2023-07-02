# Autor: Carlos Henrique Gonçalves Batista
# Esse programa implementa o jogo da velha em Python

# Bibliotecas necessárias
import numpy as np
from typing import List
from itertools import cycle

# Essa função sorteia quem começa o jogo
def game_start(names: List[str]):
    # Define uma semente aleatória para que os resultados sejam "mais aleatórios"
    np.random.seed()

    # Sorteia quem começa o jogo
    first = np.random.choice([0, 1])

    return first

# Essa função imprime o tabuleiro
def print_board(board: np.ndarray):
    for index, row in enumerate(board):
        print(index + 1, end=' ')
        for column in row:
            # Se o valor da posição for 0, imprime um espaço vazio
            if column == 0:
                print("[ ]", end=' ')
            # Se o valor da posição for 1, imprime um O
            elif column == 1:
                print("[O]", end=' ')
            # Se o valor da posição for -1, imprime um X
            elif column == -1:
                print("[X]", end=' ')
        
        print()
    
    print("   1   2   3")

# Essa função checa se a posição escolhida está vazia
def check_board(board: np.ndarray, move: str):
    # Transforma a string de entrada em uma lista de inteiros
    move = [int(position) for position in move.split(' ')]

    # Checa se a posição escolhida está vazia
    if board[move[0] - 1, move[1] - 1] == 0:
        return True
    else:
        return False

# Essa função atualiza o tabuleiro
def update_board(board: np.ndarray, move: str, draw: int):
    # Transforma a string de entrada em uma lista de inteiros
    move = [int(position) for position in move.split(' ')]

    # Se draw == 0, o jogador O fez a jogada
    if draw == 0:
        # Atualiza o tabuleiro com a jogada do jogador O como um valor inteiro 1
        board[move[0] - 1, move[1] - 1] = 1
    # Se draw == 1, o jogador X fez a jogada
    elif draw == 1:
        # Atualiza o tabuleiro com a jogada do jogador X como um valor inteiro -1
        board[move[0] - 1, move[1] - 1] = -1
    
    return board

# Essa função checa se há um vencedor
def check_winner(board: np.ndarray, names: List[str]):
    # Checa as linhas do tabuleiro
    for row in board:
        # Se a soma de uma linha for 3, o jogador O venceu
        if sum(row) == 3:
            return (True, names[0])
        # Se a soma de uma linha for -3, o jogador X venceu
        elif sum(row) == -3:
            return (True, names[1])

    # Transpõe o tabuleiro para checar as colunas
    for column in board.T:
        # Se a soma de uma coluna for 3, o jogador O venceu
        if sum(column) == 3:
            return (True, names[0])
        # Se a soma de uma coluna for -3, o jogador X venceu
        elif sum(column) == -3:
            return (True, names[1])

    # Checa as diagonais do tabuleiro
    diagonal = board.diagonal()

    # Se a soma de uma diagonal for 3, o jogador O venceu
    if sum(diagonal) == 3:
        return (True, names[0])
    # Se a soma de uma diagonal for -3, o jogador X venceu
    elif sum(diagonal) == -3:
        return (True, names[1])
    
    # Checa a diagonal secundária do tabuleiro
    diagonal = np.fliplr(board).diagonal()

    # Se a soma da diagonal secundária for 3, o jogador O venceu
    if sum(diagonal) == 3:
        return (True, names[0])
    # Se a soma da diagonal secundária for -3, o jogador X venceu
    elif sum(diagonal) == -3:
        return (True, names[1])

    # Se não houver vencedor e o tabuleiro estiver cheio, deu velha
    if np.count_nonzero(board) == 9:
        return (True, "Velha")

    return (False, "Nobody")

# Essa função define a estratégia de jogada do BOT
def strategy_move(board: np.ndarray, number_of_moves: int):
    # Se for a primeira jogada do BOT, ele joga ou no centro ou em um canto de esquina aleatório
    if number_of_moves in [0, 1]:
        if check_board(board, "2 2"):
            # Se a posição central estiver vazia, o BOT joga nela
            return "2 2"
        else:
            # Se a posição central estiver ocupada, o BOT joga em um canto de esquina aleatório
            np.random.seed()
            moves = ["1 1", "1 3", "3 1", "3 3"]

            return np.random.choice(moves)
    
    # Se o BOT tiver duas marcações em uma linha, ele joga na posição vazia para ganhar
    # Senão, se o jogador tiver duas marcações em uma linha, ele joga na posição vazia para bloquear
    for i, row in enumerate(board):
        if sum(row) == -2:
            for j, column in enumerate(row):
                if column == 0:
                    return f"{i + 1} {j + 1}"
        elif sum(row) == 2:
            for j, column in enumerate(row):
                if column == 0:
                    return f"{i + 1} {j + 1}"
    
    # Se o BOT tiver duas marcações em uma coluna, ele joga na posição vazia para ganhar
    # Senão, se o jogador tiver duas marcações em uma coluna, ele joga na posição vazia para bloquear
    for i, column in enumerate(board.T):
        if sum(column) == -2:
            for j, row in enumerate(column):
                if row == 0:
                    return f"{j + 1} {i + 1}"
        elif sum(column) == 2:
            for j, row in enumerate(column):
                if row == 0:
                    return f"{j + 1} {i + 1}"
    
    # Se o BOT tiver duas marcações em uma diagonal, ele joga na posição vazia para ganhar
    # Senão, se o jogador tiver duas marcações em uma diagonal, ele joga na posição vazia para bloquear
    diagonal = board.diagonal()
    if sum(diagonal) == -2:
        for i, row in enumerate(diagonal):
            if row == 0:
                return f"{i + 1} {i + 1}"
    elif sum(diagonal) == 2:
        for i, row in enumerate(diagonal):
            if row == 0:
                return f"{i + 1} {i + 1}"

    # Se o BOT tiver duas marcações em uma diagonal secundária, ele joga na posição vazia para ganhar
    # Senão, se o jogador tiver duas marcações em uma diagonal secundária, ele joga na posição vazia para bloquear
    secondary_diagonal = np.fliplr(board).diagonal()
    if sum(secondary_diagonal) == -2:
        for i, row in enumerate(secondary_diagonal):
            if row == 0:
                return f"{i + 1} {3 - i}"
    elif sum(secondary_diagonal) == 2:
        for i, row in enumerate(secondary_diagonal):
            if row == 0:
                return f"{i + 1} {3 - i}"
    
    # Se acontecer uma posição parecida com o tabuleiro abaixo, ele impede o jogador de ganhar
    # [ ] [O] [ ]
    # [ ] [X] [ ]
    # [ ] [ ] [O]
    if board[2, 0] == 1:
        if board[0, 1] == 1:
            if check_board(board, "1 1"):
                return "1 1"
        elif board[1, 2] == 1:
            if check_board(board, "3 1"):
                return "3 3"
    elif board[0, 2] == 1:
        if board[2, 1] == 1:
            if check_board(board, "3 3"):
                return "3 3"
        elif board[1, 0] == 1:
            if check_board(board, "1 3"):
                return "1 1"
    elif board[0, 0] == 1:
        if board[2, 1] == 1:
            if check_board(board, "3 1"):
                return "3 1"
        elif board[1, 2] == 1:
            if check_board(board, "1 3"):
                return "1 3"
    elif board[2, 2] == 1:
        if board[0, 1] == 1:
            if check_board(board, "1 3"):
                return "1 3"
        elif board[1, 0] == 1:
            if check_board(board, "3 1"):
                return "3 1"

    # Se acontecer uma posição parecida com o tabuleiro abaixo, ele impede o jogador de ganhar
    # [ ] [O] [ ]
    # [ ] [X] [O]
    # [ ] [ ] [ ]
    if board[0, 1] == 1:
        if board[1, 2] == 1:
            np.random.seed()
            moves = np.array(["1 1", "3 3", "1 3"])
            np.random.shuffle(moves)
            
            for move in moves:
                if check_board(board, move):
                    return move
        elif board[1, 0] == 1:
            np.random.seed()
            moves = ["1 3", "3 1", "1 1"]
            np.random.shuffle(moves)
            
            for move in moves:
                if check_board(board, move):
                    return move
    elif board[2, 1] == 1:
        if board[1, 0] == 1:
            np.random.seed()
            moves = ["3 3", "1 1", "3 1"]
            np.random.shuffle(moves)
            
            for move in moves:
                if check_board(board, move):
                    return move
        elif board[1, 2] == 1:
            np.random.seed()
            moves = ["3 1", "1 3", "3 3"]
            np.random.shuffle(moves)
            
            for move in moves:
                if check_board(board, move):
                    return move
    
    # Se acontecer uma posição parecida com o tabuleiro abaixo, ele impede o jogador de ganhar
    # [ ] [ ] [O]
    # [ ] [O] [ ]
    # [X] [ ] [ ]
    if board[1, 1] == 1:
        corners = board[0, 0] == 1 or board[0, 2] == 1 or board[2, 0] == 1 or board[2, 2] == 1
        if corners:
            np.random.seed()
            moves = ["1 1", "1 3", "3 1", "3 3"]
            np.random.shuffle(moves)
            
            for move in moves:
                if check_board(board, move):
                    return move
    
    # Se acontecer uma posição parecida com o tabuleiro abaixo, ele joga para ganhar
    # [ ] [ ] [X]
    # [ ] [X] [ ]
    # [O] [O] [ ]
    if board[1, 1] == -1:
        if board[0, 0] == -1 or board[2, 2] == -1:
            np.random.seed()
            moves = ["1 3", "3 1"]
            np.random.shuffle(moves)
            
            for move in moves:
                if check_board(board, move):
                    return move
        elif board[0, 2] == -1 or board[2, 0] == -1:
            np.random.seed()
            moves = ["1 1", "3 3"]
            np.random.shuffle(moves)
            
            for move in moves:
                if check_board(board, move):
                    return move

    
    # Se houver uma linha com uma marcação do BOT e duas posições vazias, ele joga na posição vazia
    for i, row in enumerate(board):
        if sum(row) == -1:
            for j, column in enumerate(row):
                if column == 0:
                    return f"{i + 1} {j + 1}"
    
    # Se houver uma coluna com uma marcação do BOT e duas posições vazias, ele joga na posição vazia
    for i, column in enumerate(board.T):
        if sum(column) == -1:
            for j, row in enumerate(column):
                if row == 0:
                    return f"{j + 1} {i + 1}"
    
    # Se a diagonal com uma marcação do BOT e duas posições vazias, ele joga na posição vazia
    if sum(diagonal) == -1:
        for i, row in enumerate(diagonal):
            if row == 0:
                return f"{i + 1} {i + 1}"
    
    # Se a diagonal secundária com uma marcação do BOT e duas posições vazias, ele joga na posição vazia
    if sum(secondary_diagonal) == -1:
        for i, row in enumerate(secondary_diagonal):
            if row == 0:
                return f"{i + 1} {3 - i}"
            
    # Se não atender nenhuma condição acima, joga aleatoriamente
    # Pega as posições vazias do tabuleiro
    indices = np.argwhere(board == 0)

    # Escolhe uma posição aleatória
    np.random.seed()
    i, j = np.random.choice(indices)

    # Retorna a posição escolhida
    return f"{i + 1} {j + 1}"

# Essa função retorna a jogada do BOT
def bot_move(board: np.ndarray, number_of_moves: int):
    # Verifica se o tabuleiro está vazio
    if np.all(board == 0):
        # Se estiver vazio, joga aleatoriamente
        np.random.seed()
        i, j = np.random.randint(3, size=2)

        return f"{i + 1} {j + 1}"
    else:
        # Se não estiver vazio, joga de acordo com a estratégia
        return strategy_move(board, number_of_moves)

# Essa função executa o jogo
def game(names: List[str], versus: str):
    # Sorteia quem começa o jogo
    first = game_start(names)

    # Cria um tabuleiro vazio
    board = np.zeros((3,3), dtype=int)

    # Cria um iterador para alternar entre os jogadores
    players = [names[first], names[1 - first]]
    players = cycle(players)

    # Inicializa o número de jogadas e o jogador que vai jogar
    number_of_moves = 0
    draw = first
    
    # Enquanto não houver vencedor, o jogo continua
    for player in players:
        # Se for a primeira jogada, muda a mensagem
        if number_of_moves == 0:
            # Se o jogador for o BOT, muda a mensagem
            if player == "BOT" and versus == "bot":
                print("\nO BOT começa o jogo!")
            else:
                print(f"\nO jogador {player} começa o jogo!\n")
        elif not (versus == "bot" and player == "BOT"):
            print(f"\nÉ a vez de {player}!\n")
        
        if player == "BOT" and versus == "bot":
            # Jogada do BOT
            move = bot_move(board, number_of_moves)

            # Atualiza o tabuleiro com a jogada do BOT
            board = update_board(board, move, draw)
        else:
            # Imprime o tabuleiro
            print_board(board)
            # Pede as coordenadas da jogada
            move = input("\nSelecione as coordenadas da jogada (linha, coluna) [EX: 1 2]: ")

            # Enquanto a jogada não for válida, pede novas coordenadas
            while True:
                try:
                    if check_board(board, move):
                        pass
                    else:
                        move = input("\nEssa posição já foi ocupada! Selecione outra: ")
                        continue

                    board = update_board(board, move, draw)
                except:
                    move = input("\nCoordenadas inválidas! Selecione outra: ")
                    continue

                break

        # Atualiza o número de jogadas e o jogador que vai jogar
        number_of_moves += 1
        draw = 1 - draw

        # Checa se há um vencedor
        winner, who = check_winner(board, names)
        if winner:
            print()
            print_board(board)

            # Imprime o vencedor
            if who != "velha":
                print(f"\nO jogador {who} venceu!")
            else:
                print("\nDeu velha!")

            break

def main():
    print("Seja bem vindo ao jogo da velha!\n")

    match int(input("Digite [1] para jogar contra o bot ou [2] para jogar contra outro jogador: ")):
        case 1:
            # Pede o nome do jogador
            name = input("\nDigite o seu nome: ")

            # Executa o jogo contra o bot
            game([name, 'BOT'], 'bot')
        case 2:
            # Pede os nomes dos jogadores
            names = []
            names.append(input('\nDigite o nome do primeiro jogador (O): '))
            names.append(input('Digite o nome do segundo jogador (X): '))

            # Executa o jogo contra outro jogador
            game(names, 'player')

if __name__ == '__main__':
    main()