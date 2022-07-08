import pygame
import random
pygame.init()

#initialize parameters
clock = pygame.time.Clock()
fps = 60
font = pygame.font.SysFont('Times New Roman', 26)
game_end = pygame.font.SysFont('Times New Roman', 70)
current_fighter = 1
action_cooldown = 0
action_wait_time = 90
attack = False
run = True
clicked = False
game_over = 0

#colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (170, 170, 170)

#screen setup
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('RPG Battle')

#initialize images
background_img = pygame.image.load('PyGame\Background.jpg')
background_img = pygame.transform.scale(background_img, (screen_width, screen_height)).convert_alpha()
sword_img = pygame.image.load('PyGame\Sword.png')
sword_img = pygame.transform.scale(sword_img, (100, 100)).convert_alpha()
bow_img = pygame.image.load('PyGame\Bow.png')
bow_img = pygame.transform.scale(bow_img, (50, 100)).convert_alpha()
fire_img = pygame.image.load('PyGame\Fire.png')
fire_img = pygame.transform.scale(fire_img, (100, 100)).convert_alpha()
heart_red_img = pygame.image.load('PyGame\Heart_Red.png')
heart_red_img = pygame.transform.scale(heart_red_img, (50, 50)).convert_alpha()
heart_blue_img = pygame.image.load('PyGame\Heart_Blue.png')
heart_blue_img = pygame.transform.scale(heart_blue_img, (50, 50)).convert_alpha()
heart_green_img = pygame.image.load('PyGame\Heart_Green.png')
heart_green_img = pygame.transform.scale(heart_green_img, (50, 50)).convert_alpha()
shield_blue = pygame.image.load('PyGame\Shield_Blue.png')
shield_blue = pygame.transform.scale(shield_blue, (100, 100)).convert_alpha()
shield_red = pygame.image.load('PyGame\Shield_Red.png')
shield_red = pygame.transform.scale(shield_red, (100, 100)).convert_alpha()
shield_green = pygame.image.load('PyGame\Shield_Green.png')
shield_green = pygame.transform.scale(shield_green, (100, 100)).convert_alpha()

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
    draw_text(f"Knight, HP: {knight.hp}", font, white, knight.x+120, knight.y+ 175)
    draw_text(f"Mage, HP: {mage.hp}", font, white, mage.x+120, mage.y+ 65)
    draw_text(f"Archer, HP: {archer.hp}", font, white, archer.x+110, archer.y+ 165)
    draw_text(f"Enemy, HP: {enemy.hp}", font, white, enemy.x+ 135, enemy.y + 135)


class Objects():
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
        self.x = x
        self.y = y

    def attack(self):
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        enemy.hp -= damage
        damage_text = Damage_Text(enemy.x + 220, enemy.y + 110, str(damage), red)
        damage_text_group.add(damage_text)
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


class Knight(Objects):
    def __init__(self, x, y, name, max_hp, strength):
        super().__init__(x, y, name, max_hp, strength)
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f'PyGame\KnightImages\Idle{i}.png')
            img = pygame.transform.scale(img, (400, 400))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(20):
            img = pygame.image.load(f'PyGame\KnightImages\Attack_{i}.png')
            img = pygame.transform.scale(img, (400, 400))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        temp_list = []
        for i in range(6):
            img = pygame.image.load(f'PyGame\KnightImages\Hit_{i}.png')
            img = pygame.transform.scale(img, (400, 400))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        temp_list = []
        for i in range(10):
            img = pygame.image.load(f'PyGame\KnightImages\Dead_{i}.png')
            img = pygame.transform.scale(img, (400, 400))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x+ 200, y+ 300)


class Archer(Objects):
    def __init__(self, x, y, name, max_hp, strength):
        super().__init__(x, y, name, max_hp, strength)
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f'PyGame\ArcherImages\Idle{i}.png')
            img = pygame.transform.scale(img, (400, 400))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(17):
            img = pygame.image.load(f'PyGame\ArcherImages\Attack_{i}.png')
            img = pygame.transform.scale(img, (400, 400))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        temp_list = []
        for i in range(5):
            img = pygame.image.load(f'PyGame\ArcherImages\Hit_{i}.png')
            img = pygame.transform.scale(img, (400, 400))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        temp_list = []
        for i in range(12):
            img = pygame.image.load(f'PyGame\ArcherImages\Dead_{i}.png')
            img = pygame.transform.scale(img, (400, 400))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x + 230, y + 300)


