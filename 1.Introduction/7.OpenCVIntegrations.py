# Import
import pygame
import cv2
import numpy as np

# Initialize
pygame.init()

# Create Window/Display
width, height = 1280, 720
window = pygame.display.set_mode((width, height/2))
pygame.display.set_caption("My First Python Game")

# Initialize Clock for FPS
fps = 30
clock = pygame.time.Clock()

# Webcam
cap = cv2.VideoCapture(2)
cap.set(3, 1280)  # width
cap.set(4, 720)  # height

# Main loop
start = True
while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # Apply Logic

    # OpenCV
    success, img = cap.read()
    # if not success:
    #     print("Can't receive frame (stream end?). Exiting ...")
    #     break
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgRGB = np.rot90(imgRGB)
    frame = pygame.surfarray.make_surface(imgRGB).convert()
    frame = pygame.transform.flip(frame, True, False)
    window.blit(frame, (0, 0))

    # Update Display
    pygame.display.update()
    # Set FPS
    clock.tick(fps)