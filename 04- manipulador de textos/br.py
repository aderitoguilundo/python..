import pygame
import random

pygame.init()

# Janela
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Cores
WHITE = (255, 255, 255)
RED = (255, 50, 50)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Jogador
player_x = 175
player_y = 500
player_speed = 5

# Tiros
bullets = []

# Inimigos
enemies = []
for i in range(5):
    enemies.append([random.randint(0, 370), random.randint(-300, 0)])

score = 0
font = pygame.font.SysFont(None, 30)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Atirar com ESPAÇO
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_x + 20, player_y])

    # Mexer com setas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < 350:
        player_x += player_speed

    # Mexer tiros
    for bullet in bullets[:]:
        bullet[1] -= 8
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Mexer inimigos
    for enemy in enemies:
        enemy[1] += 3
        if enemy[1] > 600:
            enemy[1] = random.randint(-100, 0)
            enemy[0] = random.randint(0, 370)

    # Tiro acertou inimigo?
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if enemy[0] < bullet[0] < enemy[0] + 30 and enemy[1] < bullet[1] < enemy[1] + 30:
                bullets.remove(bullet)
                enemies.remove(enemy)
                enemies.append([random.randint(0, 370), random.randint(-100, 0)])
                score += 1
                break

    # Inimigo bateu em ti? Game Over
    for enemy in enemies:
        if enemy[0] < player_x < enemy[0] + 30 and enemy[1] < player_y < enemy[1] + 30:
            running = False

    # Desenhar tudo
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, 50, 30))

    for bullet in bullets:
        pygame.draw.rect(screen, YELLOW, (bullet[0], bullet[1], 5, 10))

    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], 30, 30))

    text = font.render(f"Pontos: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print(f"Fim do jogo! Fizeste {score} pontos!")