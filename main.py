import pygame
from Player import Player
from Platform import Platform
import sys
import random

pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional

HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60


def plat_gen(platforms, all_sprites):
    while len(platforms) < 7:
        width = random.randrange(50, 100)
        p = Platform()
        p.rect.center = (random.randrange(0, WIDTH - width),
                         random.randrange(-50, 0))
        platforms.add(p)
        all_sprites.add(p)


def main():
    FramePerSec = pygame.time.Clock()

    pygame.display.set_caption("Game")
    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    p1 = Player(vec)
    pt1 = Platform(base=True)

    all_sprites, platforms = pygame.sprite.Group(), pygame.sprite.Group()
    all_sprites.add(pt1)
    platforms.add(pt1)
    all_sprites.add(p1)

    for x in range(random.randint(5, 6)):
        pl = Platform()
        platforms.add(pl)
        all_sprites.add(pl)

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

        if p1.rect.top <= HEIGHT / 3:
            p1.pos.y += abs(p1.vel.y)
            for plat in platforms:
                plat.rect.y += abs(p1.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
        if p1.rect.top >= HEIGHT:
            sys.exit()

        plat_gen(platforms, all_sprites)

        pygame.display.update()
        FramePerSec.tick(FPS)


if __name__ == '__main__':
    main()
