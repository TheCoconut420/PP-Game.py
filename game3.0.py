import random
from colorama import init, Fore, Back, Style    #pip install colorama
import PySimpleGUI as gui                       #pip install PySimpleGUI
gui.theme("Black")
init(autoreset=True)


class Hero:
    def __init__(self):
        self._name = "name"
        self._health = "health"
        self._magic_power = "magic_power"
        self._defense = "defense"
        self._weapon = "weapon"
        self._weapon_damage = "weapon_damage"
        self._speed = "speed"
        self._luck = "luck"
        self._exp = "exp"
        self._level = "level"

    def attack(self):
        if self._speed > enemy._speed:
            damage = (self._weapon_damage - enemy._defense)
            if damage <= 0:
                layout = [
                [gui.Text('The Attack did no damage!')],
                [gui.Button("Ok")]
                ]

                window = gui.Window('Results', layout)

                while True:
                    event, values = window.read()
                    if event == "Ok" or  event == gui.WIN_CLOSED:
                        break
                window.close()
                return
            else:
                if random.randint(1, 100) <= self._luck:
                    damage *= 2
                    enemy._health -= damage
                    self._exp += damage
                    layout = [
                    [gui.Text('The Attack was a critical hit!')],
                    [gui.Text('The Attack did ' + str(damage) + ' damage!')],
                    [gui.Text(self._name + ' gained ' + str(damage) + ' experience!')],
                    [gui.Text(self._name + ' has ' + str(self._exp) + ' experience!')],
                    [gui.Button("Ok")]
                    ]

                    window = gui.Window('Results', layout)

                    while True:
                        event, values = window.read()
                        if event == "Ok" or  event == gui.WIN_CLOSED:
                            break
                    window.close()
                else:
                    damage *= 1
                    enemy._health -= damage
                    self._exp += damage
                    layout = [
                    [gui.Text('The Attack did ' + str(damage) + ' damage!')],
                    [gui.Text(self._name + ' gained ' + str(damage) + ' experience!')],
                    [gui.Text(self._name + ' has ' + str(self._exp) + ' experience!')],
                    [gui.Button("Ok")]
                    ]

                    window = gui.Window('Results', layout)

                    while True:
                        event, values = window.read()
                        if event == "Ok" or  event == gui.WIN_CLOSED:
                            break
                    window.close()
        else:
            if random.randint(1, 20) <= self._speed:
                damage = (self._weapon_damage - enemy._defense)
                if damage <= 0:
                    layout = [
                    [gui.Text('The Attack did no damage!')],
                    [gui.Button("Ok")]
                    ]

                    window = gui.Window('Results', layout)

                    while True:
                        event, values = window.read()
                        if event == "Ok" or  event == gui.WIN_CLOSED:
                            break
                    window.close()
                    return
                else:
                    if random.randint(1, 100) <= self._luck:
                        damage *= 2
                        enemy._health -= damage
                        self._exp += damage
                        layout = [
                        [gui.Text('The Attack was a critical hit!')],
                        [gui.Text('The Attack did ' + str(damage) + ' damage!')],
                        [gui.Text(self._name + ' gained ' + str(damage) + ' experience!')],
                        [gui.Text(self._name + ' has ' + str(self._exp) + ' experience!')],
                        [gui.Button("Ok")]
                        ]

                        window = gui.Window('Results', layout)

                        while True:
                            event, values = window.read()
                            if event == "Ok" or  event == gui.WIN_CLOSED:
                                break
                        window.close()
                    else:
                        damage *= 1
                        enemy._health -= damage
                        self._exp += damage
                        layout = [
                        [gui.Text('The Attack did ' + str(damage) + ' damage!')],
                        [gui.Text(self._name + ' gained ' + str(damage) + ' experience!')],
                        [gui.Text(self._name + ' has ' + str(self._exp) + ' experience!')],
                        [gui.Button("Ok")]
                        ]

                        window = gui.Window('Results', layout)

                        while True:
                            event, values = window.read()
                            if event == "Ok" or  event == gui.WIN_CLOSED:
                                break
                        window.close()
            else:
                layout = [
                [gui.Text('The Attack missed!')],
                [gui.Button("Ok")]
                ]

                window = gui.Window('Results', layout)

                while True:
                    event, values = window.read()
                    if event == "Ok" or  event == gui.WIN_CLOSED:
                        break
                window.close()

    def defend(self): # not used
        if random.randint(1, 10) <= 5:
            print(Fore.LIGHTBLUE_EX + self._name + " defends!")
            self._defense += self._defense * 0.2
            print(Fore.LIGHTBLUE_EX + self._name + " has " + self._defense + " defense!")
        else:
            print(Fore.LIGHTBLUE_EX + self._name + " failed to defend!")

    def level_up(self):
        if self._exp >= 100:
            self._exp -= 100
            self._level += 1
            self._health += 5
            if self._magic_power == 0:
                self._magic_power += 0
            else:
                self._magic_power += 1
            self._defense += 1
            self._weapon_damage += 1
            self._speed += 1
            self._luck += 1
            layout = [
            [gui.Text(str(self._name) + ' now has:')],
            [gui.Text('Health: ' + str(self._health))],
            [gui.Text('Magic Power: ' + str(self._magic_power))],
            [gui.Text('Defense: ' + str(self._defense))],
            [gui.Text('Weapon: ' + self._weapon)],
            [gui.Text('Weapon Damage: ' + str(self._weapon_damage))],
            [gui.Text('Speed: ' + str(self._speed))],
            [gui.Text('Luck: ' + str(self._luck))],
            [gui.Text('Experience: ' + str(self._exp))],
            [gui.Text('Level: ' + str(self._level))],
            [gui.Button("Ok")]
            ]

            window = gui.Window('Results', layout)

            while True:
                event, values = window.read()
                if event == "Ok" or  event == gui.WIN_CLOSED:
                    break
            window.close()


