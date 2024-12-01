import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Plants vs Zombies Clone")

# Colors
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Game classes
class Plant(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100
        self.attack_cooldown = 60
        self.attack_timer = 0
        
    def update(self):
        self.attack_timer += 1

class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 80))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100
        self.speed = 1
        
    def update(self):
        self.rect.x -= self.speed

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        
    def update(self):
        self.rect.x += self.speed

class Game:
    def __init__(self):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.plants = pygame.sprite.Group()
        self.zombies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        
        # Game variables
        self.score = 0
        self.sun_points = 100
        self.font = pygame.font.Font(None, 36)
        
    def spawn_zombie(self):
        # Spawn zombies on the right side of the screen in random rows
        y = random.randint(0, SCREEN_HEIGHT - 80)
        zombie = Zombie(SCREEN_WIDTH, y)
        self.zombies.add(zombie)
        self.all_sprites.add(zombie)
    
    def spawn_plant(self, x, y):
        if self.sun_points >= 50:
            plant = Plant(x, y)
            self.plants.add(plant)
            self.all_sprites.add(plant)
            self.sun_points -= 50
    
    def handle_collisions(self):
        # Bullet-Zombie collisions
        for bullet in self.bullets:
            zombie_hits = pygame.sprite.spritecollide(bullet, self.zombies, False)
            for zombie in zombie_hits:
                zombie.health -= 20
                bullet.kill()
                
                if zombie.health <= 0:
                    zombie.kill()
                    self.score += 10
        
        # Zombie-Plant collisions
        for zombie in self.zombies:
            plant_hits = pygame.sprite.spritecollide(zombie, self.plants, False)
            for plant in plant_hits:
                plant.health -= 1
                
                if plant.health <= 0:
                    plant.kill()
    
    def run(self):
        # Zombie spawn timer
        zombie_spawn_timer = 0
        
        while self.running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                # Plant spawning with mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    self.spawn_plant(x, y)
            
            # Spawn zombies periodically
            zombie_spawn_timer += 1
            if zombie_spawn_timer >= 180:  # Every 3 seconds
                self.spawn_zombie()
                zombie_spawn_timer = 0
            
            # Plant shooting
            for plant in self.plants:
                if plant.attack_timer >= plant.attack_cooldown:
                    bullet = Bullet(plant.rect.right, plant.rect.centery)
                    self.bullets.add(bullet)
                    self.all_sprites.add(bullet)
                    plant.attack_timer = 0
            
            # Update
            self.all_sprites.update()
            
            # Handle collisions
            self.handle_collisions()
            
            # Draw
            self.screen.fill(WHITE)
            self.all_sprites.draw(self.screen)
            
            # Draw score and sun points
            score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
            points_text = self.font.render(f"Sun Points: {self.sun_points}", True, (0, 0, 0))
            self.screen.blit(score_text, (10, 10))
            self.screen.blit(points_text, (10, 50))
            
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()

# Run the game
if __name__ == "__main__":
    game = Game()
    game.run()