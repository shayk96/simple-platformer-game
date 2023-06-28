import pygame
import random

HEIGHT = 450
WIDTH = 400


class Platform(pygame.sprite.Sprite):
    def __init__(self, base=False):
        super().__init__()
        if base:
            self.surf = pygame.Surface((WIDTH, 20))
            self.surf.fill((255, 0, 0))
            self.rect = self.surf.get_rect(center=(WIDTH / 2, HEIGHT - 10))
        else:
            self.surf = pygame.Surface((random.randint(50, 100), 12))
            self.surf.fill((0, 255, 0))
            self.rect = self.surf.get_rect(center=(random.randint(0, WIDTH - 10),
                                                   random.randint(0, HEIGHT - 30)))
