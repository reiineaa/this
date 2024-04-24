import pygame
import sys

def main():
    pygame.init()

    # Initialize the Pygame window
    screen = pygame.display.set_mode((800, 600))

    # Initialize the background color and mouse click state
    background_color = (0, 0, 0)
    is_blue = True

    # Run the main game loop
    while True:
        # Get the current mouse position and mouse click state
        mouse_pos = pygame.mouse.get_pos()
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
                # Toggle the background color when the mouse is clicked
                is_blue = not is_blue

        # Clear the screen and draw the rectangle at the current mouse position
        screen.fill((0, 0, 0) if is_blue else (255, 255, 255))
        
        if is_blue:
            color = (0, 128, 255)
            # Display the current mouse position on the screen
            font = pygame.font.Font(None, 36)
            text = font.render("Mouse Position: {}".format(mouse_pos), True, (255, 255, 255))
            screen.blit(text, (10, 10))

        else:
            color = (255, 100, 0)
            # Display the current mouse position on the screen
            font = pygame.font.Font(None, 36)
            text = font.render("Mouse Position: {}".format(mouse_pos), True, (0, 0, 0))
            screen.blit(text, (10, 10))

        pygame.draw.rect(screen, color, pygame.Rect(mouse_pos[0], mouse_pos[1], 15, 15))
        

    
        # Flip the display to show the updated screen
        pygame.display.flip()
        
        
if __name__ == '__main__':
    main()