class Warrior(Hero):
    def __init__(self, name):
        self._name = name
        self._health = random.randint(70, 100)
        self._magic_power = 0
        self._defense = random.randint(5, 7)
        self._weapon = "Sword"
        self._weapon_damage = random.randint(10, 12)
        self._speed = random.randint(15, 20)
        self._luck = random.randint(5, 10)
        self._exp = 0
        self._level = 1

    def get_stats(self):
        layout = [
        [gui.Text('The Warrior has:')],
        [gui.Text('Health: ' + str(self._health))],
        [gui.Text('Magic Power: ' + str(self._magic_power))],
        [gui.Text('Defense: ' + str(self._defense))],
        [gui.Text('Weapon: ' + self._weapon)],
        [gui.Text('Weapon Damage: ' + str(self._weapon_damage))],
        [gui.Text('Speed: ' + str(self._speed))],
        [gui.Text('Luck: ' + str(self._luck))],
        [gui.Text('Experience: ' + str(self._exp))],
        [gui.Text('Level: ' + str(self._level))],
        [gui.Button("Ok")]
        ]

        window = gui.Window('Results', layout)

        while True:
            event, values = window.read()
            if event == "Ok" or  event == gui.WIN_CLOSED:
                break
        window.close()

    def attack(self):
        if self._speed > enemy._speed:
            damage = (self._weapon_damage - enemy._defense)
            if damage <= 0:
                layout = [
                [gui.Text('The Attack did no damage!')],
                [gui.Button("Ok")]
                ]

                window = gui.Window('Results', layout)

                while True:
                    event, values = window.read()
                    if event == "Ok" or  event == gui.WIN_CLOSED:
                        break
                window.close()
                return
            else:
                if random.randint(1, 100) <= self._luck:
                    damage *= 2
                    enemy._health -= damage
                    self._exp += damage
                    if random.randint(0, 100) <= 20:
                            self._weapon_damage = 1
                            self._weapon = "Empty Hand"
                            layout = [
                            [gui.Text('The Attack was a critical hit!')],
                            [gui.Text('The Attack did ' + str(damage) + ' damage!')],
                            [gui.Text(self._name + ' gained ' + str(damage) + ' experience!')],
                            [gui.Text(self._name + ' has ' + str(self._exp) + ' experience!')],
                            [gui.Text ('The ' + self._name + ' The Weapon broke!')],
                            [gui.Button("Ok")]
                            ]

                            window = gui.Window('Results', layout)

                            while True:
                                event, values = window.read()
                                if event == "Ok" or  event == gui.WIN_CLOSED:
                                    break
                            window.close()
                    else:
                        layout = [
                        [gui.Text('The Attack was a critical hit!')],
                        [gui.Text('The Attack did ' + str(damage) + ' damage!')],
                        [gui.Text(self._name + ' gained ' + str(damage) + ' experience!')],
                        [gui.Text(self._name + ' has ' + str(self._exp) + ' experience!')],
                        [gui.Button("Ok")]
                        ]

                        window = gui.Window('Results', layout)

                        while True:
                            event, values = window.read()
                            if event == "Ok" or  event == gui.WIN_CLOSED:
                                break
                        window.close()
                else:
                    damage *= 1
                    enemy._health -= damage
                    self._exp += damage
                    layout = [
                    [gui.Text('The Attack did ' + str(damage) + ' damage!')],
                    [gui.Text(self._name + ' gained ' + str(damage) + ' experience!')],
                    [gui.Text(self._name + ' has ' + str(self._exp) + ' experience!')],
                    [gui.Button("Ok")]
                    ]

                    window = gui.Window('Results', layout)

                    while True:
                        event, values = window.read()
                        if event == "Ok" or  event == gui.WIN_CLOSED:
                            break
                    window.close()

        else:
            if random.randint(1, 20) <= self._speed:
                damage = (self._weapon_damage - enemy._defense)
                if damage <= 0:
                    layout = [
                    [gui.Text('The Attack did no damage!')],
                    [gui.Button("Ok")]
                    ]

                    window = gui.Window('Results', layout)

                    while True:
                        event, values = window.read()
                        if event == "Ok" or  event == gui.WIN_CLOSED:
                            break
                    window.close()
                    return
                else:
                    if random.randint(1, 100) <= self._luck:
                        damage *= 2
                        enemy._health -= damage
                        self._exp += damage
                        if random.randint(0, 100) <= 20:
                                self._weapon_damage = 1
                                self._weapon = "Empty Hand"
                                layout = [
                                [gui.Text('The Attack was a critical hit!')],
                                [gui.Text('The Attack did ' + str(damage) + ' damage!')],
                                [gui.Text(self._name + ' gained ' + str(damage) + ' experience!')],
                                [gui.Text(self._name + ' has ' + str(self._exp) + ' experience!')],
                                [gui.Text ('The ' + self._name + ' The Weapon broke!')],
                                [gui.Button("Ok")]
                                ]

                                window = gui.Window('Results', layout)

                                while True:
                                    event, values = window.read()
                                    if event == "Ok" or  event == gui.WIN_CLOSED:
                                        break
                                window.close()
                        else:
                            layout = [
                            [gui.Text('The Attack was a critical hit!')],
                            [gui.Text('The Attack did ' + str(damage) + ' damage!')],
                            [gui.Text(self._name + ' gained ' + str(damage) + ' experience!')],
                            [gui.Text(self._name + ' has ' + str(self._exp) + ' experience!')],
                            [gui.Button("Ok")]
                            ]

                            window = gui.Window('Results', layout)

                            while True:
                                event, values = window.read()
                                if event == "Ok" or  event == gui.WIN_CLOSED:
                                    break
                            window.close()
                    else:
                        damage *= 1
                        enemy._health -= damage
                        self._exp += damage
                        layout = [
                        [gui.Text('The Attack did ' + str(damage) + ' damage!')],
                        [gui.Text(self._name + ' gained ' + str(damage) + ' experience!')],
                        [gui.Text(self._name + ' has ' + str(self._exp) + ' experience!')],
                        [gui.Button("Ok")]
                        ]

                        window = gui.Window('Results', layout)

                        while True:
                            event, values = window.read()
                            if event == "Ok" or  event == gui.WIN_CLOSED:
                                break
                        window.close()
            else:
                layout = [
                [gui.Text('The Attack missed!')],
                [gui.Button("Ok")]
                ]

                window = gui.Window('Results', layout)

                while True:
                    event, values = window.read()
                    if event == "Ok" or  event == gui.WIN_CLOSED:
                        break
                window.close()
        
    def new_weapon(self):
        if self._weapon == "Empty Hand":
            self._weapon = "Sword"
            self._weapon_damage = random.randint(7, 10)
            layout = [
            [gui.Text(str(self._name) + ' found a new Weapon!')],
            [gui.Text('The Weapon is a ' + self._weapon + '!')],
            [gui.Text('The Weapon does ' + str(self._weapon_damage) + ' damage!')],
            [gui.Button("Ok")]
            ]

            window = gui.Window('Results', layout)

            while True:
                event, values = window.read()
                if event == "Ok" or  event == gui.WIN_CLOSED:
                    break
            window.close()
        else:
            layout = [
            [gui.Text(str(self._name) + ' already has a Weapon!')],
            [gui.Button("Ok")]
            ]

            window = gui.Window('Results', layout)

            while True:
                event, values = window.read()
                if event == "Ok" or  event == gui.WIN_CLOSED:
                    break
            window.close()

    def get_enemy_stats(self):
        enemy.get_stats()

    def choose(self):
        if self._health <= 0:
            layout = [
            [gui.Text('The Warrior is dead!')],
            [gui.Button("Ok")]
            ]

            window = gui.Window('Hero Died', layout)

            while True:
                event, values = window.read()
                if event == "Ok" or  event == gui.WIN_CLOSED:
                    break
            window.close()
            exit()
        else:
            layout = [
            [gui.Text('What should the Warrior do?')],
            [gui.Button("    Attack     ", size = (20, 1))],
            [gui.Button("  New Weapon   ", size = (20, 1))],
            [gui.Button("Get Enemy Stats", size = (20, 1))],
            [gui.Button(" Get my Stats  ", size = (20, 1))],           
            ]

            window = gui.Window('Decision.', layout, size = (200, 170))
            event, values = window.read()
            if event == "    Attack     " or event == "  New Weapon   " or event == "Get Enemy Stats" or event == " Get my Stats  " or event == gui.WIN_CLOSED:
                if event == "    Attack     ":
                    window.close()
                    self.attack()
                elif event == "  New Weapon   ":
                    window.close()
                    self.new_weapon()
                elif event == "Get Enemy Stats":
                    window.close()
                    self.get_enemy_stats()
                elif event == " Get my Stats  ":
                    window.close()
                    self.get_stats()
                elif event == gui.WIN_CLOSED:
                    self.choose()


