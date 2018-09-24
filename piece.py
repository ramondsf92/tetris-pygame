import pygame


class Piece:
    def __init__(self, screen, color, maximum):
        self.screen = screen
        self.ini = 1
        self.max = maximum
        self.id = 1
        self.color = color
        self.image = pygame.image.load(f'img/{self.color}_{self.ini}.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        if self.color == 'blue' or self.color == 'purple':
            self.rect.centerx = self.screen_rect.centerx
        else:
            self.rect.centerx = self.screen_rect.centerx + 12
        self.rect.top = self.screen_rect.top + 24
        self.mask = pygame.mask.from_surface(self.image)

    def move_right(self):
        if self.rect.right < self.screen_rect.right:
            self.rect.centerx += 24

    def move_left(self):
        if self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 24

    def move_down(self):
        self.rect.top += 24

    def flip(self):
        self.id += 1
        if self.id <= self.max:
            self.image = pygame.image.load(f'img/{self.color}_{self.id}.bmp')
        else:
            self.image = pygame.image.load(f'img/{self.color}_{self.ini}.bmp')
            self.id = 1
        posx = self.rect.centerx
        posy = self.rect.top
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.top = posy
        self.mask = pygame.mask.from_surface(self.image)
        if self.color != 'purple':
            self.rect.centerx += 12
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right

    def blitme(self):
        self.screen.blit(self.image, self.rect)
