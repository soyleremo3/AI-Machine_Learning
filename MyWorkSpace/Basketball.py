import pygame

pygame.init()

isWorking = True
Makes = 0
Mises = 0

Display = (1600, 1000)

botton_Rect = {
    "botton_Rect": pygame.Rect(300, 650, 300, 150)
}

screen = pygame.display.set_mode(Display)
pygame.display.set_caption("Basketball Game")


while isWorking:
    for event in pygame.event.get():
        
        event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if botton_Rect["botton_Rect"].collidepoint(event.pos):
                print("Right button clicked")
        
        #close the window
        if event.type == pygame.QUIT:
            isWorking = False
            
    #(right to left, up to down, width, height), it at the top left corner of the screen
    pygame.draw.rect(screen, (255, 0, 0), (300, 650, 300, 150))
    pygame.draw.rect(screen, (255, 0, 0), (1000, 650, 300, 150))
    pygame.display.flip()

pygame.quit()