class Mage(Hero):
    def __init__(self, name):
        self._name = name
        self._health = random.randint(40, 50)
        self._magic_power = random.randint(10, 15)
        self._defense = random.randint(1, 3)
        self._weapon = "Staff"
        self._weapon_damage = random.randint(5, 10)
        self._speed = random.randint(9, 20)
        self._luck = random.randint(8, 10)
        self._exp = 0
        self._level = 1

    def get_stats(self):
        layout = [
        [gui.Text('The Mage has:')],
        [gui.Text('Health: ' + str(self._health))],
        [gui.Text('Magic Power: ' + str(self._magic_power))],
        [gui.Text('Defense: ' + str(self._defense))],
        [gui.Text('Weapon: ' + self._weapon)],
        [gui.Text('Weapon Damage: ' + str(self._weapon_damage))],
        [gui.Text('Speed: ' + str(self._speed))],
        [gui.Text('Luck: ' + str(self._luck))],
        [gui.Text('Experience: ' + str(self._exp))],
        [gui.Text('Level: ' + str(self._level))],
        [gui.Button("Ok")]
        ]

        window = gui.Window('Results', layout)

        while True:
            event, values = window.read()
            if event == "Ok" or  event == gui.WIN_CLOSED:
                break
        window.close()

    def magic_attack(self):
        if self._magic_power < 1:
            layout = [
            [gui.Text('The Mage has no Magic Power!')],
            [gui.Button("Ok")]
            ]

            window = gui.Window('Results', layout)

            while True:
                event, values = window.read()
                if event == "Ok" or  event == gui.WIN_CLOSED:
                    break
            window.close()
        else:
            layout = [
                [gui.Text("What magic should")],
                [gui.Text("the Mage use?")],
                [gui.Button("  Frost  ")],
                [gui.Button(" Weakness")],
                [gui.Button("   Heal  ")],
                [gui.Button("   Fire  ")],
                [gui.Button("Lightning")]
            ]

            window = gui.Window('Decision.', layout)
                
            while True:
                event, values = window.read()
                if event == "  Frost  " or event == " Weakness" or event == "   Heal  " or event == "   Fire  " or event == "Lightning" or event == "Ok" or event == gui.WIN_CLOSED:
                    if event == "  Frost  ":
                        window.close()
                        self.frost()
                        break
                    elif event == " Weakness":
                        window.close()
                        self.weakness()
                        break
                    elif event == "   Heal  ":
                        window.close()
                        self.heal
                        break
                    elif event == "   Fire  ":
                        window.close()
                        self.fire()
                        break
                    elif event == "Lightning":
                        window.close()
                        self.lightning()
                        break
                    elif event == gui.WIN_CLOSED:
                        window.close()
                        self.magic_attack()        
                        break

    def frost(self):
        if enemy._speed <= 0:
            self._magic_power -= 1
            layout = [
            [gui.Text('The enemys speed is already 0!')],
            [gui.Button("Ok")]
            ]

            window = gui.Window('Frost', layout)

            while True:
                event, values = window.read()
                if event == "Ok" or  event == gui.WIN_CLOSED:
                    break
            window.close()
            self._magic_power -=1

        else:
            enemy._speed -= 1
            self._magic_power -= 1
            layout = [
            [gui.Text('The enemys speed has been lowered by one!')],
            [gui.Button("Ok")]
            ]

            window = gui.Window('Frost', layout)

            while True:
                event, values = window.read()
                if event == "Ok" or  event == gui.WIN_CLOSED:
                    break
            window.close()

    def weakness(self):
        if enemy._weapon_damage <= 0:
            layout = [
            [gui.Text('The enemy already has 0 weapon damage!')],
            [gui.Button("Ok")]
            ]

            window = gui.Window('Weakness', layout)

            while True:
                event, values = window.read()
                if event == "Ok" or  event == gui.WIN_CLOSED:
                    break
            window.close()
            self._magic_power -= 1
        else:  
            enemy._weapon_damage -= 1
            self._magic_power -= 1
            layout = [
            [gui.Text('The enemys weapon damage is reduced by 1!')],
            [gui.Text('The enemy has ' + str(enemy._weapon_damage) + ' weapon damage!')],
            [gui.Button("Ok")]
            ]

            window = gui.Window('Weakness', layout)

            while True:
                event, values = window.read()
                if event == "Ok" or  event == gui.WIN_CLOSED:
                    break
            window.close()

    def heal(self):
        heal = random.randint(10, 20)
        layout = [
        [gui.Text('Who should get the Heal?')],
        [gui.Button("Warrior")], 
        [gui.Button("Mage")],
        [gui.Button("Archer")],
        [gui.Button("Back")] 
        ]

        window = gui.Window("Heal", layout)
        
        while True:
            if event == gui.WIN_CLOSED or event == 'Back' or event == "Warrior" or event == "Mage" or event == "Archer":
                if event == "Warrior":
                    warrior._health += heal
                    layout = [
                    [gui.Text('The Warrior now has:')],
                    [gui.Text(str(warrior._health))]
                    [gui.Button("Ok")]
                    ]

                    window = gui.Window('Results', layout)

                    while True:
                        event, values = window.read()
                        if event == "Ok" or  event == gui.WIN_CLOSED:
                            break
                    window.close()
                    break
                elif event == "Mage":
                    mage._health += heal
                    layout = [
                    [gui.Text('The Mage now has:')],
                    [gui.Text(str(mage._health))]
                    [gui.Button("Ok")]
                    ]

                    window = gui.Window('Results', layout)

                    while True:
                        event, values = window.read()
                        if event == "Ok" or  event == gui.WIN_CLOSED:
                            break
                    window.close()
                    break
                elif event == "Archer":
                    archer._health += heal
                    layout = [
                    [gui.Text('The Archer now has:')],
                    [gui.Text(str(archer._health))]
                    [gui.Button("Ok")]
                    ]

                    window = gui.Window('Results', layout)

                    while True:
                        event, values = window.read()
                        if event == "Ok" or  event == gui.WIN_CLOSED:
                            break
                    window.close()
                    break
                elif event == "Back":
                    self.magic_attack()
                    break
                elif event == gui.WIN_CLOSED:
                    self.heal

    def fire(self):
        if self._magic_power < 2:
            layout = [
            [gui.Text('You dont have enough Magic Power left!')],
            [gui.Button("Ok")]
            ]

            window = gui.Window('Illigal Input', layout)

            while True:
                event, values = window.read()
                if event == "Ok" or  event == gui.WIN_CLOSED:
                    break
            window.close()
            self.magic_attack()
        else:
            damage = random.randint(5, 20)
            enemy._health -= damage
            self._magic_power -= 2
            self._exp += damage
            damage = self._weapon_damage * 2
            enemy._health -= damage
            self._magic_power -= 1
            self._exp += damage
            layout = [
            [gui.Text('The fire did ' + str(damage) + ' damage!')],
            [gui.Text(self._name + ' gained ' + str(damage) + ' experience!')],
            [gui.Text(self._name + ' has ' + str(self._exp) + ' experience!')],
            [gui.Button("Ok")]
            ]

            window = gui.Window('Results', layout)

            while True:
                event, values = window.read()
                if event == "Ok" or  event == gui.WIN_CLOSED:
                    break
            window.close()

    def lightning(self):
        if self._magic_power < 3:
            layout = [
            [gui.Text('You dont have enough Magic Power left!')],
            [gui.Button("Ok")]
            ]

            window = gui.Window('Illigal Input', layout)

            while True:
                event, values = window.read()
                if event == "Ok" or  event == gui.WIN_CLOSED:
                    break
            window.close()
            self.magic_attack()
        else:
            damage = random.randint(15, 40)
            enemy._health -= damage
            self._magic_power -= 3
            self._exp += damage
            layout = [
            [gui.Text('The lightning did ' + str(damage) + ' damage!')],
            [gui.Text(self._name + ' gained ' + str(damage) + ' experience!')],
            [gui.Text(self._name + ' has ' + str(self._exp) + ' experience!')],
            [gui.Button("Ok")]
            ]

            window = gui.Window('Results', layout)

            while True:
                event, values = window.read()
                if event == "Ok" or  event == gui.WIN_CLOSED:
                    break
            window.close()

    def rest(self):
        layout = [
        [gui.Text('The Mage Recovered two points of Magic Power!')],
        [gui.Button("Ok")]
        ]

        window = gui.Window('Archer Rests', layout)

        while True:
            event, values = window.read()
            if event == "Ok" or  event == gui.WIN_CLOSED:
                break
        window.close()
        self._magic_power += 2

    def choose(self):
        if self._health <= 0:
            layout = [
            [gui.Text('The Mage is dead!')],
            [gui.Button("Ok")]
            ]

            window = gui.Window('Hero Died', layout)

            while True:
                event, values = window.read()
                if event == "Ok" or  event == gui.WIN_CLOSED:
                    break
            window.close()
            exit()
        else:
            layout = [
            [gui.Text('What should the Mage do?')],
            [gui.Button("   Attack   ", size = (20, 1))],
            [gui.Button("    Magic   ", size = (20, 1))],
            [gui.Button("    Rest    ", size = (20, 1))],
            [gui.Button("Get my Stats", size = (20, 1))],           
            ]

            window = gui.Window('Decision.', layout, size = (200, 170))
            event, values = window.read()
            if event == "   Attack   " or event == "    Magic   " or event == "    Rest    " or event == "Get my Stats" or event == gui.WIN_CLOSED:
                if event == "   Attack   ":
                    window.close()
                    self.attack()
                elif event == "    Magic   ":
                    window.close()
                    self.magic_attack()
                elif event == "    Rest    ":
                    window.close()
                    self.rest()
                elif event == "Get my Stats":
                    window.close()
                    self.get_stats()
                elif event == gui.WIN_CLOSED:
                    self.choose()


