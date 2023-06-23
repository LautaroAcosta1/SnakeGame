import pygame
from pygame.math import Vector2
import random
import os
import sys



#ventana:
ANCHO = 720
ALTO = 480



#imagenes:
SNAKE_BODY = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\acost\OneDrive\Escritorio\snake\img\snakebody.png")), (20, 20))
APPLE = pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\acost\OneDrive\Escritorio\snake\img\manzana.png")), (20, 20))
MENU_BACKGROUND = pygame.image.load(r"C:\Users\acost\OneDrive\Escritorio\snake\img\menuBackground.jpg")
MENU_BACKGROUND = pygame.transform.scale(MENU_BACKGROUND, (720, 480))
SNAKE_HEAD = []
for x in range (1, 5):
    SNAKE_HEAD += [pygame.transform.scale(pygame.image.load(os.path.join(r"C:\Users\acost\OneDrive\Escritorio\snake\img\SnakeHead" + str(x) + ".png")), (20, 20))]



WIN = pygame.display.set_mode((ANCHO, ALTO))






#-------------------- JUEGO --------------------
class Snake:
    def __init__(self):
        self.body = [Vector2(20, 100), Vector2(20, 110), Vector2(20, 120)]
        self.direction = Vector2(0,-20)
        self.add = False


    def draw(self):
        for bloque in self.body:
            WIN.blit(SNAKE_BODY, (bloque.x, bloque.y))

        if self.direction == Vector2 (0, -20):
            WIN.blit(SNAKE_HEAD[0], (self.body[0].x, self.body[0].y))

        if self.direction == Vector2 (0, 20):
            WIN.blit(SNAKE_HEAD[2], (self.body[0].x, self.body[0].y))

        if self.direction == Vector2 (20, 0):
            WIN.blit(SNAKE_HEAD[1], (self.body[0].x, self.body[0].y))

        if self.direction == Vector2 (-20, 0):
            WIN.blit(SNAKE_HEAD[3], (self.body[0].x, self.body[0].y))


    #movimiento de la snake.
    def move(self):
        if self.add == True:
            body_copy = self.body
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.add = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]


    def move_up(self):
        self.direction = Vector2(0, -20)

    def move_down(self):
        self.direction = Vector2(0, 20)

    def move_right(self):
        self.direction = Vector2(20, 0)

    def move_left(self):
        self.direction = Vector2(-20, 0)


    #maneras de morir de la snake.
    def die(self):

        #snake choca con cualquiera de los bordes.
        if self.body[0].x >= ANCHO + 20 or self.body[0].y >= ALTO + 20 or self.body[0].x <= -20 or self.body[0].y <= -20:
            return True

        #snake se toca a si misma.
        for i in self.body[1:]:
            if self.body[0] == i:
                return True





class Apple:
    def __init__(self):
        self.generate()


    def draw(self):
        WIN.blit(APPLE, (self.pos.x, self.pos.y))


    def generate(self):
        self.x = random.randrange(0, ANCHO / 20)
        self.y = random.randrange(0, ALTO / 20)
        self.pos = Vector2(self.x * 20, self.y * 20)


    def check_collision(self, snake):
        if snake.body[0] == self.pos:
            self.generate()
            snake.add = True
            return True
        for bloque in snake.body[1:]:
            if self.pos == bloque:
                self.generate()
        return False







#-------------------- MENU --------------------
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    WIN.blit(text_surface, text_rect)







#-------------------- FINAL --------------------
def score_guardado():
    archivo = open("scoreRecord.txt", "r")
    score_guardado = archivo.read()
    archivo.close()
    if score_guardado.strip():
        return int(score_guardado)
    else:
        return 0



def score_record(score):
    with open("scoreRecord.txt", "w") as archivo:
        archivo.write(str(score))
    return True












