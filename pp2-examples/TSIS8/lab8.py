import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
BALL_SIZE = 64
GRAVITY = 1.5

# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drag and Drop with Drawing")

# Load the beach ball image
beach_ball_images = [pygame.image.load('beachball.png'), pygame.image.load('beachball2.png'), pygame.image.load('beachball3.png')]
beach_ball_image = random.choice(beach_ball_images)
beach_ball_rect = beach_ball_image.get_rect(center=(WIDTH//2, HEIGHT//2))

# Set the size of the beach ball
beach_ball_image = pygame.transform.scale(beach_ball_image, (BALL_SIZE, BALL_SIZE))
beach_ball_rect = beach_ball_image.get_rect(center=(WIDTH//2, HEIGHT//2))

# Variables to track mouse click and movement
is_dragging = False
offset_x, offset_y = 0, 0

# Drawing variables
drawing = False
last_pos = (0, 0)
lines = []

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and beach_ball_rect.collidepoint(event.pos):
                is_dragging = True
                offset_x = event.pos[0] - beach_ball_rect.x
                offset_y = event.pos[1] - beach_ball_rect.y
            elif event.button == 1 and drawing and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                drawing = False
                lines.append((BLACK, last_pos, event.pos))
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                is_dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if is_dragging:
                mouse_x, mouse_y = event.pos
                beach_ball_rect.x = mouse_x - offset_x
                beach_ball_rect.y = mouse_y - offset_y
            elif drawing:
                current_pos = event.pos
                lines.append((BLACK, last_pos, current_pos))
                last_pos = current_pos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                drawing = not drawing
                if drawing:
                    last_pos = pygame.mouse.get_pos()

    # Move the beach ball
    if beach_ball_rect.y + BALL_SIZE/2 < HEIGHT:
        beach_ball_rect.y += GRAVITY

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the beach ball
    screen.blit(beach_ball_image, beach_ball_rect)

    # Draw lines
    for line_color, start_pos, end_pos in lines:
        pygame.draw.line(screen, line_color, start_pos, end_pos, 2)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(1000 // 60)