class Archer(Hero):
    def __init__(self, name):
        self._name = name
        self._health = random.randint(60, 80)
        self._magic_power = random.randint(2, 5)
        self._defense = random.randint(2, 4)
        self._weapon = "Bow"
        self._weapon_damage = random.randint(8, 12)
        self._speed = random.randint(10, 15)
        self._luck = random.randint(4, 10)
        self._exp = 0
        self._level = 1

    def get_stats(self):
        layout = [
        [gui.Text('The Archer has:')],
        [gui.Text('Health: ' + str(self._health))],
        [gui.Text('Magic Power: ' + str(self._magic_power))],
        [gui.Text('Defense: ' + str(self._defense))],
        [gui.Text('Weapon: ' + self._weapon)],
        [gui.Text('Weapon Damage: ' + str(self._weapon_damage))],
        [gui.Text('Speed: ' + str(self._speed))],
        [gui.Text('Luck: ' + str(self._luck))],
        [gui.Text('Experience: ' + str(self._exp))],
        [gui.Text('Level: ' + str(self._level))],
        [gui.Button("Ok")]
        ]

        window = gui.Window('Results', layout)

        while True:
            event, values = window.read()
            if event == "Ok" or  event == gui.WIN_CLOSED:
                break
        window.close()

    def magic_arrow(self):
        layout = [
        [gui.Text("What Magic Arrow should")],
        [gui.Text("the Archer use?")],
        [gui.Button("Roulette Arrow", size = (20, 1))],
        [gui.Button("Spectral Arrow", size = (20, 1))],
        ]

        window = gui.Window('Decision.', layout, size = (200, 130))
        event, values = window.read()
        if event == "Roulette Arrow" or event == "Spectral Arrow " or event == gui.WIN_CLOSED:
            if event == "Roulette Arrow":
                window.close()
                self.roulette_arrow()
            elif event == "Spectral Arrow":
                window.close()
                self.spectral_arrow()
            elif event == gui.WIN_CLOSED:
                self.magic_arrow()

    def roulette_arrow(self):
        if self._magic_power < 2:
            layout = [
            [gui.Text('You dont have enough Magic Power left!')],
            [gui.Button("Ok")]
            ]

            window = gui.Window('Illigal Input', layout)

            while True:
                event, values = window.read()
                if event == "Ok" or  event == gui.WIN_CLOSED:
                    break
            window.close()
            self.magic_arrow()
        else:
            if random.randint(1, 10) == 1:
                damage = self._weapon_damage * 10
                enemy._health -= damage
                self._magic_power -= 2
                self._exp += damage
                  
            else:
                layout = [
                [gui.Text('The roulette arrow missed!')],
                [gui.Button("Ok")]
                ]

                window = gui.Window('Missed Attack', layout)

                while True:
                    event, values = window.read()
                    if event == "Ok" or  event == gui.WIN_CLOSED:
                        break
                window.close()
                self._magic_power -= 2
            
    def spectral_arrow(self):
        if self._magic_power < 1:
            layout = [
            [gui.Text('You dont have enough Magic Power left!')],
            [gui.Button("Ok")]
            ]

            window = gui.Window('Illigal Input', layout)

            while True:
                event, values = window.read()
                if event == "Ok" or  event == gui.WIN_CLOSED:
                    break
            window.close()
            self.magic_arrow()
        else:
            damage = self._weapon_damage * 2
            enemy._health -= damage
            self._magic_power -= 1
            self._exp += damage
            layout = [
            [gui.Text('The spectral arrow did ' + str(damage) + ' damage!')],
            [gui.Text(self._name + ' gained ' + str(damage) + ' experience!')],
            [gui.Text(self._name + ' has ' + str(self._exp) + ' experience!')],
            [gui.Button("Ok")]
            ]

            window = gui.Window('Results', layout)

            while True:
                event, values = window.read()
                if event == "Ok" or  event == gui.WIN_CLOSED:
                    break
            window.close()

    def rest(self):
        layout = [
            [gui.Text('The Archer Recovered one point of Magic Power!')],
            [gui.Button("Ok")]
        ]

        window = gui.Window('Archer Rests', layout)

        while True:
            event, values = window.read()
            if event == "Ok" or  event == gui.WIN_CLOSED:
                break
        window.close()
        self._magic_power += 1

    def choose(self):
        if self._health <= 0:
            layout = [
            [gui.Text('The Archer is dead!')],
            [gui.Button("Ok")]
            ]

            window = gui.Window('Hero Died', layout)

            while True:
                event, values = window.read()
                if event == "Ok" or  event == gui.WIN_CLOSED:
                    break
            window.close()
            exit()
        else:
            layout = [
            [gui.Text('What should the Archer do?')],
            [gui.Button("   Attack   ", size = (20, 1))],
            [gui.Button("Magic Arrow ", size = (20, 1))],
            [gui.Button("    Rest    ", size = (20, 1))],
            [gui.Button("Get my Stats", size = (20, 1))],           
            ]

            window = gui.Window('Decision.', layout, size = (200, 170))
            event, values = window.read()
            if event == "   Attack   " or event == "Magic Arrow " or event == "    Rest    " or event == "Get my Stats" or event == gui.WIN_CLOSED:
                if event == "   Attack   ":
                    window.close()
                    self.attack()
                elif event == "Magic Arrow ":
                    window.close()
                    self.magic_arrow()
                elif event == "    Rest    ":
                    window.close()
                    self.rest()
                elif event == "Get my Stats":
                    window.close()
                    self.get_stats()
                elif event == gui.WIN_CLOSED:
                    self.choose()


