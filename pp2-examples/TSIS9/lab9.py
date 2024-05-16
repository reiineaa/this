import pygame
import sys
import random

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SIZE = 64
GRAVITY = 1.5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drag and Drop with Drawing")

# Load beach ball images
beach_ball_images = [pygame.image.load('beachball.png'), pygame.image.load('beachball2.png'), pygame.image.load('beachball3.png')]


class Ball:
    def __init__(self):
        self.image = random.choice(beach_ball_images)
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.image = pygame.transform.scale(self.image, (BALL_SIZE, BALL_SIZE))


class Square:
    def __init__(self, start_pos):
        self.rect = pygame.Rect(start_pos[0], start_pos[1], BALL_SIZE, BALL_SIZE)


class Circle:
    def __init__(self, center_pos):
        self.center = center_pos
        self.radius = BALL_SIZE // 2


class Game:
    def __init__(self):
        self.is_dragging_ball = False
        self.is_dragging_shape = False
        self.offset_x, self.offset_y = 0, 0
        self.drawing = False
        self.lines = []
        self.shapes = []
        self.selected_shape = None
        self.ball = Ball()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.ball.rect.collidepoint(event.pos):
                    self.is_dragging_ball = True
                    self.offset_x = event.pos[0] - self.ball.rect.x
                    self.offset_y = event.pos[1] - self.ball.rect.y
                    self.selected_shape = self.ball
                elif event.button == 1 and self.drawing:
                    self.lines.append([event.pos])
                elif event.button == 1:
                    for shape in self.shapes:
                        if isinstance(shape, Square) and shape.rect.collidepoint(event.pos):
                            self.is_dragging_shape = True
                            self.offset_x = event.pos[0] - shape.rect.x
                            self.offset_y = event.pos[1] - shape.rect.y
                            self.selected_shape = shape
                        elif isinstance(shape, Circle) and pygame.Rect(shape.center[0] - shape.radius, shape.center[1] - shape.radius, shape.radius * 2, shape.radius * 2).collidepoint(event.pos):
                            self.is_dragging_shape = True
                            self.offset_x = event.pos[0] - shape.center[0]
                            self.offset_y = event.pos[1] - shape.center[1]
                            self.selected_shape = shape
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.is_dragging_ball = False
                    self.is_dragging_shape = False
            elif event.type == pygame.MOUSEMOTION:
                if self.is_dragging_ball:
                    mouse_x, mouse_y = event.pos
                    self.ball.rect.x = mouse_x - self.offset_x
                    self.ball.rect.y = mouse_y - self.offset_y
                elif self.is_dragging_shape:
                    mouse_x, mouse_y = event.pos
                    if isinstance(self.selected_shape, Square):
                        self.selected_shape.rect.x = mouse_x - self.offset_x
                        self.selected_shape.rect.y = mouse_y - self.offset_y
                    elif isinstance(self.selected_shape, Circle):
                        self.selected_shape.center = (mouse_x - self.offset_x, mouse_y - self.offset_y)
                elif self.drawing:
                    current_pos = event.pos
                    self.lines[-1].append(current_pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.drawing = not self.drawing
                elif event.key == pygame.K_s and not self.drawing:
                    self.shapes.append(Square(pygame.mouse.get_pos()))
                elif event.key == pygame.K_c and not self.drawing:
                    self.shapes.append(Circle(pygame.mouse.get_pos()))

    def move_shapes(self):
        for shape in self.shapes:
            if isinstance(shape, Square):
                if shape.rect.y + BALL_SIZE/2 < HEIGHT:
                    shape.rect.y += GRAVITY
            elif isinstance(shape, Circle):
                if shape.center[1] + BALL_SIZE/2 < HEIGHT:
                    shape.center = (shape.center[0], shape.center[1] + GRAVITY)

    def draw_shapes(self):
        for item in self.lines:
            if len(item) == 4:  # Drawing a square
                color, start, width, height = item
                pygame.draw.rect(screen, color, (start[0], start[1], width, height), 2)

        for shape in self.shapes:
            if isinstance(shape, Square):
                pygame.draw.rect(screen, BLACK, shape.rect, 2)
            elif isinstance(shape, Circle):
                pygame.draw.circle(screen, BLACK, shape.center, shape.radius, 2)

    def run(self):
        while True:
            self.handle_events()

            self.ball.rect.y += GRAVITY if self.ball.rect.y + BALL_SIZE/2 < HEIGHT else 0
            self.move_shapes()

            screen.fill(WHITE)
            screen.blit(self.ball.image, self.ball.rect)
            self.draw_shapes()

            pygame.display.flip()
            pygame.time.delay(1000 // 60)


if __name__ == "__main__":
    game = Game()
    game.run()