class Mage(Objects):
    def __init__(self, x, y, name, max_hp, strength):
        super().__init__(x, y, name, max_hp, strength)
        temp_list = []
        for i in range(9):
            img = pygame.image.load(f'PyGame\MageImages\Idle{i}.png')
            img = pygame.transform.scale(img, (400, 400))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(19):
            img = pygame.image.load(f'PyGame\MageImages\Attack_{i}.png')
            img = pygame.transform.scale(img, (400, 400))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        temp_list = []
        for i in range(6):
            img = pygame.image.load(f'PyGame\MageImages\Hit_{i}.png')
            img = pygame.transform.scale(img, (400, 400))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        temp_list = []
        for i in range(17):
            img = pygame.image.load(f'PyGame\MageImages\Dead_{i}.png')
            img = pygame.transform.scale(img, (400, 400))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x + 170, y+ 250)

    def heal(self):
        heal = random.randint(7, 15)
        if healing == 1:
            knight.hp += heal
            if knight.hp > knight.max_hp:
                knight.hp = knight.max_hp
            heal_text = Heal_Text(knight.x + 210, enemy.y + 150, str(heal), green)
            heal_text_group.add(heal_text)
        elif healing == 2:
            archer.hp += heal
            if archer.hp > archer.max_hp:
                archer.hp = archer.max_hp
            heal_text = Heal_Text(archer.x + 210, enemy.y + 150, str(heal), green)
            heal_text_group.add(heal_text)
        elif healing == 3:
            mage.hp += heal
            if mage.hp > mage.max_hp:
                mage.hp = mage.max_hp
            heal_text = Heal_Text(mage.x + 210, enemy.y + 90, str(heal), green)
            heal_text_group.add(heal_text)


