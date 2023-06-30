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
    for row in board:
        for column in row:
            print(column, end=' ')
        
        print()

# Essa função checa se a posição escolhida está vazia
def check_board(board: np.ndarray, move: str):
    # Transforma a string de entrada em uma lista de inteiros
    move = [int(position) for position in move.split(' ')]

    # Checa se a posição escolhida está vazia
    if board[move[0], move[1]] == 0:
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
        board[move[0], move[1]] = 1
    # Se draw == 1, o jogador X fez a jogada
    elif draw == 1:
        # Atualiza o tabuleiro com a jogada do jogador X como um valor inteiro -1
        board[move[0], move[1]] = -1
    
    return board

# Essa função checa se há um vencedor
def check_winner(board: np.ndarray, names: List[str]):
    # Checa as linhas do tabuleiro
    for row in board:
        # Se a soma de uma linha for 3, o jogador O venceu
        if sum(row) == 3:
            print_board(board)
            print(f"\nO jogador {names[0]} venceu!")
            return True
        # Se a soma de uma linha for -3, o jogador X venceu
        elif sum(row) == -3:
            print_board(board)
            print(f"\nO jogador {names[1]} venceu!")
            return True

    # Transpõe o tabuleiro para checar as colunas
    for column in board.T:
        # Se a soma de uma coluna for 3, o jogador O venceu
        if sum(column) == 3:
            print_board(board)
            print(f"\nO jogador {names[0]} venceu!")
            return True
        # Se a soma de uma coluna for -3, o jogador X venceu
        elif sum(column) == -3:
            print_board(board)
            print(f"\nO jogador {names[1]} venceu!")
            return True

    # Checa as diagonais do tabuleiro
    diagonal = board.diagonal()

    # Se a soma de uma diagonal for 3, o jogador O venceu
    if sum(diagonal) == 3:
        print_board(board)
        print(f"\nO jogador {names[0]} venceu!")
        return True
    # Se a soma de uma diagonal for -3, o jogador X venceu
    elif sum(diagonal) == -3:
        print_board(board)
        print(f"\nO jogador {names[1]} venceu!")
        return True
    
    # Checa a diagonal secundária do tabuleiro
    diagonal = np.fliplr(board).diagonal()

    # Se a soma da diagonal secundária for 3, o jogador O venceu
    if sum(diagonal) == 3:
        print_board(board)
        print(f"\nO jogador {names[0]} venceu!")
        return True
    # Se a soma da diagonal secundária for -3, o jogador X venceu
    elif sum(diagonal) == -3:
        print_board(board)
        print(f"\nO jogador {names[1]} venceu!")
        return True

    # Se não houver vencedor e o tabuleiro estiver cheio, deu velha
    if np.count_nonzero(board) == 9:
        print_board(board)
        print("\nDeu velha!")
        return True

    return False

# Essa função executa o jogo
def game(names: List[str]):
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
            print(f"\nO jogador {player} começa o jogo!\n")
        else:
            print(f"\nÉ a vez de {player}!\n")
        
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
        if check_winner(board, names):
            break

def main():
    print("Seja bem vindo ao jogo da velha!\n")

    # Pede os nomes dos jogadores
    names = []
    names.append(input('Digite o nome do primeiro jogador (O): '))
    names.append(input('Digite o nome do segundo jogador (X): '))
    
    # Inicia o jogo
    game(names)

if __name__ == '__main__':
    main()