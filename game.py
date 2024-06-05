import pygame
import sys
import numpy as np
import random

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0) 
#Player
PLAYER = 1 # Jogador 1 é 'X', Jogador 2 é 'O' ou a máquina

# Função para desenhar o tabuleiro
def draw_board(screen, screen_size):
    screen.fill(WHITE)
    # Linhas verticais
    pygame.draw.line(screen, BLACK, (screen_size // 3, 0), (screen_size // 3, screen_size), 5)
    pygame.draw.line(screen, BLACK, (2 * screen_size // 3, 0), (2 * screen_size // 3, screen_size), 5)
    # Linhas horizontais
    pygame.draw.line(screen, BLACK, (0, screen_size // 3), (screen_size, screen_size // 3), 5)
    pygame.draw.line(screen, BLACK, (0, 2 * screen_size // 3), (screen_size, 2 * screen_size // 3), 5)

# Função para desenhar X ou O no tabuleiro
def draw_markers(board, screen, screen_size):
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                pygame.draw.line(screen, BLACK, (col * screen_size // 3 + 20, row * screen_size // 3 + 20),
                                 (col * screen_size // 3 + screen_size // 3 - 20, row * screen_size // 3 + screen_size // 3 - 20), 5)
                pygame.draw.line(screen, BLACK, (col * screen_size // 3 + screen_size // 3 - 20, row * screen_size // 3 + 20),
                                 (col * screen_size // 3 + 20, row * screen_size // 3 + screen_size // 3 - 20), 5)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, BLACK, (col * screen_size // 3 + screen_size // 6, row * screen_size // 3 + screen_size // 6), screen_size // 6 - 20, 5)

# Função para verificar cliques do mouse e registrar jogadas
def check_mouse_click(board, screen_size):
    global PLAYER
    mouseX, mouseY = pygame.mouse.get_pos()
    clicked_row = mouseY // (screen_size // 3)
    clicked_col = mouseX // (screen_size // 3)

    if board[clicked_row][clicked_col] == 0:
        board[clicked_row][clicked_col] = PLAYER
        if PLAYER == 1:
            PLAYER = 2
        else:
            PLAYER = 1

# Função para a jogada da máquina
def machine_move(board):
    global PLAYER
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == 0]
    if empty_cells:
        move = random.choice(empty_cells)
        board[move[0]][move[1]] = 2
        PLAYER = 1

# Função para verificar condições de vitória
def check_winner(board):
    # Verificar linhas
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != 0:
            return board[row][0]
    # Verificar colunas
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            return board[0][col]
    # Verificar diagonais
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]
    return 0

def main():
# Inicialização do Pygame
    pygame.init()

    # Configuração da Janela
    screen_size = 300
    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption('Tic-Tac-Toe')

    # Inicialização do tabuleiro
    board = np.zeros((3, 3))
    # Loop principal do jogo
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and PLAYER == 1:
                check_mouse_click(board, screen_size)
                winner = check_winner(board)
                if winner != 0:
                    print(f"Jogador {winner} venceu!")
                    running = False

        if PLAYER == 2 and running:
            machine_move(board)
            winner = check_winner(board)
            if winner != 0:
                print(f"Jogador {winner} venceu!")
                running = False

        draw_board(screen, screen_size)
        draw_markers(board,screen, screen_size)
        pygame.display.flip()

    # Encerramento do Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()