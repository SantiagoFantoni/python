
import pygame
import sys
pygame.init()
pygame.font.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


vel = 4


size = (800, 600)

ventana = pygame.display.set_mode(size)

char = pygame.transform.scale(pygame.image.load(
    "assets/char.jpg").convert_alpha(), (64, 64))
enemy = pygame.transform.scale(pygame.image.load(
    "assets/enemy.png").convert_alpha(), (64, 64))


clock = pygame.time.Clock()
pygame.display.set_caption("Juego")

FONT = pygame.font.Font("assets/Fonts/Roboto-Regular.ttf",
                        30)  # La fuente y su tamaño


class Entity:

    def __init__(self, x, y, sprite, health):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.health = health
        self.speed = 4
        self.atk_speed = 20
        self.mask = pygame.mask.from_surface(self.sprite)

    def dibujar(self, where):
        where.blit(self.sprite, (self.x, self.y))

    def collision(self, obj):
        return Collide(obj, self)


class Player(Entity):
    def __init__(self, x, y, sprite, health):
        super().__init__(x, y, sprite, health)

        self.maxHealth = health


def Collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


player = Player(400, 300, char, 100)
enemy_1 = Entity(600, 300, enemy, 100)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        enemy_1.x += enemy_1.speed
    if keys[pygame.K_d]:
        enemy_1.x -= enemy_1.speed
    if keys[pygame.K_w]:
        enemy_1.y += enemy_1.speed
    if keys[pygame.K_s]:
        enemy_1.y -= enemy_1.speed

    ventana.fill(BLACK)
    # ----ZONA DE DIBUJO----

    player.dibujar(ventana)
    enemy_1.dibujar(ventana)

    # que escribir en el label y su color
    vidas_label = FONT.render(
        f"Vida:{player.health}/{player.maxHealth}", 1, (RED))
    ventana.blit(vidas_label, (10, 10))  # Donde dibujar el label
    # ---ZONA DE DIBUJO

    # actualiza pantalla
    pygame.display.flip()
    clock.tick(30)
