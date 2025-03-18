import pygame

# Game constants
HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12

VELOCITY = -15  # Initial jump velocity (negative because y increases downward)
MIN_VELOCITY = -3  # Minimum jump velocity when jump is canceled


class Player(pygame.sprite.Sprite):
    """
    Player class for the game character.

    Attributes:
        surf (Surface): The player's surface
        rect (Rect): Rectangle for collision detection
        vec (Vector2): Vector class for physics calculations
        score (int): Player's score
        pos (Vector2): Position vector
        vel (Vector2): Velocity vector
        acc (Vector2): Acceleration vector
        jumping (bool): Whether the player is currently jumping
    """

    def __init__(self, vec):
        """
        Initialize the player.

        Args:
            vec (Vector2): Pygame vector class for physics calculations
        """
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128, 255, 40))  # Green color
        self.rect = self.surf.get_rect(center=(10, 420))
        self.vec = vec
        self.score = 0

        self.pos = vec((10, 385))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.jumping = False

    def move(self):
        """
        Update player position based on keyboard input and physics.
        Applies gravity, handles left/right movement, and implements
        screen wrapping.
        """
        # Apply gravity
        self.acc = self.vec(0, 0.5)

        # Check keyboard input for movement
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[pygame.K_RIGHT]:
            self.acc.x = ACC

        # Apply friction to slow down horizontal movement
        self.acc.x += self.vel.x * FRIC

        # Update velocity and position using physics equations
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # Wrap around screen edges
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        # Update rectangle position
        self.rect.midbottom = self.pos

    def update(self, platforms):
        """
        Handle collision with platforms.

        Args:
            platforms: Group of platform sprites
        """
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and self.vel.y > 0 and self.pos.y < hits[0].rect.bottom:
            # If player is on a moving platform, inherit its speed
            if hits[0].moving and hits[0].speed:
                self.acc.x = hits[0].speed
                self.pos += self.vel + self.acc

            # Place player on top of platform
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0
            self.jumping = False

            # If platform is a trampoline, apply super jump
            if hits[0].trampoline:
                self.vel.y = VELOCITY * 2

    def jump(self, platforms):
        """
        Make the player jump if they're on a platform.

        Args:
            platforms: Group of platform sprites
        """
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = VELOCITY

    def cancel_jump(self):
        """
        Cancel the jump if the space key is released early.
        Limits the jump height by setting velocity to MIN_VELOCITY.
        """
        if self.jumping and self.vel.y < MIN_VELOCITY:
            self.vel.y = MIN_VELOCITY
