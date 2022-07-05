import random
import pygame
import PySimpleGUI as gui
pygame.font.init()
gui.theme("Black")  

WIDTH, HEIGHT = 1920 / 2, 1080 / 2
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Role Playing Game")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (70, 130, 255)
FPS = 15

IMAGE_WIDTH = 128
IMAGE_HEIGHT = 128

ARCHER_ALLY_IMAGE = pygame.image.load("PyGame\Archer.png")
ENEMY_IMAGE = pygame.image.load("PyGame\Enemy.png")
BACKGROUND_IMAGE = pygame.image.load("PyGame\Background.jpg")

BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (1920 / 2, 1080 / 2))
font = pygame.font.SysFont("comicsans", 15, True)


class Objects():
    def __init__(self, x, y, name, health, max_health, mana, attack, defense, speed, exp, level):
        self._name = name
        self._health = health
        self._max_health = max_health
        self._mana = mana
        self._attack = attack
        self._defense = defense
        self._speed = speed
        self._exp = exp
        self._level = level
        self._alive = True
        self._x = x
        self._y = y
        self._image = "image"

    def draw(self):
        WIN.blit(self._image, (self._x, self._y))


    def check_alive(self):
        if self._health <= 0:
            self._health = 0
            self._alive = False
        return self._alive

    def attack(self):
        return


