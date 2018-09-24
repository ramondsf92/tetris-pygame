import pygame
from settings import Settings
from piece import Piece
import game_functions as gf
import random


def run_game():
    pygame.init()
    init = 1000
    start_time = pygame.time.get_ticks()

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Tetris V0.0")
    pieces = []
    piece_group = []
    piece_colors = {'blue': 2, 'cyan': 2, 'green': 4, 'pink': 2, 'purple': 1, 'red': 4, 'yellow': 4}
    for color in piece_colors.keys():
        maximum = piece_colors[color]
        piece = Piece(screen, color, maximum)
        pieces.append(piece)

    piece = random.choice(pieces)
    piece_group.append(piece)
    while True:
        if piece.rect.top == piece.screen_rect.top:
            break
        gf.check_events(piece)
        time = pygame.time.get_ticks() - start_time
        if init < time:
            piece.rect.top += 24
            init += 600
        piece = gf.update_screen(ai_settings, screen, piece, piece_group, piece_colors)
        if not piece:
            break


run_game()
