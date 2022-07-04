import random
import pygame
pygame.font.init()

WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Role Playing Game")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (70, 130, 255)
FPS = 5

IMAGE_WIDTH = 256
IMAGE_HEIGHT = 256

ARCHER_ALLY_IMAGE = pygame.image.load("PyGame\Archer.png")
KNIGHT_ALLY_IMAGE = pygame.image.load("PyGame\Knight.png")
MAGE_ALLY_IMAGE = pygame.image.load("PyGame\Mage.png")
ENEMY_IMAGE = pygame.image.load("PyGame\Enemy.png")
BACKGROUND_IMAGE = pygame.image.load("PyGame\Background.jpg")

ARCHER_ALLY = pygame.transform.scale(ARCHER_ALLY_IMAGE, (IMAGE_WIDTH, IMAGE_HEIGHT))
KNIGHT_ALLY = pygame.transform.scale(KNIGHT_ALLY_IMAGE, (IMAGE_WIDTH, IMAGE_HEIGHT))
MAGE_ALLY = pygame.transform.scale(MAGE_ALLY_IMAGE, (200, IMAGE_HEIGHT))
ENEMY = pygame.transform.scale(ENEMY_IMAGE, (IMAGE_WIDTH * 1.5 , IMAGE_HEIGHT * 1.5))
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (1920, 1080))
font = pygame.font.SysFont("comicsans", 30, True)

current_fighter = 1
total_fighters = 4
action_cooldown = 0
action_wait_time = 90

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


class Knight(Objects):
    def __init__(self, x, y, name, health, max_health, mana, attack, defense, speed, exp, level):
        super().__init__(x, y, name, health, max_health, mana, attack, defense, speed, exp, level)
        self._image = KNIGHT_ALLY

    def attack(self, enemy):
        enemy._health -= self._attack


class Archer(Objects):
    def __init__(self, x, y, name, health, max_health, mana, attack, defense, speed, exp, level):
        super().__init__(x, y, name, health, max_health, mana, attack, defense, speed, exp, level)
        self._image = ARCHER_ALLY

    def attack(self, enemy):
        enemy._health -= self._attack


class Mage(Objects):
    def __init__(self, x, y, name, health, max_health, mana, attack, defense, speed, exp, level):
        super().__init__(x, y, name, health, max_health, mana, attack, defense, speed, exp, level)
        self._image = MAGE_ALLY

    def attack(self, enemy):
        enemy._health -= self._attack


class Enemy(Objects):
    def __init__(self, x, y, name, health, max_health, mana, attack, defense, speed, exp, level):
        super().__init__(x, y, name, health, max_health, mana, attack, defense, speed, exp, level)
        self._image = ENEMY
    
    def attack(self):
        turn = random.randint(1, 3)
        if turn == 1:
            knight._health -= self._attack
        elif turn == 2:
            archer._health -= self._attack
        else:
            mage._health -= self._attack


class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self._x = x
        self._y = y
        self._hp = hp
        self._max_hp = max_hp
    
    def draw(self, hp):

        self._hp = hp
        ratio = self._hp / self._max_hp
        pygame.draw.rect(WIN, RED, [self._x, self._y, 200, 22])
        pygame.draw.rect(WIN, GREEN, [self._x, self._y, 200 * ratio, 22])

def draw_window():
    WIN.blit(BACKGROUND, (0, 0))
    knight.draw()
    archer.draw()
    mage.draw()
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
    draw_text(f"{knight._name}, HP: {knight._health}", font, BLUE, knight._x, knight._y- 40)
    draw_text(f"{archer._name}, HP: {archer._health}", font, BLUE, archer._x, archer._y- 40)
    draw_text(f"{mage._name}, HP: {mage._health}", font, BLUE, mage._x, mage._y- 40)
    draw_text(f"{enemy._name}, HP: {enemy._health}", font, RED, enemy._x+ 120, enemy._y- 60)

knight = Knight(600, 700, "Knight", 100, 100, 0, 10, 5, 10, 0, 1)
archer = Archer(50, 700, "Archer", 80, 80, 5, 7, 3, 25, 0, 1)
mage = Mage(350, 700, "Mage", 75, 75, 20, 10, 2, 15, 0, 1)
enemy = Enemy(1400, 580, "Enemy", 350, 350, 0, 10, 10, 5, 0, 1)

knight_healthbar = HealthBar(knight._x+ 20, knight._y - 70, knight._health, knight._max_health)
archer_healthbar = HealthBar(archer._x, archer._y - 70, archer._health, archer._max_health)
mage_healthbar = HealthBar(mage._x, mage._y - 70, mage._health, mage._max_health)
enemy_healthbar = HealthBar(enemy._x + 130, enemy._y - 100, enemy._health, enemy._max_health)

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
            knight.attack(enemy)
            enemy.check_alive()
            if enemy._alive == False:
                print("Enemy is dead")
                print("You win")
                break
        if archer._alive == True:
            archer.attack(enemy)
            enemy.check_alive()
            if enemy._alive == False:
                print("Enemy is dead")
                print("You win")
                break
        if mage._alive == True:
            mage.attack(enemy)
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
