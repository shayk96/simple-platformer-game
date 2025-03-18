# simple platformer game
A simple platformer game i did in order to familiarise myself with pygame.
in order to run the game:
1. download the code
2. install pygame
3. run main

# Platform Jumper Game Documentation

## Overview

This is a simple 2D platformer game built using Pygame where the player controls a character that jumps on platforms to gain height and score points. The game features:

- A player character that can move left and right and jump
- Randomly generated platforms of different colors
- Moving platforms
- Trampoline platforms (pink) that make the player jump higher
- Score tracking
- Game over when the player falls off the screen

## File Structure

The game is organized into three Python files:
1. `main.py` - Contains the game loop and main functionality
2. `Platform.py` - Defines the Platform class
3. `Player.py` - Defines the Player class

## Game Mechanics

### Player

The player is represented by a green square that can:
- Move left and right using the arrow keys
- Jump by pressing the space bar
- Control jump height by releasing the space bar early
- Wrap around the screen horizontally

The player's movement is physics-based, with velocity and acceleration vectors that create smooth movement. Gravity constantly pulls the player downward.

### Platforms

Platforms come in several varieties:
- Base platform: A red platform at the bottom of the screen that doesn't move
- Regular platforms: Randomly colored platforms (green, blue, yellow, or purple)
- Moving platforms: Regular platforms that move horizontally across the screen
- Trampoline platforms: Pink platforms that provide a higher jump

Platforms are randomly generated at the top of the screen as the player ascends. They are placed with minimum distance constraints to ensure the game remains playable.

### Camera System

The game uses a "moving camera" system:
- When the player reaches the top third of the screen, instead of the player moving upward, the platforms move downward
- This creates the illusion of the player continually ascending
- As platforms move below the screen, they are removed and new ones are generated at the top

### Scoring

The player earns points when platforms move off the bottom of the screen. The score is displayed at the top of the screen.

### Game Over

The game ends when the player falls off the bottom of the screen. A "GAME OVER" message is displayed before the game exits.

## Technical Implementation

### Constants

- `HEIGHT`: 450 pixels (game window height)
- `WIDTH`: 400 pixels (game window width)
- `ACC`: 0.5 (player acceleration)
- `FRIC`: -0.12 (friction coefficient)
- `FPS`: 60 (frames per second)
- `NUM_PLATFORMS`: 7 (minimum number of platforms)
- `MIN_DISTANCE`: 50 (minimum vertical distance between platforms)
- `VELOCITY`: -15 (initial jump velocity)
- `MIN_VELOCITY`: -3 (minimum jump velocity when jump is canceled)

### Helper Functions

- `check(platform, groupies)`: Validates that a new platform doesn't overlap with existing platforms
- `plat_gen(platforms, all_sprites, color)`: Generates new platforms as needed
- `main()`: The main game loop that handles events, updates game objects, and renders the screen

### Classes

#### Player Class

Attributes:
- `surf`: Surface representing the player
- `rect`: Rectangle for collision detection
- `pos`, `vel`, `acc`: Vectors for physics-based movement
- `score`: Player's score
- `jumping`: Boolean tracking jump state

Methods:
- `move()`: Updates player position based on keyboard input and physics
- `update(platforms)`: Handles collision with platforms
- `jump(platforms)`: Initiates a jump when the player is on a platform
- `cancel_jump()`: Reduces jump height when space is released

#### Platform Class

Attributes:
- `surf`: Surface representing the platform
- `rect`: Rectangle for collision detection
- `point`: Boolean indicating if the platform awards points when passed
- `moving`: Boolean indicating if the platform moves
- `speed`: Integer representing platform's horizontal speed
- `trampoline`: Boolean indicating if the platform is a trampoline

Methods:
- `move()`: Updates platform position when moving

## Controls

- Left Arrow: Move left
- Right Arrow: Move right
- Space Bar: Jump (hold for higher jumps)
- Escape: Quit the game

## Game Features

1. Platform color changes every 20 points
2. Platforms are randomly sized
3. Some platforms move left or right
4. Some platforms are trampolines that make the player jump higher
5. Game over screen with final score
