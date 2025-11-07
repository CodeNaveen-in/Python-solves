import pygame
import random

# Initialize
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("👾 Space Invaders")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player
player_img = pygame.Surface((50, 30))
player_img.fill(WHITE)
player_x = WIDTH // 2
player_y = HEIGHT - 60
player_speed = 5

# Bullet
bullet_img = pygame.Surface((5, 15))
bullet_img.fill(RED)
bullet_speed = 7
bullets = []

# Alien
alien_img = pygame.Surface((40, 30))
alien_img.fill((0, 255, 0))
aliens = []
alien_speed = 2
alien_direction = 1

# Create alien fleet
for row in range(3):
    for col in range(8):
        aliens.append(pygame.Rect(80 + col * 80, 50 + row * 50, 40, 30))

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Game loop
running = True
while running:
    screen.fill((0, 0, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:
            bullets.append(pygame.Rect(player_x + 22, player_y, 5, 15))

    # Move bullets
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Move aliens
    for alien in aliens:
        alien.x += alien_speed * alien_direction
    if any(a.x > WIDTH - 40 or a.x < 0 for a in aliens):
        alien_direction *= -1
        for alien in aliens:
            alien.y += 20

    # Collision detection
    for bullet in bullets[:]:
        for alien in aliens[:]:
            if bullet.colliderect(alien):
                bullets.remove(bullet)
                aliens.remove(alien)
                score += 10
                break

    # Draw player
    screen.blit(player_img, (player_x, player_y))

    # Draw bullets
    for bullet in bullets:
        screen.blit(bullet_img, bullet)

    # Draw aliens
    for alien in aliens:
        screen.blit(alien_img, alien)

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()