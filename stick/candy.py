import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
HERO_SIZE = 50
BULLET_SIZE = 20
ENEMY_SIZE = 50

# Set up some colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the game characters
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, speed):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.x += self.speed

class Hero(GameSprite):
    def __init__(self):
        super().__init__("./images/hero.png", 0)
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT - HERO_SIZE - 20
        self.bullets = pygame.sprite.Group()

    def update(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.speed = 3
        elif keys_pressed[pygame.K_LEFT]:
            self.speed = -3
        else:
            self.speed = 0
        super().update()
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def fire(self):
        bullet = Bullet()
        bullet.rect.x = self.rect.x + HERO_SIZE / 2
        bullet.rect.y = self.rect.y
        self.bullets.add(bullet)

class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet.png", -2)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

class Enemy(GameSprite):
    def __init__(self):
        super().__init__("./images/enemy.png", random.randint(1, 3))
        self.rect.x = random.randint(0, WIDTH - ENEMY_SIZE)
        self.rect.y = -ENEMY_SIZE

    def update(self):
        super().update()
        if self.rect.top > HEIGHT:
            self.kill()

# Set up the game loop
def game_loop():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Airplane War Game")

    clock = pygame.time.Clock()

    hero = Hero()
    enemies = pygame.sprite.Group()

    BULLET_TIMER = pygame.USEREVENT + 1
    ENEMY_TIMER = pygame.USEREVENT + 2

    pygame.time.set_timer(BULLET_TIMER, 500)
    pygame.time.set_timer(ENEMY_TIMER, 1000)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == BULLET_TIMER:
                hero.fire()
            elif event.type == ENEMY_TIMER:
                enemy = Enemy()
                enemies.add(enemy)

        hero.update()
        hero.bullets.update()
        enemies.update()

        screen.fill(WHITE)
        hero.bullets.draw(screen)
        enemies.draw(screen)
        hero.draw(screen)
        pygame.display.flip()
        clock.tick(60)

game_loop()