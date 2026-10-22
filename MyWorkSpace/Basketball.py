import pygame

pygame.init()

isWorking = True
Makes = 0
Mises = 0

Display = (1600, 1000)

Boottoms = {
    "Make": pygame.Rect(300, 650, 300, 150), 
    "Miss": pygame.Rect(1000, 650, 300, 150)
}

screen = pygame.display.set_mode(Display)
pygame.display.set_caption("Basketball Game")


while isWorking:
    for event in pygame.event.get():
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #Make
            if Boottoms["Make"].collidepoint(event.pos):
                Makes += 1
                print("Makes:", Makes)
                
            #Miss
            if Boottoms["Miss"].collidepoint(event.pos):
                Mises += 1
                print("Misses:", Mises)
        
        #close the window
        if event.type == pygame.QUIT:
            isWorking = False
            
    #(right to left, up to down, width, height), it at the top left corner of the screen
    pygame.draw.rect(screen, (255, 0, 0), (300, 650, 300, 150))
    pygame.draw.rect(screen, (255, 0, 0), (1000, 650, 300, 150))
    pygame.display.flip()

pygame.quit()