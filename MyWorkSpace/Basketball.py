import pygame

pygame.init()

isWorking = True

Display = (1600, 1000)

screen = pygame.display.set_mode(Display)
pygame.display.set_caption("Basketball Game")


while isWorking:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isWorking = False
            
    #(right to left, up to down, width, height), it at the top left corner of the screen
    pygame.draw.rect(screen, (255, 0, 0), (700, 425, 200, 150))
    pygame.display.flip()

pygame.quit()