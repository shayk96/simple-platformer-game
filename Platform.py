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
            self.point = False
            self.moving = False
        else:
            self.surf = pygame.Surface((random.randint(50, 100), 12))
            self.surf.fill((0, 255, 0))
            self.rect = self.surf.get_rect(center=(random.randint(0, WIDTH - 10),
                                                   random.randint(0, HEIGHT - 30)))
            self.point = True
            self.moving = True
            self.speed = random.randint(-1, 1)

    def move(self):
        if self.moving:
            self.rect.move_ip(self.speed, 0)
            if self.speed > 0 and self.rect.left > WIDTH:
                self.rect.right = 0
            if self.speed < 0 and self.rect.right < 0:
                self.rect.left = WIDTH



