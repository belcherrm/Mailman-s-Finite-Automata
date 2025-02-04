import pygame
import sys
import config
from game import start_game

# Initialize Pygame
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mailman DFA vs. NFA Game - Mode Selection")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 50, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
GRAY = (180, 180, 180)

# Font
FONT = pygame.font.Font(None, 40)

def draw_text(text, x, y, color=BLACK):
    """Helper function to render text on the screen."""
    text_surface = FONT.render(text, True, color)
    screen.blit(text_surface, (x, y))

def main_menu():
    running = True
    while running:
        screen.fill(WHITE)

        if config.mode_selected is None:
            # Mode selection
            draw_text("Select Mode:", WIDTH // 2 - 100, 100)
            pygame.draw.rect(screen, BLUE, (250, 200, 150, 50))
            pygame.draw.rect(screen, RED, (450, 200, 150, 50))
            draw_text("DFA", 300, 210, WHITE)
            draw_text("NFA", 500, 210, WHITE)

        elif config.difficulty_selected is None:
            # Difficulty selection
            draw_text(f"Mode: {config.mode_selected}", WIDTH // 2 - 100, 100)
            draw_text("Select Difficulty:", WIDTH // 2 - 150, 200)
            pygame.draw.rect(screen, GREEN, (250, 300, 100, 50))
            pygame.draw.rect(screen, BLUE, (375, 300, 100, 50))
            pygame.draw.rect(screen, RED, (500, 300, 100, 50))
            draw_text("Easy", 270, 310, WHITE)
            draw_text("Medium", 385, 310, WHITE)
            draw_text("Hard", 525, 310, WHITE)

        else:
            # Game Start
            start_game(config.mode_selected, config.difficulty_selected)
            return  # Exit menu and start game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if config.mode_selected is None:
                    if 250 <= x <= 400 and 200 <= y <= 250:
                        config.mode_selected = "DFA"
                    elif 450 <= x <= 600 and 200 <= y <= 250:
                        config.mode_selected = "NFA"
                elif config.difficulty_selected is None:
                    if 250 <= x <= 350 and 300 <= y <= 350:
                        config.difficulty_selected = "Easy"
                    elif 375 <= x <= 475 and 300 <= y <= 350:
                        config.difficulty_selected = "Medium"
                    elif 500 <= x <= 600 and 300 <= y <= 350:
                        config.difficulty_selected = "Hard"

        pygame.display.update()

if __name__ == "__main__":
    main_menu()