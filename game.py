import pygame
import sys
import config # Import the config Module
import random
import shapes


def init_game():
    pygame.init()
    
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constanst from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

background_image = pygame.image.load('saturn_family1.jpg').convert()




def main():
    screen = init_game()
    screen.blit(background_image,[0,0])
    running = True
    clock = pygame.time.Clock() # Initialize the clock her
    
    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config
        
        
        pygame.display.flip()

        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()