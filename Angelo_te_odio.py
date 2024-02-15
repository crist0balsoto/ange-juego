import pygame
import sys
import random

# Función para reiniciar el juego
def reset_game():
    global hits, player_rect, bullets, enemies, items, start_time, game_over, enemy_speed, last_speed_increase_time
    hits = 0
    player_rect.topleft = (width // 2 - player_rect.width // 2, height - player_rect.height - 10)
    bullets.clear()
    enemies.clear()
    items.clear()
    start_time = pygame.time.get_ticks()
    last_speed_increase_time = start_time
    enemy_speed = 5
    game_over = False

# Función para aumentar el tamaño de los disparos
def increase_bullet_size():
    global bullet_image, bullet_rect, bullet_speed
    bullet_image = pygame.transform.scale(bullet_image, (bullet_rect.width + 2, bullet_rect.height + 2))
    bullet_rect = bullet_image.get_rect()

def increase_bullet_speed():
    global bullet_speed
    bullet_speed += 2  # Incrementa la velocidad de las balas

# Función para generar enemigos
def generate_enemies():
    if random.randint(0, 100) < 1:
        enemy_rect = enemy_image.get_rect()
        enemy_rect.x = random.randint(0, width - enemy_rect.width)
        enemies.append(enemy_rect.copy())

# Función para generar items
def generate_items():
    if random.randint(0, 100) < 0.1:  # Reducir la tasa de aparición de los ítems "Yasuo"
        item_rect = item_image.get_rect()
        item_rect.x = random.randint(0, width - item_rect.width)
        items.append(item_rect.copy())
    elif random.randint(0, 100) < 0.1:  # Asegurarse de que el item "Redbull" se genera
        item_rect2 = item_image2.get_rect()
        item_rect2.x = random.randint(0, width - item_rect2.width)
        items2.append(item_rect2.copy())

def generate_obstacles():
    if random.randint(0, 100) < 1:  # Ajusta la tasa de aparición de los obstáculos
        obstacle_rect = obstacle_image.get_rect()
        obstacle_rect.x = random.randint(0, width - obstacle_rect.width)
        obstacles.append(obstacle_rect.copy())


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

item_image2 = pygame.image.load("imgs/redbull.png")
item_image2 = pygame.transform.scale(item_image2, (40, 40))
item_rect2 = item_image.get_rect()

background_image = pygame.image.load("imgs/atacama2.jpg")
background_image = pygame.transform.scale(background_image, (width, height))

# Jugador
player_rect = player_image.get_rect()
player_rect.topleft = (width // 2 - player_rect.width // 2, height - player_rect.height - 10)
player_speed = 15

# Cargar la imagen del obstáculo
obstacle_image = pygame.image.load('imgs/amonus.png')
obstacle_image = pygame.transform.scale(obstacle_image, (40, 40))
# Velocidad del obstáculo
obstacle_speed = 1

# Lista de obstáculos
obstacles = []
# Bala
bullet_speed = 5
bullets = []

# Enemigo
enemy_speed = 2
enemies = []

# Item
item_speed = 9
items = []

# Item 2
item_speed2 = 9
items2 = []

# Reloj
clock = pygame.time.Clock()

# Mantener registro de teclas presionadas
keys_pressed = {'left': False, 'right': False}

# Tiempo transcurrido
start_time = pygame.time.get_ticks()
last_speed_increase_time = start_time
enemy_speed_increase_interval = 15000  # 15 segundos

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
                for item_rect in items.copy():
                    if item_rect.colliderect(player_rect):
                        increase_bullet_size()
                        items.remove(item_rect)
                for item_rect2 in items2.copy():
                    if item_rect2.colliderect(player_rect):
                        increase_bullet_speed()
                        items2.remove(item_rect2)

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
    generate_obstacles()

    # Actualizar posición de los enemigos
    for enemy in enemies:
        enemy.y += enemy_speed

    # Actualizar posición de los items
    for item in items:
        item.y += item_speed

    for item in items2:
        item.y += item_speed2

    # Actualizar posición de los obstáculos
    for obstacle in obstacles:
        obstacle.y += obstacle_speed

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
    
    # Verificar si hay un obstáculo en la pantalla y el jugador ha chocado con él
    for obstacle in obstacles:
        if obstacle.colliderect(player_rect):
            game_over = True # Llama a tu función de fin de juego

    # Aumentar la velocidad de los enemigos si ha pasado suficiente tiempo
    current_time = pygame.time.get_ticks()
    if current_time - last_speed_increase_time > enemy_speed_increase_interval:
        last_speed_increase_time = current_time
        enemy_speed += 2  # Aumentar la velocidad de los enemigos

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
    # Dibujar obstáculos en la pantalla
    for obstacle in obstacles:
        screen.blit(obstacle_image, obstacle)    

    # Dibujar los items
    for item in items:
        screen.blit(item_image, item)
    for item in items2:
        screen.blit(item_image2, item)  # Asegurarse de que el item "Redbull" se dibuja

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
    clock.tick(60)

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
