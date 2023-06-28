import pygame
from Player import Player
from Platform import Platform
import sys
import random
import time

pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional

HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60
NUM_PLATFORMS = 7
MIN_DISTANCE = 50
MAX_ATTEMPTS = 10


def check(platform, groupies):
    if pygame.sprite.spritecollideany(platform, groupies):
        return False
    else:
        for entity in groupies:
            if entity == platform:
                continue
            if (abs(platform.rect.top - entity.rect.bottom) < MIN_DISTANCE) and (
                    abs(platform.rect.bottom - entity.rect.top) < MIN_DISTANCE):
                return False
        return True


def plat_gen(platforms, all_sprites):
    while len(platforms) < NUM_PLATFORMS:
        width = random.randrange(50, 100)
        p = Platform()

        valid = False
        attempts = 0
        while not valid:
            p = Platform()
            p.rect.center = (random.randrange(0, WIDTH - width),
                             random.randrange(-50, 0))
            valid = check(p, platforms)

            if not valid:
                attempts += 1
                print(attempts)
            if attempts == MAX_ATTEMPTS:
                attempts = 0
                valid = True

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

    for i in range(random.randint(NUM_PLATFORMS, NUM_PLATFORMS + 2)):
        pl = Platform()
        if not check(pl, platforms):
            i -= 1
            continue
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
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    p1.cancel_jump()

        if p1.rect.top > HEIGHT:
            for entity in all_sprites:
                entity.kill()
                time.sleep(1)
                displaysurface.fill((255, 0, 0))
                f = pygame.font.SysFont("Verdana", 50)
                g = f.render("GAME OVER", True, (255, 255, 255))
                displaysurface.blit(g, (10, 10))
                pygame.display.update()
                time.sleep(1)
                pygame.quit()
                sys.exit()

        displaysurface.fill((0, 0, 0))
        f = pygame.font.SysFont("Verdana", 20)
        g = f.render(str(p1.score), True, (123, 255, 0))
        displaysurface.blit(g, (WIDTH / 2, 10))
        p1.update(platforms)
        p1.move()

        for entity in all_sprites:
            displaysurface.blit(entity.surf, entity.rect)

        if p1.rect.top <= HEIGHT / 3:
            p1.pos.y += abs(p1.vel.y)
            for plat in platforms:
                plat.rect.y += abs(p1.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()

        plat_gen(platforms, all_sprites)
        for platform in platforms:
            platform.move()

        pygame.display.update()
        FramePerSec.tick(FPS)


if __name__ == '__main__':
    main()
