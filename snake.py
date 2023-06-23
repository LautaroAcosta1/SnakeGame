import pygame
from funciones import *
from pygame.math import Vector2
import random
import os
import sys



pygame.init()
pygame.display.set_caption("SNAKE GAME")


#sonidos:
EAT_SOUND = pygame.mixer.Sound(r"C:\Users\acost\OneDrive\Escritorio\snake\sound\coin.wav")
CRASH_SOUND = pygame.mixer.Sound(r"C:\Users\acost\OneDrive\Escritorio\snake\sound\lose.mp3")

#musica:
pygame.mixer.music.load(r"C:\Users\acost\OneDrive\Escritorio\snake\sound\musicBackground.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

#fuente:
SCORE_TEXT = pygame.font.Font(r"C:\Users\acost\OneDrive\Escritorio\snake\fonts\Acme-Regular.ttf", 20)
font_title = pygame.font.Font(r"C:\Users\acost\OneDrive\Escritorio\snake\fonts\Acme-Regular.ttf", 68)
font_menu = pygame.font.Font(r"C:\Users\acost\OneDrive\Escritorio\snake\fonts\CarterOne-Regular.ttf", 36)
font_final = pygame.font.Font(r"C:\Users\acost\OneDrive\Escritorio\snake\fonts\PressStart2P-Regular.ttf", 68)

#colores:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GREEN2 = (175, 215, 70)




#-------------------- FINAL --------------------
def final():
    menu_options = ["Volver a jugar", "Opciones", "Volver al inicio"]
    selected_option = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        # Lógica para la opción "Jugar"
                        main()
                        print("Jugando...")
                    elif selected_option == 1:
                        # Lógica para la opción "Opciones"
                        print("Ingresando a opciones...")
                    elif selected_option == 2:
                        # Lógica para la opción "Volver a inicio"
                        menu()
                        print("Volviendo al inicio...")

        WIN.fill(GREEN2)
        draw_text("GAME OVER", font_final, BLACK, ANCHO // 2, 100)


        archivo = open("scoreRecord.txt", "r")
        record = archivo.read()
        draw_text("Tu record es: " + record, font_menu, BLACK, ANCHO // 2, 400)



        for i, option in enumerate(menu_options):
            if i == selected_option:
                draw_text(option, font_menu, WHITE, ANCHO // 2, 190 + i * 50)
            else:
                draw_text(option, font_menu, BLACK, ANCHO // 2, 190 + i * 50)
        pygame.display.update()





#-------------------- JUEGO --------------------
def main():

    snake = Snake()
    apple = Apple()
    score = 0
    clock = pygame.time.Clock()
    fps = 9
    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN and snake.direction.y != 20:
                if event.key == pygame.K_UP:
                    snake.move_up()

            if event.type == pygame.KEYDOWN and snake.direction.y != -20:
                if event.key == pygame.K_DOWN:
                    snake.move_down()

            if event.type == pygame.KEYDOWN and snake.direction.x != -20:
                if event.key == pygame.K_RIGHT:
                    snake.move_right()

            if event.type == pygame.KEYDOWN and snake.direction.x != 20:
                if event.key == pygame.K_LEFT:
                    snake.move_left()

        ##fondo.
        WIN.fill(GREEN2)

        snake.draw()
        apple.draw()
        snake.move()

        if apple.check_collision(snake):
            score += 1
            fps += 0.25
            EAT_SOUND.play()


        if snake.die():
            scoreRecord = score_guardado()

            if score > scoreRecord:
                score_record(score)

            CRASH_SOUND.play()
            final()


        text = SCORE_TEXT.render("Score: {}".format(score), 1, (WHITE))
        WIN.blit(text, (ANCHO - text.get_width() - 20, 20))
        pygame.display.update()







#-------------------- MENU --------------------
def menu():
    menu_options = ["Jugar", "Opciones", "Salir"]
    selected_option = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        # Lógica para la opción "Jugar"
                        main()
                        print("Jugando...")
                    elif selected_option == 1:
                        # Lógica para la opción "Opciones"
                        print("Ingresando a opciones...")
                    elif selected_option == 2:
                        # Lógica para la opción "Salir"
                        pygame.quit()
                        sys.exit()

        WIN.blit(MENU_BACKGROUND, (0, 0))
        draw_text("SNAKE", font_title, BLACK, ANCHO // 2, 100)
        for i, option in enumerate(menu_options):
            if i == selected_option:
                draw_text(option, font_menu, GREEN, ANCHO // 2, 220 + i * 60)
            else:
                draw_text(option, font_menu, BLACK, ANCHO // 2, 220 + i * 60)
        pygame.display.update()

menu()
























