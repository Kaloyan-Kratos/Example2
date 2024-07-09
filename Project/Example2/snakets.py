
import sys
import random
import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
SNAKE_SPEED = 10

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake initialization
snake = [(WIDTH // 2, HEIGHT // 2)]
snake_direction = (1, 0)

# Apple initialization
apple = (random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE,
         random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE)

# High score and leaderboard
high_score = 0
leaderboard = []

# Get player's username
username = input("Enter your username: ")

# Load apple image (replace with your own image)
apple_image = pygame.image.load("apple.png") # Provide the path to your apple image

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake_direction = (0, -1)
    elif keys[pygame.K_DOWN]:
        snake_direction = (0, 1)
    elif keys[pygame.K_LEFT]:
        snake_direction = (-1, 0)
    elif keys[pygame.K_RIGHT]:
        snake_direction = (1, 0)

    # Update snake position
    x, y = snake[0]
    x += snake_direction[0] * GRID_SIZE
    y += snake_direction[1] * GRID_SIZE
    snake.insert(0, (x, y))

    # Check for collisions
    if snake[0] == apple:
        apple = (random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE,
                 random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE)
        high_score += 1
        leaderboard.append((username, high_score))
        leaderboard.sort(key=lambda x: x[1], reverse=True)
        leaderboard = leaderboard[:5] # Display top 5 scores
    else:
        snake.pop()

    # Draw checkered background
    for i in range(WIDTH // GRID_SIZE):
        for j in range(HEIGHT // GRID_SIZE):
            color = WHITE if (i + j) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (i * GRID_SIZE, j * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Draw snake and apple
    screen.blit(apple_image, (*apple, GRID_SIZE, GRID_SIZE))
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))

    # Display high score and leaderboard
    font = pygame.font.Font(None, 36)
    text = font.render(f"High Score: {high_score}", True, GREEN)
    screen.blit(text, (10, 10))

    for i, (name, score) in enumerate(leaderboard):
        text = font.render(f"{i + 1}. {name}: {score}", True, GREEN)
        screen.blit(text, (10, 50 + i * 30))

    pygame.display.flip()

    pygame.time.Clock().tick(SNAKE_SPEED)

