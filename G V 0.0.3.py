import random
from G_V_character import Enemy, Hero, Ork, Elf, Ppl, Dwarf, Hobbit, Goblin

hero_global = Hero()
enemy_global = Enemy()

ork_global = Ork()
elf_global = Elf()
ppl_global = Ppl()
dwarf_global = Dwarf()
hobbit_global = Hobbit()
goblin_global = Goblin()


def attack_choice_hero():
    global hero_global
    global enemy_global
    while True:
        choice_enemy = random.randint(1, 3)
        if choice_enemy == 1:  # если атака/атака
            hero_global.damage = (enemy_global.power * 2 + enemy_global.luck * 2 + enemy_global.speed * 1.5) * 2
            enemy_global.damage = (hero_global.power * 2 + hero_global.luck * 2 + hero_global.speed * 1.5) * 2
            break
        elif choice_enemy == 2:
            hero_global.damage = (enemy_global.defense * 3 + enemy_global.power + enemy_global.power * 2) * 2
            enemy_global.damage = (hero_global.power * 2 + hero_global.luck * 2 + hero_global.speed * 1.5) / 2
            break
        elif choice_enemy == 3:
            hero_global.damage = (enemy_global.speed * 2 + enemy_global.power * 2 + enemy_global.luck) * 3
            enemy_global.damage = (hero_global.power * 2 + hero_global.luck * 2 + hero_global.speed * 1.5) * 1.5
            break
    return


def defence_choice_hero():
    global hero_global
    global enemy_global
    while True:
        choice_enemy = random.randint(1, 3)
        if choice_enemy == 1:  # если атака/атака
            hero_global.damage = (enemy_global.power * 2 + enemy_global.luck * 2 + enemy_global.speed * 1.5) / 2
            enemy_global.damage = (hero_global.defense * 3 + hero_global.luck * 2 + hero_global.power) * 2
            break
        elif choice_enemy == 2:
            hero_global.damage = 1
            enemy_global.damage = 1
            break
        elif choice_enemy == 3:
            hero_global.damage = enemy_global.speed * 2 + enemy_global.power * 2 + enemy_global.luck
            enemy_global.damage = hero_global.defense * 3 + hero_global.luck * 2 + hero_global.power
            break
    return


def ram_choice_hero():
    global hero_global
    global enemy_global
    while True:
        choice_enemy = random.randint(1, 3)
        if choice_enemy == 1:  # если атака/атака
            hero_global.damage = (enemy_global.power * 2 + enemy_global.luck * 2 + enemy_global.speed * 1.5) * 1.5
            enemy_global.damage = (hero_global.power * 2 + hero_global.luck + hero_global.speed * 2) * 3
            break
        elif choice_enemy == 2:
            hero_global.damage = enemy_global.defense * 3 + enemy_global.power + enemy_global.luck * 2
            enemy_global.damage = hero_global.power * 2 + hero_global.luck + hero_global.speed * 2
            break
        elif choice_enemy == 3:
            hero_global.damage = enemy_global.speed * 2 + enemy_global.power * 2 + enemy_global.luck
            enemy_global.damage = hero_global.power * 2 + hero_global.luck + hero_global.speed * 2
            break
    return


#

def hero_choice():
    global hero_global
    global enemy_global
    print('Выбери за кого ты будешь драться:')
    print('''
    1 - Орк
    2 - Эльф
    3 - Человек
    4 - Гном
    5 - Хоббит
    6 - Гоблин''')
    while True:
        choice = int(input('Сделай выбор ? :'))
        if choice == 1:
            hero_global = ork_global
            hero_global.MyName_name = MyName
            break
        elif choice == 2:
            hero_global = elf_global
            hero_global.MyName_name = MyName
            break
        elif choice == 3:
            hero_global = ppl_global
            hero_global.MyName_name = MyName
            break
        elif choice == 4:
            hero_global = dwarf_global
            hero_global.MyName_name = MyName
            break
        elif choice == 5:
            hero_global = hobbit_global
            hero_global.MyName_name = MyName
            break
        elif choice == 5:
            hero_global = goblin_global
            hero_global.MyName_name = MyName
            break
        else:
            print("Ошибка!")
    menu_choice()
    return


#

def enemy_choice():
    global hero_global
    global enemy_global
    choice = random.randint(1, 6)
    if choice == 1:
        enemy_global = ork_global
    elif choice == 2:
        enemy_global = elf_global
    elif choice == 3:
        enemy_global = ppl_global
    elif choice == 4:
        enemy_global = dwarf_global
    elif choice == 5:
        enemy_global = hobbit_global
    elif choice == 6:
        enemy_global = goblin_global
    return
    #


def menu_choice():
    global hero_global
    global enemy_global
    print('Приветствую тебя ' + hero_global.MyName_name + ' ' + hero_global.name_character)
    enemy_choice()
    hero_global.hp = 1000
    enemy_global.hp = 1000
    print('''
    Сделай выбор:
    1 - снаряжение
    2 - магазин
    3 - профиль
    4 - в бой
    ''')
    while True:
        choice = int(input('Сделай выбор ? :'))
        if choice == 1:
            #inventory_choice()
            break
        elif choice == 2:
            #shop_choice()
            break
        elif choice == 3:
            #profile_choice()
            break
        elif choice == 4:
            battle_choice()
            break
        else:
            print('Ошибка')
    return

    #


def battle_choice():
    global hero_global
    global enemy_global
    print('Привет!!--' + hero_global.MyName_name + hero_global.name_character)
    while hero_global.hp > 0 or enemy_global.hp > 0:
        print('Твой противник :' + enemy_global.name_character + '---' + str(enemy_global.hp))
        print('Твой герой :' + hero_global.name_character + '---' + str(hero_global.hp))
        print('Что ты будешь делать? ')
        print('1 - Атака')
        print('2 - Оборона')
        print('3 - Таран')
        while True:
            choice = int(input('Сделай выбор :'))
            if choice == 1:
                attack_choice_hero()
                hero_global.hp = hero_global.hp - hero_global.damage
                enemy_global.hp = enemy_global.hp - enemy_global.damage
                break
            elif choice == 2:
                defence_choice_hero()
                hero_global.hp = hero_global.hp - hero_global.damage
                enemy_global.hp = enemy_global.hp - enemy_global.damage
                break
            elif choice == 3:
                ram_choice_hero()
                hero_global.hp = hero_global.hp - hero_global.damage
                enemy_global.hp = enemy_global.hp - enemy_global.damage
                break
            else:
                print('Ошибка')
                break
    else:
        if enemy_global.hp <= 0:
            print('Поздравляю ты победил!!!')
            print('Твой герой :' + hero_global.MyName_name + '---' + str(hero_global.hp))
            menu_choice()
        elif hero_global.hp <= 0:
            print('Увы но ты проиграл(((')
            print('Твой противник :' + enemy_global.name_character + '---' + str(enemy_global.hp))
            menu_choice()
    return


print('Привет! Как тебя зовут?')
MyName = input()
hero_global.MyName_name = MyName
print('Рад познакомиться ' + MyName)
hero_choice()
