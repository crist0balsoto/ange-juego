import pygame
import sys
import random

# Función para reiniciar el juego
def reset_game():
    global hits, player_rect, bullets, enemies, items, start_time, game_over
    hits = 0
    player_rect.topleft = (width // 2 - player_rect.width // 2, height - player_rect.height - 10)
    bullets.clear()
    enemies.clear()
    items.clear()
    start_time = pygame.time.get_ticks()
    game_over = False

# Función para aumentar el tamaño de los disparos
def increase_bullet_size():
    global bullet_image, bullet_rect
    bullet_image = pygame.transform.scale(bullet_image, (bullet_rect.width + 5, bullet_rect.height + 5))
    bullet_rect = bullet_image.get_rect()

# Función para generar enemigos
def generate_enemies():
    if random.randint(0, 100) < 5:
        enemy_rect = enemy_image.get_rect()
        enemy_rect.x = random.randint(0, width - enemy_rect.width)
        enemies.append(enemy_rect.copy())

# Función para generar items
def generate_items():
    if random.randint(0, 100) < 2:
        item_rect = item_image.get_rect()
        item_rect.x = random.randint(0, width - item_rect.width)
        items.append(item_rect.copy())

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 700, 775
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("ojala el angelo muera en un accidente de tráfico")

# Cargar imágenes y escalarlas
player_image = pygame.image.load("imgs/messi.png")
player_image = pygame.transform.scale(player_image, (60, 60))

bullet_image = pygame.image.load("imgs/pene.png")
bullet_image = pygame.transform.scale(bullet_image, (50, 50))
bullet_rect = bullet_image.get_rect()

enemy_image = pygame.image.load("imgs/Angelo.png")
enemy_image = pygame.transform.scale(enemy_image, (60, 60))

item_image = pygame.image.load("imgs/yasuo.png")
item_image = pygame.transform.scale(item_image, (40, 40))
item_rect = item_image.get_rect()

background_image = pygame.image.load("imgs/fondo_amor.jpg")
background_image = pygame.transform.scale(background_image, (width, height))

# Jugador
player_rect = player_image.get_rect()
player_rect.topleft = (width // 2 - player_rect.width // 2, height - player_rect.height - 10)
player_speed = 15

# Bala
bullet_speed = 10
bullets = []

# Enemigo
enemy_speed = 5
enemies = []

# Item
item_speed = 5
items = []

# Reloj
clock = pygame.time.Clock()

# Mantener registro de teclas presionadas
keys_pressed = {'left': False, 'right': False}

# Tiempo transcurrido
start_time = pygame.time.get_ticks()

# Contador de golpes
hits = 0

# Variable de control de juego
game_over = False

# Bucle principal del juego
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Manejar movimientos del jugador
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keys_pressed['left'] = True
            elif event.key == pygame.K_RIGHT:
                keys_pressed['right'] = True
            elif event.key == pygame.K_SPACE:
                bullet_rect = bullet_image.get_rect()
                bullet = {
                    'rect': pygame.Rect(
                        player_rect.x +
                        player_rect.width // 2 -
                        bullet_rect.width // 2,
                        player_rect.y,
                        bullet_rect.width,
                        bullet_rect.height
                    ),
                    'image': bullet_image
                }
                bullets.append(bullet)
                
                # Verificar si hay un item en la pantalla y el jugador ha disparado
                if any(item_rect.colliderect(player_rect) for item_rect in items):
                    increase_bullet_size()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys_pressed['left'] = False
            elif event.key == pygame.K_RIGHT:
                keys_pressed['right'] = False

    # Actualizar posición del jugador
    if keys_pressed['left'] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys_pressed['right'] and player_rect.right < width:
        player_rect.x += player_speed

    # Actualizar posición de las balas
    for bullet in bullets:
        bullet['rect'].y -= bullet_speed

    # Generar enemigos y items
    generate_enemies()
    generate_items()

    # Actualizar posición de los enemigos
    for enemy in enemies:
        enemy.y += enemy_speed

    # Actualizar posición de los items
    for item in items:
        item.y += item_speed

    # Colisiones entre balas y enemigos
    for bullet in bullets:
        for enemy in enemies:
            if enemy.colliderect(bullet['rect']):
                bullets.remove(bullet)
                enemies.remove(enemy)
                hits += 1  # Incrementar contador de golpes

    # Colisiones entre jugador y enemigos
    for enemy in enemies:
        if player_rect.colliderect(enemy):
            game_over = True

    # Limpiar la pantalla con el fondo
    screen.blit(background_image, (0, 0))

    # Dibujar al jugador
    screen.blit(player_image, player_rect)

    # Dibujar las balas
    for bullet in bullets:
        screen.blit(bullet['image'], bullet['rect'].topleft)

    # Dibujar los enemigos
    for enemy in enemies:
        screen.blit(enemy_image, enemy)

    # Dibujar los items
    for item in items:
        screen.blit(item_image, item)

    # Mostrar el tiempo transcurrido
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    font = pygame.font.Font(None, 36)
    text = font.render("Tiempo transcurrido: {} seg".format(elapsed_time), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Mostrar el contador de golpes
    text_hits = font.render("Golpes: {}".format(hits), True, (255, 255, 255))
    screen.blit(text_hits, (10, 40))

    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer límite de FPS
    clock.tick(30)

# Ventana de juego terminado
font_game_over = pygame.font.Font(None, 48)
text_game_over = font_game_over.render("¡Perdiste!", True, (255, 0, 0))
text_game_over_rect = text_game_over.get_rect(center=(width // 2, height // 2))
screen.blit(text_game_over, text_game_over_rect)

# Preguntar al jugador si quiere jugar de nuevo
font_again = pygame.font.Font(None, 36)
text_again = font_again.render("¿Quieres jugar de nuevo? Presiona 'Again'", True, (255, 255, 255))
text_again_rect = text_again.get_rect(center=(width // 2, height // 2 + 50))
screen.blit(text_again, text_again_rect)

# Actualizar la pantalla
pygame.display.flip()

# Esperar respuesta del jugador
while game_over:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                reset_game()
