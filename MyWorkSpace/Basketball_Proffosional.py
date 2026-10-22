import pygame
import sys

# Initialize Pygame
pygame.init()

# Game Constants & Settings
DISPLAY_SIZE = (1600, 1000)
FPS = 60

# Stats Variables
makes = 0
misses = 0

# Colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Setup Display and Clock
screen = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption("Basketball Game Stats")
clock = pygame.time.Clock()

# Setup Font (System Arial, size 36)
font = pygame.font.SysFont("Arial", 36)

# Button Definitions (Using Pygame Rectangles)
buttons = {
    "Make": pygame.Rect(300, 650, 300, 150), 
    "Miss": pygame.Rect(1000, 650, 300, 150)
}

# Main Game Loop Flag
is_running = True

while is_running:
    # 1. Clear the screen with a black background
    screen.fill(BLACK)
    
    # 2. Event Handling
    for event in pygame.event.get():
        # Handle window close event
        if event.type == pygame.QUIT:
            is_running = False
            
        # Handle mouse click event (Left click only)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if "Make" button is clicked
            if buttons["Make"].collidepoint(event.pos):
                makes += 1
                print(f"Makes: {makes}")
                
            # Check if "Miss" button is clicked
            elif buttons["Miss"].collidepoint(event.pos):
                misses += 1
                print(f"Misses: {misses}")
        
    # 3. Game Logic (Calculate Shooting Percentage)
    total_shots = makes + misses
    if total_shots > 0:
        shooting_percentage = (makes / total_shots) * 100
    else:
        shooting_percentage = 0.0 # Prevents ZeroDivisionError at the start
        
    # 4. Rendering / Drawing UI Elements
    
    # Draw the interactive buttons
    pygame.draw.rect(screen, RED, buttons["Make"])
    pygame.draw.rect(screen, RED, buttons["Miss"])
    
    # Render text strings into surface objects
    stats_text = f"Makes: {makes}   |   Misses: {misses}   |   Percentage: {shooting_percentage:.1f}%"
    text_surface = font.render(stats_text, True, WHITE)
    make_miss_surface = font.render("Make", True, WHITE)
    miss_miss_surface = font.render("Miss", True, WHITE)
    
    # Draw the text surface to the top-center of the screen
    screen.blit(text_surface, (550, 100))
    screen.blit(make_miss_surface, (400, 700))  # Positioning the "Make" and "Miss" labels above their respective buttons
    screen.blit(miss_miss_surface, (1100, 700))  # Positioning the "Make" and "Miss" labels above their respective buttons
    
    # 5. Update the display and cap the frame rate
    pygame.display.flip()
    clock.tick(FPS)

# Clean up and close the application safely
pygame.quit()
sys.exit()
