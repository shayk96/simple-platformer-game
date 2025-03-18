import pygame
import random

# Game constants
HEIGHT = 450
WIDTH = 400


class Platform(pygame.sprite.Sprite):
    """
    Platform class for creating platforms that the player can jump on.

    Attributes:
        surf (Surface): The platform's surface
        rect (Rect): Rectangle for collision detection
        point (bool): Whether the platform awards points when passed
        moving (bool): Whether the platform moves horizontally
        speed (int): Speed of horizontal movement (if moving)
        trampoline (bool): Whether the platform acts as a trampoline
    """

    def __init__(self, color, base=False):
        """
        Initialize a platform.

        Args:
            color (str): Color of the platform
            base (bool): Whether this is the base platform
        """
        super().__init__()

        if base:
            # Base platform is wide red platform at the bottom
            self.surf = pygame.Surface((WIDTH, 20))
            self.surf.fill((255, 0, 0))  # Red color
            self.rect = self.surf.get_rect(center=(WIDTH / 2, HEIGHT - 10))
            self.point = False
            self.moving = False
            self.trampoline = False
        else:
            # Regular platforms are randomly sized and positioned
            self.surf = pygame.Surface((random.randint(50, 100), 12))
            self.surf.fill(color)
            self.rect = self.surf.get_rect(center=(random.randint(0, WIDTH - 10),
                                                   random.randint(0, HEIGHT - 30)))
            self.point = True
            self.moving = True
            self.speed = random.randint(-1, 1)  # Random speed (-1, 0, or 1)
            self.trampoline = random.randint(0, 1)  # 50% chance of being a trampoline

            # Trampoline platforms are pink
            if self.trampoline:
                self.surf.fill("pink")

    def move(self):
        """
        Move the platform horizontally if it's a moving platform.
        Wrap around the screen edges.
        """
        if self.moving:
            self.rect.move_ip(self.speed, 0)
            # Wrap around edges
            if self.speed > 0 and self.rect.left > WIDTH:
                self.rect.right = 0
            if self.speed < 0 and self.rect.right < 0:
                self.rect.left = WIDTH