class Enemy():
    def __init__(self, mate) -> None:
        self._name = "Enemy"
        self._health = random.randint(270, 400)
        self._magic_power = 0
        self._defense = random.randint(5, 8)
        self._weapon = "Ancient Sword"
        self._weapon_damage = random.randint(13, 15)
        self._speed = random.randint(15, 20)
        self._luck = random.randint(5, 10)
        self._exp = 0
        self._level = 10
        self._mate = mate

    def get_stats(self):
        layout = [
        [gui.Text('The Enemy has:')],
        [gui.Text('Health: ' + str(self._health))],
        [gui.Text('Magic Power: ' + str(self._magic_power))],
        [gui.Text('Defense: ' + str(self._defense))],
        [gui.Text('Weapon: ' + self._weapon)],
        [gui.Text('Weapon Damage: ' + str(self._weapon_damage))],
        [gui.Text('Speed: ' + str(self._speed))],
        [gui.Text('Luck: ' + str(self._luck))],
        [gui.Text('Experience: ' + str(self._exp))],
        [gui.Text('Level: ' + str(self._level))],
        [gui.Button("Ok")]
        ]

        window = gui.Window('Results', layout)

        while True:
            event, values = window.read()
            if event == "Ok" or  event == gui.WIN_CLOSED:
                break
        window.close()

    def attack(self):
        if self._health < 200:
            if random.randint(1, 3) == 1:
                self.aoe_attack
            else:
                self.single_attack
        else:
            self.single_attack()

    def aoe_attack(self):
        damage = self._weapon_damage * 2
        archer._health -= damage
        warrior._health -= damage
        mage._health -= damage
        layout = [
        [gui.Text('The Enemy has attacked all Heros!')],
        [gui.Text('The Enemy did ' + str(damage) + ' damage!')],
        ]

        window = gui.Window('Results', layout)

        while True:
            event, values = window.read()
            if event == "Ok" or  event == gui.WIN_CLOSED:
                window.close()
                break

    def single_attack(self):
        mate = random.randint(1, 3)
        damage = self._weapon_damage + random.randint(1, 3)
        if mate == 1:
            if warrior._health < 1:
                self.single_attack()
            else:
                damage -= warrior._defense
                warrior._health -= damage
                layout = [
                [gui.Text('The Enemy attacked the Warrior!')],
                [gui.Text('The Enemy did ' + str(damage) + ' damage!')],
                [gui.Button("Ok")]
                ]

                window = gui.Window('Results', layout)

                while True:
                    event, values = window.read()
                    if event == "Ok" or  event == gui.WIN_CLOSED:
                        window.close()
                        break
        elif mate == 2:
            if archer._health < 1:
                self.single_attack()
            else:
                damage -= archer._defense
                archer._health -= damage
                layout = [
                [gui.Text('The Enemy attacked the Archer!')],
                [gui.Text('The Enemy did ' + str(damage) + ' damage!')],
                [gui.Button("Ok")]
                ]

                window = gui.Window('Results', layout)

                while True:
                    event, values = window.read()
                    if event == "Ok" or  event == gui.WIN_CLOSED:
                        window.close()
                        break
        elif mate == 3:
            if mage._health < 1:
                self.single_attack()
            else:
                damage -= mage._defense
                mage._health -= damage
                layout = [
                [gui.Text('The Enemy attacked the Mage!')],
                [gui.Text('The Enemy did ' + str(damage) + ' damage!')],
                [gui.Button("Ok")]
                ]

                window = gui.Window('Results', layout)

                while True:
                    event, values = window.read()
                    if event == "Ok" or  event == gui.WIN_CLOSED:
                        window.close()
                        break
                    

