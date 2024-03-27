import pygame
import random

# Ekran boyutu
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Renkler
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)

class BonziFriend:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.width = 50
        self.height = 50
        self.velocity = 5

    def draw(self, screen):
        pygame.draw.rect(screen, PURPLE, (self.x, self.y, self.width, self.height))

    def move(self):
        self.x += random.randint(-self.velocity, self.velocity)
        self.y += random.randint(-self.velocity, self.velocity)
        self.x = max(0, min(self.x, SCREEN_WIDTH - self.width))
        self.y = max(0, min(self.y, SCREEN_HEIGHT - self.height))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Bonzi Friend")
    clock = pygame.time.Clock()

    bonzi = BonziFriend()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        bonzi.move()

        screen.fill(WHITE)
        bonzi.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
