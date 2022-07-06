import pygame
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60
font = pygame.font.SysFont('Times New Roman', 26)
game_end = pygame.font.SysFont('Times New Roman', 70)

current_fighter = 1
total_fighters = 4
action_cooldown = 0
action_wait_time = 120
attack = False

clicked = False
game_over = 0
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (170, 170, 170)

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('RPG Battle')

background_img = pygame.image.load('PyGame\Background.jpg')
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))

def draw_bg():
    screen.blit(background_img, (0, 0))

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

def draw_game_over():
    draw_text("DEFEAT", game_end, red, screen_width/2 - 100, screen_height/4)

def draw_win():
    draw_text("VICTORY", game_end, green, screen_width/2 - 100, screen_height/4)

def draw_name():
    draw_text(f"Knight, HP: {knight.hp}", font, white, knight.x+166, knight.y+ 215)
    draw_text(f"Mage, HP: {mage.hp}", font, white, mage.x+170, mage.y+ 100)
    draw_text(f"Archer, HP: {archer.hp}", font, white, archer.x+155, archer.y+ 200)
    draw_text(f"Enemy, HP: {enemy.hp}", font, white, enemy.x+ 200, enemy.y + 160)


class Fighter():
    def __init__(self, x, y, name, max_hp, strength):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        temp_list = []
        self.x = x
        self.y = y
        for i in range(8):
            img = pygame.image.load(f'PyGame\KnightImages\Idle{i}.png')
            img = pygame.transform.scale(img, (500, 500))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(20):
            img = pygame.image.load(f'PyGame\KnightImages\Attack_{i}.png')
            img = pygame.transform.scale(img, (500, 500))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        temp_list = []
        for i in range(6):
            img = pygame.image.load(f'PyGame\KnightImages\Hit_{i}.png')
            img = pygame.transform.scale(img, (500, 500))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        temp_list = []
        for i in range(10):
            img = pygame.image.load(f'PyGame\KnightImages\Dead_{i}.png')
            img = pygame.transform.scale(img, (500, 500))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]

    def attack(self):
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        enemy.hp -= damage
        if enemy.hp < 1:
            enemy.hp = 0
            enemy.alive = False
            enemy.dead()
        else:
            enemy.hurt()

    def idle(self):
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def hurt(self):
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def dead(self):
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        animation_cooldown = 40
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.idle()


class Mage():
    def __init__(self, x, y, name, max_hp, strength):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        temp_list = []
        self.x = x
        self.y = y
        for i in range(9):
            img = pygame.image.load(f'PyGame\MageImages\Idle{i}.png')
            img = pygame.transform.scale(img, (500, 500))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(19):
            img = pygame.image.load(f'PyGame\MageImages\Attack_{i}.png')
            img = pygame.transform.scale(img, (500, 500))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        temp_list = []
        for i in range(6):
            img = pygame.image.load(f'PyGame\MageImages\Hit_{i}.png')
            img = pygame.transform.scale(img, (500, 500))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        temp_list = []
        for i in range(17):
            img = pygame.image.load(f'PyGame\MageImages\Dead_{i}.png')
            img = pygame.transform.scale(img, (500, 500))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]#

    def attack(self):
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        enemy.hp -= damage
        if enemy.hp < 1:
            enemy.hp = 0
            enemy.alive = False
            enemy.dead()
        else:
            enemy.hurt()

    def idle(self):
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def hurt(self):
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def dead(self):
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        animation_cooldown = 40
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.idle()


class Enemy():
    def __init__(self, x, y, name, max_hp, strength):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        temp_list = []
        self.x = x
        self.y = y
        for i in range(13):
            img = pygame.image.load(f'PyGame\EnemyImages\Idle{i}.png')
            img = pygame.transform.scale(img, (540, 540))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        temp_list = []
        for i in range(6, 21):
            img = pygame.image.load(f'PyGame\EnemyImages\Attack_{i}.png')
            img = pygame.transform.scale(img, (540, 540))
            temp_list.append(img)
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(12):
            img = pygame.image.load(f'PyGame\EnemyImages\Hit_{i}.png')
            img = pygame.transform.scale(img, (540, 540))
            temp_list.append(img)
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(15):
            img = pygame.image.load(f'PyGame\EnemyImages\Dead_{i}.png')
            img = pygame.transform.scale(img, (540, 540))
            temp_list.append(img)
            temp_list.append(img)
        self.animation_list.append(temp_list)

    def attack_attack(self):
        rand = random.randint(1, 5)
        damage = self.strength + rand
        choose = random.randint(0, 2)
        if choose == 0:
            if knight.hp > 0:
                knight.hp -= damage
                if knight.hp < 1:
                    knight.hp = 0
                    knight.alive = False
                    knight.dead()
                else:
                    knight.hurt()
            else:
                self.attack_attack()
        elif choose == 1:
            if mage.hp > 0:
                mage.hp -= damage
                if mage.hp < 1:
                    mage.hp = 0
                    mage.alive = False
                    mage.dead()
                else:
                    mage.hurt()
            else:
                self.attack_attack()
        elif choose == 2:
            if archer.hp > 0:
                archer.hp -= damage
                if archer.hp < 1:
                    archer.hp = 0
                    archer.alive = False
                    archer.dead()
                else:
                    archer.hurt()
            else:
                self.attack_attack()

    def attack(self):
        i = random.randint(0, 2)
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.attack_attack()
        while i > 0:
            self.attack_attack()
            i -= 1


    def idle(self):
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def hurt(self):
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def dead(self):
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def update(self):
        animation_cooldown = 40
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.idle()

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


