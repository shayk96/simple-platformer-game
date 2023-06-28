import pygame
from Player import Player
from Platform import Platform
import sys

pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional

HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60


def main():
    FramePerSec = pygame.time.Clock()

    pygame.display.set_caption("Game")
    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    pt1 = Platform()
    p1 = Player(vec)

    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    platforms.add(pt1)
    all_sprites.add(pt1)
    all_sprites.add(p1)

    while True:
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            sys.exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    p1.jump(platforms)

        displaysurface.fill((0, 0, 0))
        p1.move()
        p1.update(platforms)

        for entity in all_sprites:
            displaysurface.blit(entity.surf, entity.rect)

        pygame.display.update()
        FramePerSec.tick(FPS)


if __name__ == '__main__':
    main()


