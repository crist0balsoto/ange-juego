import pygame
from pygame import mixer
import sys
import random
import os




# Función para reiniciar el juego
def reset_game():
    global hits, player_rect, bullets, enemies, items, start_time, game_over, enemy_speed, last_speed_increase_time, bullet_speed, bullet_rect
    hits = 0
    player_rect.topleft = (width // 2 - player_rect.width // 2, height - player_rect.height - 10)
    bullets.clear()
    enemies.clear()
    items.clear()
    items2.clear()
    obstacles.clear()
    bullet_speed = 5
    bullet_rect.width, bullet_rect.height = 50, 50

    start_time = pygame.time.get_ticks()
    last_speed_increase_time = start_time
    enemy_speed = 5
    game_over = False

def play_random_sound():
    random.choice(sounds).play()

    

# Función para aumentar el tamaño de los disparos
def increase_bullet_size():
    global bullet_image, bullet_rect, bullet_speed
    bullet_image = pygame.transform.scale(bullet_image, (bullet_rect.width + 2, bullet_rect.height + 2))
    bullet_rect = bullet_image.get_rect()

def increase_bullet_speed():
    global bullet_speed
    bullet_speed += 2  # Incrementa la velocidad de las balas

def start_screen():
    width, height = 700, 775
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("jueguito hecho por andres")
    icono= pygame.image.load("imgs/messi.png")
    pygame.display.set_icon(icono)
    
    # Cargar las imágenes del botón
    button_image = pygame.image.load("imgs/pene.png")
    button_image = pygame.transform.scale(button_image, (200, 200))  # Cambia el tamaño según tus necesidades
    hover_image = pygame.image.load("imgs/pene.png")  # Cambia esto por la ruta a tu imagen de hover
    hover_image = pygame.transform.scale(hover_image, (200, 200))  # Cambia el tamaño según tus necesidades

    # Definir el botón de inicio
    start_button = button_image.get_rect()
    start_button.topleft = (100, 200)  # Cambia las coordenadas según tus necesidades

    # Definir el título
    font = pygame.font.Font(None, 74)  # Cambia el tamaño de la fuente según tus necesidades
    title = font.render('Bienvenido al ange-juego', True, (255, 10, 180))  # Cambia 'Mi Juego' por el título de tu juego
    
    font2 = pygame.font.Font(None, 30)  # Cambia el tamaño de la fuente según tus necesidades
    text = font2.render('Presiona el botón para comenzar', True, (255, 255, 255))  # Cambia 'Mi Juego' por el título de tu juego
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return

        # Cambiar la imagen del botón cuando el mouse está sobre él
        current_image = hover_image if start_button.collidepoint(pygame.mouse.get_pos()) else button_image

        # Llenar la pantalla y dibujar el título, el texto y el botón de inicio
        background_image = pygame.image.load("imgs/atacama2.jpg")
        background_image = pygame.transform.scale(background_image, (700, 775))
        screen.fill((0, 0, 0))  # Cambia el color de fondo si lo deseas
        screen.blit(background_image, (0, 0))
        screen.blit(title, (70, 50))  # Cambia las coordenadas según tus necesidades
        screen.blit(text, (75, 130))  # Cambia las coordenadas según tus necesidades
        screen.blit(current_image, start_button.topleft)

        pygame.display.flip()
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
mixer.init()

screen = pygame.display.set_mode((700, 775))  # Cambia el tamaño si lo deseas

# Llamar a la pantalla de inicio después de inicializar Pygame
start_screen()
sounds = [pygame.mixer.Sound(os.path.join('sonidos', sound)) for sound in os.listdir('sonidos') if sound.endswith('.mp3')]
# Cargar y reproducir la música de fondo
mixer.music.load('music/musica2.mp3')
mixer.music.play(-1)

# Configuración de la pantalla
width, height = 700, 775
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("jueguito hecho por andres")
icono= pygame.image.load("imgs/amonus.png")
pygame.display.set_icon(icono)

# Cargar imágenes y escalarlas
player_image = pygame.image.load("imgs/messi.png")
player_image = pygame.transform.scale(player_image, (60, 60))

bullet_image = pygame.image.load("imgs/pene.png")
bullet_image = pygame.transform.scale(bullet_image, (50, 50))
bullet_rect = bullet_image.get_rect()

enemy_image = pygame.image.load("imgs/Angelo.png")
enemy_image = pygame.transform.scale(enemy_image, (60, 60))

item_image = pygame.image.load("imgs/yasuo.png")
item_image = pygame.transform.scale(item_image, (60, 60))
item_rect = item_image.get_rect()

item_image2 = pygame.image.load("imgs/redbull.png")
item_image2 = pygame.transform.scale(item_image2, (60, 60))
item_rect2 = item_image.get_rect()

background_image = pygame.image.load("imgs/atacama2.jpg")
background_image = pygame.transform.scale(background_image, (width, height))

# Jugador
player_rect = player_image.get_rect()
player_rect.topleft = (width // 2 - player_rect.width // 2, height - player_rect.height - 10)
player_speed = 15

# Inicializa la variable de pausa
paused = False

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
keys_pressed = {'left': False, 'right': False, 'up': False, 'down': False}

# Tiempo transcurrido
start_time = pygame.time.get_ticks()
last_speed_increase_time = start_time
enemy_speed_increase_interval = 15000  # 15 segundos

# Contador de golpes
hits = 0

# Variable de control de juego
game_over = False

# Crear un objeto Font
font = pygame.font.Font(None, 36)  # Cambia el tamaño de la fuente según tus necesidades

# Crear las superficies de texto
game_over_text = font.render("¡Cagaste!", True, (255, 0, 0))
text_game_over_text = game_over_text.get_rect(center=(width // 2, height // 2))  # Cambia el color del texto si lo deseas
font_again = pygame.font.Font(None, 36)
text_again = font_again.render("Para volver a comenzar Presiona 'w'", True, (255, 255, 255))
text_again_rect = text_again.get_rect(center=(width // 2, height // 2 + 50))  # Cambia el color del texto si lo deseas

font_pause = pygame.font.Font(None, 48)
text_pause = font_pause.render("Juego Pausado", True, (0, 0, 0))
text_pause_rect = text_pause.get_rect(center=(width // 2, height // 2))

for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:  # Ahora se usa la tecla Escape para pausar el juego
            paused = not paused  # Cambia el estado de pausa


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
            elif event.key == pygame.K_UP:
                keys_pressed['up'] = True
            elif event.key == pygame.K_DOWN:
                keys_pressed['down'] = True
            elif event.key == pygame.K_ESCAPE:  # Ahora se usa la tecla Escape para pausar el juego
                paused = not paused  # Cambia el estado de pausa    
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
            elif event.key == pygame.K_UP:
                keys_pressed['up'] = False
            elif event.key == pygame.K_DOWN:
                keys_pressed['down'] = False
    if paused:
        screen.blit(text_pause, text_pause_rect)
        pygame.display.flip()
        continue

    # Actualizar posición del jugador
    if keys_pressed['left'] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys_pressed['right'] and player_rect.right < width:
        player_rect.x += player_speed
    if keys_pressed['up'] and player_rect.top > 0:
        player_rect.y -= player_speed
    if keys_pressed['down'] and player_rect.bottom < height:
        player_rect.y += player_speed

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
                play_random_sound()
                hits += 1  # Incrementar contador de golpes
    
    # Actualizar y dibujar explosiones

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
    if game_over:

        # Dibujar las superficies de texto en la pantalla
        screen.blit(game_over_text, text_game_over_text)  # Cambia las coordenadas según tus necesidades
        screen.blit(text_again, text_again_rect)  # Cambia las coordenadas según tus necesidades
    
        # Actualizar la pantalla
        pygame.display.flip()
    
        # Esperar a que el jugador presione 'w' para reiniciar el juego
        while game_over:
            for event in pygame.event.get():
                font_game_over = pygame.font.Font(None, 48)
                text_game_over = font_game_over.render("¡Cagaste!", True, (255, 0, 0))
                text_game_over_rect = text_game_over.get_rect(center=(width // 2, height // 2))
                screen.blit(text_game_over, text_game_over_rect)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        game_over = False
                        reset_game()
                        break

# Ventana de juego terminado
font_game_over = pygame.font.Font(None, 48)
text_game_over = font_game_over.render("¡Cagaste!", True, (255, 0, 0))
text_game_over_rect = text_game_over.get_rect(center=(width // 2, height // 2))
screen.blit(text_game_over, text_game_over_rect)


# Actualizar la pantalla
pygame.display.flip()

# Esperar respuesta del jugador
while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                game_over = False
                reset_game()