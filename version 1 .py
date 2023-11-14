import pygame

def show_title_screen():
    title_running = True
    while title_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                title_running = False
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                title_running = False

        screen.fill((0, 0, 0))  # Fill the screen with a color
        font = pygame.font.Font(None, 74)
        text = font.render("Horror Maze", True, (255, 255, 255))
        screen.blit(text, (200, 250))  # Adjust the position as needed
        pygame.display.flip()

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("horror maze")

show_title_screen()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