class Knight(Objects):
    def __init__(self, x, y, name, health, max_health, mana, attack, defense, speed, exp, level):
        super().__init__(x, y, name, health, max_health, mana, attack, defense, speed, exp, level)
        self._image = ("PyGame\KnightImages\A.png")
        self._image_number = 0

    def update_image(self):
        if self._image_number == 0:
            self._image = pygame.image.load("PyGame\KnightImages\A.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 2.5, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 1:
            self._image = pygame.image.load("PyGame\KnightImages\B.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 2.5, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 2:
            self._image = pygame.image.load("PyGame\KnightImages\C.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 2.5, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 3:
            self._image = pygame.image.load("PyGame\KnightImages\D.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 2.5, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 4:
            self._image = pygame.image.load("PyGame\KnightImages\E.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 2.5, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 5:
            self._image = pygame.image.load("PyGame\KnightImages\F.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 2.5, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 6:
            self._image = pygame.image.load("PyGame\KnightImages\G.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 2.5, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 7:
            self._image = pygame.image.load("PyGame\KnightImages\H.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 2.5, IMAGE_HEIGHT * 3))
            self._image_number += 1
        else:
            self._image_number = 0

        KNIGHT_ALLY_IMAGE = self._image 


class Archer(Objects):
    def __init__(self, x, y, name, health, max_health, mana, attack, defense, speed, exp, level):
        super().__init__(x, y, name, health, max_health, mana, attack, defense, speed, exp, level)
        self._image = ("PyGame\KnightImages\A.png")
        self._image_number = 0

    def update_image(self):
        if self._image_number == 0:
            self._image = pygame.image.load("PyGame\ArcherImages\A.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 2.5, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 1:
            self._image = pygame.image.load("PyGame\ArcherImages\B.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 2.5, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 2:
            self._image = pygame.image.load("PyGame\ArcherImages\C.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 2.5, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 3:
            self._image = pygame.image.load("PyGame\ArcherImages\D.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 2.5, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 4:
            self._image = pygame.image.load("PyGame\ArcherImages\E.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 2.5, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 5:
            self._image = pygame.image.load("PyGame\ArcherImages\F.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 2.5, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 6:
            self._image = pygame.image.load("PyGame\ArcherImages\G.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 2.5, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 7:
            self._image = pygame.image.load("PyGame\ArcherImages\H.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 2.5, IMAGE_HEIGHT * 3))
            self._image_number += 1
        else:
            self._image_number = 0

        KNIGHT_ALLY_IMAGE = self._image


class Mage(Objects):
    def __init__(self, x, y, name, health, max_health, mana, attack, defense, speed, exp, level):
        super().__init__(x, y, name, health, max_health, mana, attack, defense, speed, exp, level)
        self._image_number = 0

    def update_image(self):
        if self._image_number == 0:
            self._image = pygame.image.load("PyGame\MageImages\A.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 3, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 1:
            self._image = pygame.image.load("PyGame\MageImages\B.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 3, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 2:
            self._image = pygame.image.load("PyGame\MageImages\C.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 3, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 3:
            self._image = pygame.image.load("PyGame\MageImages\D.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 3, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 4:
            self._image = pygame.image.load("PyGame\MageImages\E.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 3, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 5:
            self._image = pygame.image.load("PyGame\MageImages\F.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 3, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 6:
            self._image = pygame.image.load("PyGame\MageImages\G.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 3, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 7:
            self._image = pygame.image.load("PyGame\MageImages\H.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 3, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 8:
            self._image = pygame.image.load("PyGame\MageImages\I.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 3, IMAGE_HEIGHT * 3))
            self._image_number += 1
        else:
            self._image_number = 0

        MAGE_ALLY_IMAGE = self._image 


class Enemy(Objects):
    def __init__(self, x, y, name, health, max_health, mana, attack, defense, speed, exp, level):
        super().__init__(x, y, name, health, max_health, mana, attack, defense, speed, exp, level)
        self._image = ("PyGame\EnemyImages\A.png")
        self._image_number = 0

    def update_image(self):
        if self._image_number == 0:
            self._image = pygame.image.load("PyGame\EnemyImages\A.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 3, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 1:
            self._image = pygame.image.load("PyGame\EnemyImages\B.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 3, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 2:
            self._image = pygame.image.load("PyGame\EnemyImages\C.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 3, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 3:
            self._image = pygame.image.load("PyGame\EnemyImages\D.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 3, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 4:
            self._image = pygame.image.load("PyGame\EnemyImages\E.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 3, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 5:
            self._image = pygame.image.load("PyGame\EnemyImages\F.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 3, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 6:
            self._image = pygame.image.load("PyGame\EnemyImages\G.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 3, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 7:
            self._image = pygame.image.load("PyGame\EnemyImages\H.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 3, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 8:
            self._image = pygame.image.load("PyGame\EnemyImages\I.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 3, IMAGE_HEIGHT * 3))
            self._image_number += 1
        elif self._image_number == 9:
            self._image = pygame.image.load("PyGame\EnemyImages\J.png")
            self._image = pygame.transform.scale(self._image, (IMAGE_WIDTH * 3, IMAGE_HEIGHT * 3))
            self._image_number += 1
        else:
            self._image_number = 0

        ENEMY_ALLY_IMAG = self._image 
    
    def attack(self):
        return


class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self._x = x
        self._y = y
        self._hp = hp
        self._max_hp = max_hp
    
    def draw(self, hp):
        self._hp = hp
        ratio = self._hp / self._max_hp
        pygame.draw.rect(WIN, RED, [self._x, self._y, 200 / 2, 22 / 2])
        pygame.draw.rect(WIN, GREEN, [self._x, self._y, 200/ 2 * ratio, 22 / 2])


def draw_window():
    WIN.blit(BACKGROUND, (0, 0))
    knight.update_image()
    knight.draw()
    archer.update_image()
    archer.draw()
    mage.update_image()
    mage.draw()
    enemy.update_image()
    enemy.draw()
    draw_name()
    knight_healthbar.draw(knight._health)
    archer_healthbar.draw(archer._health)
    mage_healthbar.draw(mage._health)
    enemy_healthbar.draw(enemy._health)
    pygame.display.update()

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    WIN.blit(img, (x, y))

def draw_name():
    draw_text(f"{knight._name}, HP: {knight._health}", font, BLUE, knight._x+100, knight._y+ 200)
    draw_text(f"{archer._name}, HP: {archer._health}", font, BLUE, archer._x+ 100, archer._y+ 180)
    draw_text(f"{mage._name}, HP: {mage._health}", font, BLUE, mage._x + 120, mage._y + 100)
    draw_text(f"{enemy._name}, HP: {enemy._health}", font, RED, enemy._x+ 120, enemy._y + 140)

knight = Knight(500 / 2, 200 / 2, "Knight", 100, 100, 0, 10, 5, 10, 0, 1)
archer = Archer(-120 / 2, 200 / 2, "Archer", 80, 80, 5, 7, 3, 25, 0, 1)
mage = Mage(100 / 2, 300 / 2, "Mage", 75, 75, 20, 10, 2, 15, 0, 1)
enemy = Enemy(1200 / 2, 250 / 2, "Enemy", 350, 350, 0, 10, 10, 5, 0, 1)

knight_healthbar = HealthBar(knight._x+110, knight._y + 180, knight._health, knight._max_health)
archer_healthbar = HealthBar(archer._x+110, archer._y + 170, archer._health, archer._max_health)
mage_healthbar = HealthBar( mage._x + 120, mage._y + 80, mage._health, mage._max_health)
enemy_healthbar = HealthBar(enemy._x + 130, enemy._y + 130, enemy._health, enemy._max_health)

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window()
        if knight._alive == True:
            knight.attack()
            enemy.check_alive()
            if enemy._alive == False:
                print("Enemy is dead")
                print("You win")
                break
            
        if enemy._alive == True:
            enemy.attack()
            knight.check_alive()
            archer.check_alive()
            mage.check_alive()
            if knight._alive or archer._alive or mage._alive == False:
                if knight._alive == False:
                    print("Knight is dead")
                if archer._alive == False:
                    print("Archer is dead")
                if mage._alive == False:
                    print("Mage is dead")
                if knight._alive == False and archer._alive == False and mage._alive == False:
                    print("You lose")
                    break
    pygame.quit()

if __name__ == "__main__":
    main()
