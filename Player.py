import pygame

HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12

VELOCITY = -15
MIN_VELOCITY = -3


class Player(pygame.sprite.Sprite):

    def __init__(self, vec):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect(center=(10, 420))
        self.vec = vec

        self.pos = vec((10, 385))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.jumping = False

    def move(self):
        self.acc = self.vec(0, 0.5)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[pygame.K_RIGHT]:
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

    def update(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and self.vel.y > 0 and self.pos.y < hits[0].rect.bottom:
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0
            self.jumping = False

    def jump(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = VELOCITY

    def cancel_jump(self):
        if self.jumping and self.vel.y < MIN_VELOCITY:
            self.vel.y = MIN_VELOCITY

