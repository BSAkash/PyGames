# Import
import pygame

# Initialize
pygame.init()

# Create Window/Display
width, height = 1280, 720
window = pygame.display.set_mode((width, height/2))
pygame.display.set_caption("My First Python Game")

# Initialize Clock for FPS
fps = 30
clock = pygame.time.Clock()

# Main loop
start = True
while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # Apply Logic
    window.fill((255, 255, 255))
    font = pygame.font.Font('Resources\Marcellus-Regular.ttf', 100)
    font2 = pygame.font.Font(None, 100)
    text = font.render("My First Python Game", True, (50, 50, 50))
    text2 = font2.render("My First Python Game", True, (50, 50, 50))
    window.blit(text, (350, 200))
    window.blit(text2, (350, 400))

    # Update Display
    pygame.display.update()
    # Set FPS
    clock.tick(fps)