class Enemy(Objects):
    def __init__(self, x, y, name, max_hp, strength, defend):
        super().__init__(x, y, name, max_hp, strength)
        self.defend = defend
        temp_list = []
        for i in range(13):
            img = pygame.image.load(f'PyGame\EnemyImages\Idle{i}.png')
            img = pygame.transform.scale(img, (440, 440))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        temp_list = []
        for i in range(6, 21):
            img = pygame.image.load(f'PyGame\EnemyImages\Attack_{i}.png')
            img = pygame.transform.scale(img, (440, 440))
            temp_list.append(img)
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(12):
            img = pygame.image.load(f'PyGame\EnemyImages\Hit_{i}.png')
            img = pygame.transform.scale(img, (440, 440))
            temp_list.append(img)
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(15):
            img = pygame.image.load(f'PyGame\EnemyImages\Dead_{i}.png')
            img = pygame.transform.scale(img, (440, 440))
            temp_list.append(img)
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.rect = self.image.get_rect()
        self.rect.center = (x + 180, y + 260)

    def aoe_attack(self):
        rand = random.randint(3, 5)
        damage = self.strength + rand
        if knight.hp > 0:
                knight.hp -= damage
                damage_text = Damage_Text(knight.x + 250, enemy.y + 190, str(damage), red)
                damage_text_group.add(damage_text)
                if knight.hp < 1:
                    knight.hp = 0
                    knight.alive = False
                    knight.dead()
                    mage.strength += 3
                    archer.strength += 3
                else:
                    knight.hurt()
        if mage.hp > 0:
                mage.hp -= damage
                damage_text = Damage_Text(mage.x + 250, enemy.y + 130, str(damage), red)
                damage_text_group.add(damage_text)
                if mage.hp < 1:
                    mage.hp = 0
                    mage.alive = False
                    mage.dead()
                    knight.strength += 3
                    archer.strength += 3
                else:
                    mage.hurt()
        if archer.hp > 0:
                archer.hp -= damage
                damage_text = Damage_Text(archer.x + 240, enemy.y + 190, str(damage), red)
                damage_text_group.add(damage_text)
                if archer.hp < 1:
                    archer.hp = 0
                    archer.alive = False
                    archer.dead()
                    knight.strength += 3
                    mage.strength += 3
                else:
                    archer.hurt()

    def attack(self):
        i = random.randint(1, 3)
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        if i == 3:
            self.aoe_attack()
        else:
            i = random.randint(1, 3)
            if i == 1:
                self.attack_knight()
            elif i == 2:
                self.attack_mage()
            else:
                self.attack_archer()

    def attack_knight(self):
        rand = random.randint(1, 5)
        damage = self.strength + rand
        self.defend = 0
        if knight.hp > 0:
            knight.hp -= damage
            damage_text = Damage_Text(knight.x + 250, enemy.y + 190, str(damage), red)
            damage_text_group.add(damage_text)
            if knight.hp < 1:
                knight.hp = 0
                knight.alive = False
                knight.dead()
                mage.strength += 3
                archer.strength += 3
            else:
                knight.hurt()
        else:
            self.attack_attack()

    def attack_mage(self):
        if self.defend == 3:
            self.attack_knight()
            self.defend = 0
        else:
            rand = random.randint(1, 5)
            damage = self.strength + rand
            if mage.hp > 0:
                mage.hp -= damage
                damage_text = Damage_Text(mage.x + 250, enemy.y + 130, str(damage), red)
                damage_text_group.add(damage_text)
                if mage.hp < 1:
                    mage.hp = 0
                    mage.alive = False
                    mage.dead()
                    knight.strength += 3
                    archer.strength += 3
                else:
                    mage.hurt()
            else:
                self.attack_attack()

    def attack_archer(self):
        if self.defend == 2:
            self.attack_knight()
            self.defend = 0
        else:
            rand = random.randint(1, 5)
            damage = self.strength + rand
            if archer.hp > 0:
                archer.hp -= damage
                damage_text = Damage_Text(archer.x + 240, enemy.y + 190, str(damage), red)
                damage_text_group.add(damage_text)
                if archer.hp < 1:
                    archer.hp = 0
                    archer.alive = False
                    archer.dead()
                    knight.strength += 3
                    mage.strength += 3
                else:
                    archer.hurt()
            else:
                self.attack_attack()


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


class Damage_Text(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, colour):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(f'{damage}', True, colour)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0

    def update(self):
        self.rect.y -= 1
        self.counter += 1
        if self.counter > 20:
            self.kill()


class Heal_Text(pygame.sprite.Sprite):
    def __init__(self, x, y, heal, colour):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(f'{heal}', True, colour)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0
    
    def update(self):
        self.rect.y -= 1
        self.counter += 1
        if self.counter > 20:
            self.kill()


#initialize characters
knight = Knight(500, 260, 'Knight', 40, random.randint(8, 12))
mage = Mage(-100, 300, 'Mage', 40, random.randint(6, 14))
archer = Archer(200, 260, 'Archer', 40, 10)
enemy = Enemy(900, 263, 'Enemy', 150, 7, 0)
damage_text_group = pygame.sprite.Group()
heal_text_group = pygame.sprite.Group()

