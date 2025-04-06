import time
from pygame.locals import *
import pygame

guanyador = 0
AMPLADA = 800
ALTURA = 600
BACKGROUND_IMAGE = 'assets/fons.png'
MUSICA_FONS = 'assets/music.mp3'
WHITE = (255,255,255)
MAGENTA =(255,0,255)
NEGRE = (0,0,0)
CYAN = (0,255,255)
RED = (255,0,0)
INDIGO = (75,0,130)

# Pantalles:
# Pantalla 1 = Menú
# pantalla 2 = Credits
# Pantalla 3 = JOC
# Pantalla 4 = GAMEOVER
pantalla_actual = 1


# vides jugador 1:
vides_imatge1=pygame.image.load('assets/vida.png')
pygame.init()
pygame.mixer.music.load('assets/musicmenu.mp3')
# Jugador 1:
player_image = pygame.image.load('assets/pixilart-drawing.png')
player_rect = player_image.get_rect(midbottom=(AMPLADA // 2, ALTURA - 10))
velocitat_nau = 4
vida_jugador1= 3

# vides jugador 2:
vides_imatge2=pygame.image.load('assets/vida2.png')
# Jugador 2:
player_image2 = pygame.image.load('assets/nauenemiga.png')
player_rect2 = player_image2.get_rect(midbottom=(AMPLADA // 2, ALTURA - 500))
velocitat_nau2 = 4
vida_jugador2= 3
# Bala rectangular blanca:
bala_imatge = pygame.Surface((4,10)) #definim una superficie rectangle de 4 pixels d'ample i 10 d'alçada
bala_imatge.fill(WHITE) #pintem la superficie de color blanc
bales_jugador1 = [] #llista on guardem les bales del jugador 1
bales_jugador2 = [] #llista on guardem les bales del jugador 2
velocitat_bales = 20
temps_entre_bales = 500 #1 segon
temps_ultima_bala_jugador1 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 1
temps_ultima_bala_jugador2 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 2


pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("SPACE FIGHT")

# Control de FPS
clock = pygame.time.Clock()
fps = 30


pygame.mixer.music.load('assets/musicmenu.mp3')
pygame.mixer.music.play()


def imprimir_pantalla_fons(image):
    # Imprimeixo imatge de fons:
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))

def mostrar_menu():


    imprimir_pantalla_fons('assets/mennu.png')
    font1 = pygame.font.SysFont("tlwgtypist", 70)
    font2 = pygame.font.SysFont("gidudu", 40)
    img1 = font1.render("SPACE FIGHT", True, CYAN)
    img2 = font2.render("1. Jugar", True, NEGRE)
    img3 = font2.render("2. Crèdits", True, NEGRE)
    img4 = font2.render("3. Sortir", True, NEGRE)
    pantalla.blit(img1, (200, 30))
    pantalla.blit(img2, (250, 230))
    pantalla.blit(img3, (250, 280))
    pantalla.blit(img4, (250, 330))


def mostrar_credits():
    imprimir_pantalla_fons('assets/credits.png')
    font1 = pygame.font.SysFont(None, 40)
    font2 = pygame.font.SysFont(None, 25)
    img1 = font1.render("CRÈDITS", True, INDIGO)
    img2 = font2.render("PROGRAMACIÓ: Carla Rodriguez i Xavi Sancho", True, INDIGO)
    img3 = font2.render("Gràfic: Carla Rodriguez", True, INDIGO)
    img4 = font2.render("Música: Stranger Things", True, INDIGO)
    img6 = font2.render("SPACE FIGHT", True, INDIGO)
    pantalla.blit(img1, (335, 130))
    pantalla.blit(img6, (335, 90))
    pantalla.blit(img3, (300, 230))
    pantalla.blit(img2, (200, 290))
    pantalla.blit(img4, (300, 330))



while True:
    #contador
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # Pantalla gameover
        if pantalla_actual == 4:

            # Restauro vida dels jugadors
            vida_jugador1 = 3
            vida_jugador2 = 3
            # Elimino les bales del joc
            for i in bales_jugador1:
                bales_jugador1.remove(i)
            for i in bales_jugador2:
                bales_jugador2.remove(i)
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pygame.mixer.music.load('assets/musicmenu.mp3')
                    pygame.mixer.music.play()
                    pantalla_actual = 1

        # Pantalla crèdits
        if pantalla_actual == 2:
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pantalla_actual = 1
        # Pantalla menú
        if pantalla_actual == 1:
            if event.type == KEYDOWN:
                print()
                if event.key == K_1:
                    pantalla_actual = 3
                    pygame.mixer.music.load('assets/musicajoc.mp3')

                if event.key == K_2:
                    pantalla_actual = 2
                    pygame.mixer.music.load('assets/musicmenu.mp3')
                if event.key == K_3:
                    pygame.quit()
                pygame.mixer.music.play()



        so_dispar = pygame.mixer.Sound('assets/bala1.mp3')
        so_dispar.set_volume(100)
        so_dispar2 = pygame.mixer.Sound('assets/bala2.mp3')
        so_dispar2.set_volume(100)

        # controlar trets de les naus
        if event.type == KEYDOWN:
            # jugador 1
            if event.key == K_w and current_time - temps_ultima_bala_jugador1 >= temps_entre_bales:
                so_dispar.play()
                bales_jugador1.append(pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10))
                temps_ultima_bala_jugador1 = current_time

            # jugador 2
            if event.key == K_UP and current_time - temps_ultima_bala_jugador2 >= temps_entre_bales:
                so_dispar2.play()
                bales_jugador2.append(pygame.Rect(player_rect2.centerx - 2, player_rect2.bottom - 10, 4, 10))
                temps_ultima_bala_jugador2 = current_time




    # PANTALLA MENÚ

    if pantalla_actual == 1:
        mostrar_menu()
    # PANTALLA CREDITS
    elif pantalla_actual == 2:
        mostrar_credits()
    elif pantalla_actual == 2:
        mostrar_credits()

    # PANTALLA GAME OVER
    elif pantalla_actual == 4:
        imprimir_pantalla_fons('assets/gameover.png')
        text = "Jugador " + str(guanyador) + " guanya!"
        font = pygame.font.SysFont(None, 100)
        img = font.render(text, True, NEGRE)
        pantalla.blit(img, (109, 450))



    if pantalla_actual == 3:
        # Moviment del jugador 1
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            player_rect.x -= velocitat_nau
        if keys[K_d]:
            player_rect.x += velocitat_nau
        # Moviment del jugador 2
        if keys[K_LEFT]:
            player_rect2.x -= velocitat_nau2
        if keys[K_RIGHT]:
            player_rect2.x += velocitat_nau2



        # Mantenir al jugador dins de la pantalla:
        player_rect.clamp_ip(pantalla.get_rect())
        player_rect2.clamp_ip(pantalla.get_rect())

        #dibuixar el fons:
        imprimir_pantalla_fons(BACKGROUND_IMAGE)

        #Actualitzar i dibuixar les bales del jugador 1:
        for bala in bales_jugador1: # bucle que recorre totes les bales
            bala.y -= velocitat_bales # mou la bala
            if bala.bottom < 0 or bala.top > ALTURA: # comprova que no ha sortit de la pantalla
                bales_jugador1.remove(bala) # si ha sortit elimina la bala
            else:
                pantalla.blit(bala_imatge, bala) # si no ha sortit la dibuixa
            # Detectar col·lisions jugador 2:
            if player_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                print("BOOM 1!")
                bales_jugador1.remove(bala)  # eliminem la bala
                vida_jugador2 = vida_jugador2 - 1
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1

        # Actualitzar i dibuixar les bales del jugador 2:
        for bala in bales_jugador2:
            bala.y += velocitat_bales
            if bala.bottom < 0 or bala.top > ALTURA:
                bales_jugador2.remove(bala)
            else:
                pantalla.blit(bala_imatge, bala)
            # Detectar col·lisions jugador 1:
            if player_rect.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                print("BOOM 2!")
                bales_jugador2.remove(bala)  # eliminem la bala
                vida_jugador1= vida_jugador1 - 1
                # mostrem una explosió
                # eliminem el jugador 1 (un temps)
                # anotem punts al jugador 1

        #dibuixar els jugadors:
        pantalla.blit(player_image, player_rect)
        pantalla.blit(player_image2, player_rect2)
        # dibuixar vidajugador1
        if vida_jugador1 >= 3:
            pantalla.blit(vides_imatge1,(680,560))
        if vida_jugador1 >= 2:
            pantalla.blit(vides_imatge1, (710, 560))
        if vida_jugador1 >= 1:
            pantalla.blit(vides_imatge1, (740, 560))

            # dibuixar vidajugador2
        if vida_jugador2 >= 3:
            pantalla.blit(vides_imatge2, (680, 30))
        if vida_jugador2 >= 2:
            pantalla.blit(vides_imatge2, (710, 30))
        if vida_jugador2 >= 1:
            pantalla.blit(vides_imatge2, (740, 30))

        if vida_jugador1 <=0 or vida_jugador2 <= 0:
            guanyador = 1
            if vida_jugador1 <= 0:
                guanyador = 2
            pygame.mixer.music.load('assets/gameover.mp3')
            pygame.mixer.music.play()
            pantalla_actual = 4


    pygame.display.update()
    clock.tick(fps)