import sys
import pygame
import random
from piece import Piece

def check_events(piece):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                piece.move_right()
            if event.key == pygame.K_LEFT:
                piece.move_left()
            if event.key == pygame.K_DOWN:
                piece.move_down()
            if event.key == pygame.K_SPACE:
                piece.flip()
        '''
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                piece.moving_right = False
            if event.key == pygame.K_LEFT:
                piece.moving_left = False
        '''


def update_screen(ai_settings, screen, piece, piece_group, piece_colors):
    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    collide = False
    for peca in piece_group:
        peca.blitme()
    for p in piece_group:
        if pygame.sprite.collide_rect(piece, p) and piece != p:
            collide = True
            piece.rect.top -= 24
            break
    if piece.rect.bottom == piece.screen_rect.bottom or collide:
        if piece.rect.top == piece.screen_rect.top + 24:
            return 0
        cor, maximum = random.choice(list(piece_colors.items()))
        piece = Piece(screen, cor, maximum)
        piece_group.append(piece)
    # Make the most recently drawn screen visible
    pygame.display.flip()
    return piece