#initialize health bars
knight_health_bar = HealthBar(knight.x + 125, knight.y + 210, knight.hp, knight.max_hp)
mage_health_bar = HealthBar(mage.x + 120, mage.y + 100, mage.hp, mage.max_hp)
archer_health_bar = HealthBar(archer.x + 110, archer.y + 200, archer.hp, archer.max_hp)
enemy_health_bar = HealthBar(enemy.x + 140, enemy.y + 170, enemy.hp, enemy.max_hp)

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
    damage_text_group.update()
    damage_text_group.draw(screen)
    heal_text_group.update()
    heal_text_group.draw(screen)
    enemy.update()
    enemy.draw()
    mage.update()
    mage.draw()
    archer.update()
    archer.draw()

    attack = False
    target = None

    posx = pygame.mouse.get_pos()[0]
    posy = pygame.mouse.get_pos()[1]
    if current_fighter == 1:
        if enemy.rect.collidepoint(posx, posy):
            pygame.mouse.set_visible(False)
            screen.blit(sword_img, (posx - 50, posy - 50))
            if clicked == True:
                attack = True
                target = enemy
        elif knight.rect.collidepoint(posx, posy):
            pygame.mouse.set_visible(False)
            screen.blit(shield_blue, (posx - 50, posy - 50))
            if clicked == True:
                enemy.defend = 1
                if archer.hp > 0:
                    current_fighter = 2
                    action_cooldown = 0
                elif mage.hp > 0:
                    current_fighter = 3
                    action_cooldown = 0
                else:
                    current_fighter = 4
                    action_cooldown = 0
                    
        elif mage.rect.collidepoint(posx, posy):
            pygame.mouse.set_visible(False)
            screen.blit(shield_red, (posx - 50, posy - 50))
            if clicked == True:
                enemy.defend = 3
                if archer.hp > 0:
                    current_fighter = 2
                    action_cooldown = 0
                elif mage.hp > 0:
                    current_fighter = 3
                    action_cooldown = 0
                else:
                    current_fighter = 4
                    action_cooldown = 0
                
            else:
                pass

        elif archer.rect.collidepoint(posx, posy):
            pygame.mouse.set_visible(False)
            screen.blit(shield_green, (posx - 50, posy - 50))
            if clicked == True:
                enemy.defend = 2
                if archer.hp > 0:
                    current_fighter = 2
                    action_cooldown = 0
                elif mage.hp > 0:
                    current_fighter = 3
                    action_cooldown = 0
                else:
                    current_fighter = 4
                    action_cooldown = 0
            else:
                pass    
                
    elif current_fighter == 2:
        if enemy.rect.collidepoint(posx, posy):
            pygame.mouse.set_visible(False)
            screen.blit(sword_img, (posx - 50, posy - 50))
            if clicked == True:
                attack = True
                target = enemy
        else:
            pygame.mouse.set_visible(True)

    elif current_fighter == 3:
        if action_cooldown >= action_wait_time:
            pygame.mouse.set_visible(False)
            if knight.rect.collidepoint(posx, posy):
                screen.blit(heart_red_img, (posx - 50, posy - 50))
                if knight.hp < 1:
                    pass
                else:    
                    if clicked == True:
                        healing = 1
                        mage.heal()
                        current_fighter = 4
                        action_cooldown = 0
                    
            elif archer.rect.collidepoint(posx, posy):
                screen.blit(heart_blue_img, (posx - 50, posy - 50))
                if archer.hp < 1:
                    pass
                else:
                    if clicked == True:
                        healing = 2
                        mage.heal()
                        current_fighter = 4
                        action_cooldown = 0

            elif mage.rect.collidepoint(posx, posy):
                screen.blit(heart_green_img, (posx - 50, posy - 50))
                if mage.hp < 1:
                    pass
                else:
                    if clicked == True:
                        healing = 3
                        mage.heal()
                        current_fighter = 4
                        action_cooldown = 0

            elif enemy.rect.collidepoint(posx-50, posy-50):
                screen.blit(fire_img, (posx - 50, posy - 50))
                if clicked == True:
                    attack = True
                    target = enemy
            else:
                pygame.mouse.set_visible(True)

    
    else:
        pygame.mouse.set_visible(True)


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

    if game_over ==  0 or game_over == -1:
        if mage.alive == True:
            if current_fighter == 3:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    if attack == True and enemy != None:
                        mage.attack()
                        current_fighter = 4
                        action_cooldown = 0                    

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

#ideas:
#special for the knight: if he is attacked, he has a chance of an counterattack
#                        he can take the damage for an ally (symbol = shield)
#
#special for the archer: if he attacks, he has a chance of another attack
#                        he can increase the damage of an ally (symbol = fist)
#
#special for the mage:  chance of getting a heal when attacked
#                       increasing max hp of an ally
#                       chance of avoiding an attack