class Archer():
    def __init__(self, x, y, name, max_hp, strength):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        temp_list = []
        self.x = x
        self.y = y
        for i in range(8):
            img = pygame.image.load(f'PyGame\ArcherImages\Idle{i}.png')
            img = pygame.transform.scale(img, (500, 500))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(17):
            img = pygame.image.load(f'PyGame\ArcherImages\Attack_{i}.png')
            img = pygame.transform.scale(img, (500, 500))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        temp_list = []
        for i in range(5):
            img = pygame.image.load(f'PyGame\ArcherImages\Hit_{i}.png')
            img = pygame.transform.scale(img, (500, 500))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        temp_list = []
        for i in range(12):
            img = pygame.image.load(f'PyGame\ArcherImages\Dead_{i}.png')
            img = pygame.transform.scale(img, (500, 500))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]

    def attack(self):
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        enemy.hp -= damage
        if enemy.hp < 1:
            enemy.hp = 0
            enemy.alive = False
            enemy.dead()
        else:
            enemy.hurt()

    def idle(self):
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def hurt(self):
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def dead(self):
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        animation_cooldown = 40
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.idle()


class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp):
        self.hp = hp
        ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, green, (self.x, self.y, 150 * ratio, 20))


knight = Fighter(450, 160, 'Knight', 40, random.randint(8, 12))
mage = Mage(-100, 200, 'Mage', 40, random.randint(6, 14))
archer = Archer(150, 160, 'Archer', 40, 10)
enemy = Enemy(780, 163, 'Enemy', 150, 7)

knight_health_bar = HealthBar(knight.x + 170, knight.y + 250, knight.hp, knight.max_hp)
mage_health_bar = HealthBar(mage.x + 170, mage.y + 140, mage.hp, mage.max_hp)
archer_health_bar = HealthBar(archer.x + 160, archer.y + 240, archer.hp, archer.max_hp)
enemy_health_bar = HealthBar(enemy.x + 200, enemy.y + 200, enemy.hp, enemy.max_hp)

run = True
while run:

    clock.tick(fps)
    draw_bg()

    knight_health_bar.draw(knight.hp)
    enemy_health_bar.draw(enemy.hp)
    mage_health_bar.draw(mage.hp)
    archer_health_bar.draw(archer.hp)
    draw_name()

    knight.update()
    knight.draw()
    enemy.update()
    enemy.draw()
    mage.update()
    mage.draw()
    archer.update()
    archer.draw()
    enemy_list = [enemy]

    attack = False
    potion = False
    target = None

    pygame.mouse.set_visible(True)
    pos = pygame.mouse.get_pos()
    for count, enemy in enumerate(enemy_list):
        if clicked == True:
            attack = True
            target = enemy_list[count]

    if game_over ==  0 or game_over == -1:	
        if knight.alive == True:
            if current_fighter == 1:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    if attack == True and enemy != None:
                        knight.attack()
                        if archer.hp > 0:
                            current_fighter = 2
                            action_cooldown = 0
                        elif mage.hp > 0:
                            current_fighter = 3
                            action_cooldown = 0
                        else:
                            current_fighter = 4
                            action_cooldown = 0
                        print(f"After Knight: {current_fighter}")

    if game_over ==  0 or game_over == -1 :	
        if archer.alive == True:
            if current_fighter == 2:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    if attack == True and enemy != None:
                        archer.attack()
                        if mage.hp > 0:
                            current_fighter = 3
                            action_cooldown = 0
                        else:
                            current_fighter = 4
                            action_cooldown = 0
                        print(f"After Archer: {current_fighter}")

    if game_over ==  0 or game_over == -1:
        if mage.alive == True:
            if current_fighter == 3:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    if attack == True and enemy != None:
                        mage.attack()
                        current_fighter = 4
                        action_cooldown = 0
                        print(f"After Mage: {current_fighter}")

    if game_over ==  0 or game_over == -1:
        if enemy.alive == True:
            if current_fighter == 4:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    enemy.attack()
                    if knight.hp > 0:
                        current_fighter = 1
                        action_cooldown = 0
                    elif archer.hp > 0:
                        current_fighter = 2
                        action_cooldown = 0
                    else:
                        current_fighter = 3
                        action_cooldown = 0
                    print(f"After Enemy: {current_fighter}")
        else:
            game_over = 1
    

    if mage.alive == False and knight.alive == False and archer.alive == False:
        game_over = -3

    if game_over == 1:
        draw_win()
    elif game_over == -3:
        draw_game_over()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False

    pygame.display.update()


pygame.quit()