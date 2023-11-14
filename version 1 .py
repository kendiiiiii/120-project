import pygame
import requests
import os

def download_image(url, filename):
    if not os.path.exists(filename):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(filename, 'wb') as file:
                    file.write(response.content)
            else:
                print(f"Failed to download the image. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred during image download: {e}")
            
image_url = 'https://preview.redd.it/4f5rrt9qexk71.jpg?width=640&crop=smart&auto=webp&s=ae4d53cc0da15d67732db0f055270e6b805af012'
image_filename = 'title_screen_image.jpg'
download_image(image_url, image_filename)

def show_title_screen(screen):
    
    title_image = pygame.image.load(image_filename).convert()
    font = pygame.font.Font(None, 74)
    
    title_running = True
    while title_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                title_running = False
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                title_running = False
                
        

        screen.fill((200, 200, 100))  # Fill the screen with a color
        screen.blit(title_image, (0, 0))
        
        text = font.render("Horror Maze", True, (32, 255, 200))
        screen.blit(text, (500, 450))  # Adjust the position as needed
        
        
        
        pygame.display.flip()

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Horror Maze")

show_title_screen(screen)

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