if __name__ == "__main__":

    layout = [
    [gui.Text('Enter the Name of the Warrior.')],
    [gui.Text("Name:", size=(10, 1), justification='right'),gui.Input(key="-Warrior_Name-")],
    [gui.Button("Ok")]
    ]

    window = gui.Window("Name of Warrior", layout, size = (300, 100))

    while True:
        event, values = window.read()
        if event == "Ok" or  event == gui.WIN_CLOSED:
            warrior_name = values["-Warrior_Name-"]
            break
    window.close()
    layout = [
    [gui.Text('Enter the Name of the Mage.')],
    [gui.Text("Name:", size=(10, 1), justification='right'),gui.Input(key="-Mage_Name-")],
    [gui.Button("Ok")]
    ]

    window = gui.Window('Name of Mage', layout, size = (300, 100))

    while True:
        event, values = window.read()
        if event == "Ok" or  event == gui.WIN_CLOSED:
            mage_name = values["-Mage_Name-"]
            break
    window.close()

    layout = [
    [gui.Text('Enter the Name of the Archer.')],
    [gui.Text("Name:", size=(10, 1), justification='right'),gui.Input(key="-Archer_Name-")],
    [gui.Button("Ok")]
    ]

    window = gui.Window('Name of Archer', layout, size = (300, 100))

    while True:
        event, values = window.read()
        if event == "Ok" or  event == gui.WIN_CLOSED:
            archer_name = values["-Archer_Name-"]
            break
    window.close()

    mage = Mage(mage_name)
    archer = Archer(archer_name)
    warrior = Warrior(warrior_name)
    enemy = Enemy(0) 

    while True:
        warrior.choose()
        warrior.level_up()
        if enemy._health <= 0:
            layout = [
            [gui.Text('The Enemy has been defeated!')],
            [gui.Button("Ok")]
            ]

            window = gui.Window('Results', layout)

            while True:
                event, values = window.read()
                if event == "Ok" or  event == gui.WIN_CLOSED:
                    window.close()
                    break
        mage.choose()
        mage.level_up()
        if enemy._health <= 0:
            layout = [
            [gui.Text('The Enemy has been defeated!')],
            [gui.Button("Ok")]
            ]

            window = gui.Window('Results', layout)

            while True:
                event, values = window.read()
                if event == "Ok" or  event == gui.WIN_CLOSED:
                    window.close()
                    break
        archer.choose()
        archer.level_up()
        if enemy._health <= 0:
            layout = [
            [gui.Text('The Enemy has been defeated!')],
            [gui.Button("Ok")]
            ]

            window = gui.Window('Results', layout)

            while True:
                event, values = window.read()
                if event == "Ok" or  event == gui.WIN_CLOSED:
                    window.close()
                    break
        enemy.attack()
        if warrior._health <= 0 and mage._health <= 0 and archer._health <= 0:
            layout = [
            [gui.Text('You have been defeated!')],
            [gui.Button("Ok")]
            ]
            
            window = gui.Window('Results', layout)

            while True:
                event, values = window.read()
                if event == "Ok" or  event == gui.WIN_CLOSED:
                    window.close()
                    break