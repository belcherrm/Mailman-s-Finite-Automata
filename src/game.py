import pygame
from easy_dfa import get_easy_dfa
import sys


pygame.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 50, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)


FONT = pygame.font.Font(None, 30)  


dfa = get_easy_dfa()
states = dfa["states"]
alphabet = dfa["alphabet"]
start_state = dfa["start_state"]
accept_states = dfa["accept_states"]
transitions = dfa["transitions"]


state_positions = {
    "A": (200, 300),
    "B": (400, 300),
    "C": (600, 300),
}

# Score
score = 0

class Mailman:
    def __init__(self):
        self.current_state = start_state
        self.x, self.y = state_positions[self.current_state]
        self.radius = 20  # Size of the mailman

    def move(self, input_symbol):
        """Move the mailman based on DFA transitions."""
        global score
        if input_symbol not in alphabet:
            print(f"Invalid input: {input_symbol}. Use 'a' or 'b'.")
            return

        if self.current_state in transitions and input_symbol in transitions[self.current_state]:
            next_state = transitions[self.current_state][input_symbol]
            self.current_state = next_state
            self.x, self.y = state_positions[next_state]  # Update position

            # Increase score if mailman reaches an accepting state
            if next_state in accept_states:
                score += 10  # Award 10 points for correct delivery

    def draw(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)

def draw_roads():
    """Draw transitions between states."""
    for start, trans in transitions.items():  
        for label, end in trans.items():
            x1, y1 = state_positions[start]
            x2, y2 = state_positions[end]

            pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 3)

            mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
            text = FONT.render(label, True, BLACK)
            screen.blit(text, (mid_x - 10, mid_y - 10))

def draw_states():
    """Draw states as circles."""
    for state, (x, y) in state_positions.items():
        color = GREEN if state in accept_states else BLUE
        pygame.draw.circle(screen, color, (x, y), 40)
        pygame.draw.circle(screen, BLACK, (x, y), 42, 2)
        text = FONT.render(state, True, WHITE)
        screen.blit(text, (x - 10, y - 10))

def draw_score():
    """Display the current score."""
    score_text = FONT.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (20, 20))

def start_game(mode, difficulty):
    """Start the game with the selected mode and difficulty."""
    global mailman, score, screen
    score = 0  # Reset score
    mailman = Mailman()  # Reset player

    # Initialize Pygame screen
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption(f"Mailman {mode} Game - {difficulty} Mode")

    running = True
    while running:
        screen.fill(WHITE)

        draw_roads()
        draw_states()
        mailman.draw()
        draw_score()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    mailman.move("a")
                elif event.key == pygame.K_b:
                    mailman.move("b")

        pygame.display.update()