import pygame
from Player import Player
from Platform import Platform
import sys
import random
import time

pygame.init()  # Initialize pygame
vec = pygame.math.Vector2  # 2D vector for physics calculations

# Game constants
HEIGHT = 450  # Window height in pixels
WIDTH = 400  # Window width in pixels
ACC = 0.5  # Player acceleration
FRIC = -0.12  # Friction coefficient (slows down the player)
FPS = 60  # Frames per second
NUM_PLATFORMS = 7  # Minimum number of platforms
MIN_DISTANCE = 50  # Minimum distance between platforms
MAX_ATTEMPTS = 10  # Maximum attempts to place a platform
COLORS = ["green", "blue", "yellow", "purple"]  # Available platform colors


def check(platform, groupies):
    """
    Check if a platform can be placed without overlapping other platforms.

    Args:
        platform: The platform to check
        groupies: Group of existing platforms

    Returns:
        bool: True if platform can be placed, False otherwise
    """
    # Check if platform collides with any existing platform
    if pygame.sprite.spritecollideany(platform, groupies):
        return False
    else:
        # Check if platform is too close to any existing platform
        for entity in groupies:
            if entity == platform:
                continue
            if (abs(platform.rect.top - entity.rect.bottom) < MIN_DISTANCE) and (
                    abs(platform.rect.bottom - entity.rect.top) < MIN_DISTANCE):
                return False
        return True


def plat_gen(platforms, all_sprites, color):
    """
    Generate new platforms at the top of the screen.

    Args:
        platforms: Group of platform sprites
        all_sprites: Group of all sprites
        color: Color for the new platforms
    """
    while len(platforms) < NUM_PLATFORMS:
        width = random.randrange(50, 100)
        p = Platform(color)

        valid = False
        attempts = 0
        # Try to place platform in a valid position
        while not valid:
            p = Platform(color)
            p.rect.center = (random.randrange(0, WIDTH - width),
                             random.randrange(-50, 0))  # Above the screen
            valid = check(p, platforms)

            if not valid:
                attempts += 1
            # If max attempts reached, force placement
            if attempts == MAX_ATTEMPTS:
                attempts = 0
                valid = True

        platforms.add(p)
        all_sprites.add(p)


def main():
    """
    Main game function. Handles game initialization, game loop, and events.
    """
    # Set up the game clock
    FramePerSec = pygame.time.Clock()

    # Set up the game window
    pygame.display.set_caption("Game")
    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))

    # Create player
    p1 = Player(vec)

    # Select random color for platforms
    color = COLORS[random.randint(0, len(COLORS) - 1)]

    # Create base platform
    pt1 = Platform(color, base=True)

    # Create sprite groups
    all_sprites, platforms = pygame.sprite.Group(), pygame.sprite.Group()
    all_sprites.add(pt1)
    platforms.add(pt1)
    all_sprites.add(p1)

    # Generate initial platforms
    for i in range(random.randint(NUM_PLATFORMS, NUM_PLATFORMS + 2)):
        pl = Platform(color)
        if not check(pl, platforms):
            i -= 1  # Retry if platform can't be placed
            continue
        platforms.add(pl)
        all_sprites.add(pl)

    # Main game loop
    while True:
        # Change platform color every 20 points
        if not (p1.score % 20) and p1.score != 0:
            color = COLORS[random.randint(0, len(COLORS) - 1)]

        # Exit game if Escape is pressed
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            sys.exit()

        # Handle events
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

        # Check if player has fallen off the screen (game over)
        if p1.rect.top > HEIGHT:
            for entity in all_sprites:
                entity.kill()
                time.sleep(1)
                displaysurface.fill((255, 0, 0))  # Red background
                f = pygame.font.SysFont("Verdana", 50)
                g = f.render("GAME OVER", True, (255, 255, 255))  # White text
                displaysurface.blit(g, (10, 10))
                pygame.display.update()
                time.sleep(1)
                pygame.quit()
                sys.exit()

        # Clear the screen
        displaysurface.fill((0, 0, 0))  # Black background

        # Draw score
        f = pygame.font.SysFont("Verdana", 20)
        g = f.render(str(p1.score), True, (123, 255, 0))  # Green text
        displaysurface.blit(g, (WIDTH / 2, 10))

        # Update player
        p1.update(platforms)
        p1.move()

        # Draw all sprites
        for entity in all_sprites:
            displaysurface.blit(entity.surf, entity.rect)

        # Camera system - when player reaches top third of screen
        if p1.rect.top <= HEIGHT / 3:
            p1.pos.y += abs(p1.vel.y)  # Move player down
            for plat in platforms:
                plat.rect.y += abs(p1.vel.y)  # Move platforms down
                if plat.rect.top >= HEIGHT:
                    p1.score += 1  # Increase score when platform goes off screen
                    plat.kill()  # Remove platform

        # Generate new platforms as needed
        plat_gen(platforms, all_sprites, color)

        # Move platforms
        for platform in platforms:
            platform.move()

        # Update display and maintain framerate
        pygame.display.update()
        FramePerSec.tick(FPS)


# Run the game if this script is executed directly
if __name__ == '__main__':
    main()
