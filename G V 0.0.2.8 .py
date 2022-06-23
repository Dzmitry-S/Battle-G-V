import random
from G_V_character import ParentCharacter, Enemy, Hero, Ork, Elf, Ppl, Dwarf, Hobbit, Goblin


def attack_choice_hero(enemy, hero):
    while True:
        choice_enemy = random.randint(1, 3)
        if choice_enemy == 1:  # если атака/атака
            hero.damage = (enemy.power * 2 + enemy.luck * 2 + enemy.speed * 1.5) * 2
            enemy.damage = (hero.power * 2 + hero.luck * 2 + hero.speed * 1.5) * 2
            break
        elif choice_enemy == 2:
            hero.damage = (enemy.defence * 3 + enemy.power + enemy.power * 2) * 2
            enemy.damage = (hero.power * 2 + hero.luck * 2 + hero.speed * 1.5) / 2
            break
        elif choice_enemy == 3:
            hero.damage = (enemy.speed * 2 + enemy.power * 2 + enemy.luck) * 3
            enemy.damage = (hero.power * 2 + hero.luck * 2 + hero.speed * 1.5) * 1.5
            break
    return


def defence_choice_hero(hero, enemy):
    while True:
        choice_enemy = random.randint(1, 3)
        if choice_enemy == 1:  # если атака/атака
            hero.damage = (enemy.power * 2 + enemy.luck * 2 + enemy.speed * 1.5) / 2
            enemy.damage = (hero.defense * 3 + hero.luck * 2 + hero.power) * 2
            break
        elif choice_enemy == 2:
            hero.damage = 1
            enemy.damage = 1
            break
        elif choice_enemy == 3:
            hero.damage = enemy.speed * 2 + enemy.power * 2 + enemy.luck
            enemy.damage = hero.defense * 3 + hero.luck * 2 + hero.power
            break
    return


def ram_choice_hero(enemy, hero):
    while True:
        choice_enemy = random.randint(1, 3)
        if choice_enemy == 1:  # если атака/атака
            hero.damage = (enemy.power * 2 + enemy.luck * 2 + enemy.speed * 1.5) * 1.5
            enemy.damage = (hero.power * 2 + hero.luck + hero.speed * 2) * 3
            break
        elif choice_enemy == 2:
            hero.damage = enemy.defence * 3 + enemy.power + enemy.luck * 2
            enemy.damage = hero.power * 2 + hero.luck + hero.speed * 2
            break
        elif choice_enemy == 3:
            hero.damage = enemy.speed * 2 + enemy.power * 2 + enemy.luck
            enemy.damage = hero.power * 2 + hero.luck + hero.speed * 2
            break
    return


#

def hero_choice(ork, elf, ppl, dwarf, hobbit, goblin, enemy):
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
            hero = ork
            hero.MyName_name = MyName
            break
        elif choice == 2:
            hero = elf
            hero.MyName_name = MyName
            break
        elif choice == 3:
            hero = ppl
            hero.MyName_name = MyName
            break
        elif choice == 4:
            hero = dwarf
            hero.MyName_name = MyName
            break
        elif choice == 5:
            hero = hobbit
            hero.MyName_name = MyName
            break
        elif choice == 5:
            hero = goblin
            hero.MyName_name = MyName
            break
        else:
            print("Ошибка!")
    menu_choice(hero, enemy)
    return hero


#

def enemy_choice(ork, elf, ppl, dwarf, hobbit, goblin):
    while True:
        choice = random.randint(1, 6)
        if choice == 1:
            enemy = ork
            break
        elif choice == 2:
            enemy = elf
            break
        elif choice == 3:
            enemy = ppl
            break
        elif choice == 4:
            enemy = dwarf
            break
        elif choice == 5:
            enemy = hobbit
            break
        elif choice == 6:
            enemy = goblin
            break
    return enemy


#


def menu_choice(hero, enemy):
    print('Приветствую тебя ' + hero.MyName_name + hero.name_character)
    print('Сделай выбор:')
    enemy_choice(ork, elf, ppl, dwarf, hobbit, goblin)
    print('1 - снаряжение')
    print('2 - магазин')
    print('3 - профиль')
    print('4 - в бой')
    while True:
        choice = int(input('Сделай выбор ? :'))
        if choice == 1:
            inventory_choice()
            break
        elif choice == 2:
            shop_choice()
            break
        elif choice == 3:
            profile_choice()
            break
        elif choice == 4:
            battle_choice(hero, enemy)
            break
        else:
            print('Ошибка')
    return


#


# def inventory_choice():
#     print("Инвентарь")
#     print("Уже одето: ")
#     print("Голова: " + head['name'])
#     print("Правая рука: " + right_hand['name'])
#     print("Левая рука: " + left_hand['name'])
#     print("Торс: " + torso['name'])
#     print("штаны: " + trousers['name'])
#     print("ноги: " + legs['name'])
#     print("Дополнительные аксесуары: " + accessory_1['name'] + accessory_2['name'] + accessory_3['name'])
#     print("список что есть: ")
#     print("Нажми - 1 чтобы поменять снаряжение")
#     print("Нажми -  2 чтобы посмотреть свое снаряжение")
#     print("Нажми - 3 чтобы попасть в главное меню")
#     while True:
#         choice = int(input('Сделай выбор ? :'))
#         if choice == 1:
#             print("1 - Голова: " + head['name'])
#             print("2 - Правая рука: " + right_hand['name'])
#             print("3 - Левая рука: " + left_hand['name'])
#             print("4 - Торс: " + torso['name'])
#             print("5 - Штаны: " + trousers['name'])
#             print("6 - Ноги: " + legs['name'])
#             print("7 - ополнительные аксесуары:  " + accessory_1['name'] + accessory_2['name'] + accessory_3['name'])
#             print("8 - Назад")
#             while True:  #head['n']>0 or right_hand['n']>0 or left_hand['n']>0 or torso['n']>0 or trousers['n']>0 or legs['n']>0 or accessory_1['n']>0 or accessory_2['n']>0 or accessory_3['n']>0:
#                 choice = int(input())
#                 if choice == 1:
#                     print("Голова ")
#                     print('У тебя есть: ')
#                     print('Напиши что хочешь одеть: ')
#                     while True: # head['n']>0:
#                         choice = input()
#                         if choice == 'wood':
#                             head['speed'] = wood_helmet['speed']
#                             head['power'] = wood_helmet['power']
#                             head['defense'] = wood_helmet['defense']
#                             head['luck'] = wood_helmet['luck']
#                             head['hp'] = wood_helmet['hp']
#                             head['name'] = wood_helmet['name']
#                             print(inventory_choice())
#                             break
#                         else:
#                             print('Ошибка')
#                             break
#                 elif choice == 2:
#                     print("Правая рука")
#                     print('У тебя есть: ')
#                     print('Напиши что хочешь одеть: ')
#                     while True:  # head['n']>0:
#                         choice = input()
#                         if choice == 'sword':
#                             right_hand['speed'] = wooden_sword['speed']
#                             right_hand['power'] = wooden_sword['power']
#                             right_hand['defense'] = wooden_sword['defense']
#                             right_hand['luck'] = wooden_sword['luck']
#                             right_hand['hp'] = wooden_sword['hp']
#                             right_hand['name'] = wooden_sword['name']
#                             print(inventory_choice())
#                             break
#                         else:
#                             print('Ошибка')
#                             break
#                 elif choice == 3:
#                     print("Правая рука")
#                     print('У тебя есть: ')
#                     print('Напиши что хочешь одеть: ')
#                     while True:  # head['n']>0:
#                         choice = input()
#                         if choice == 'sword':
#                             right_hand['speed'] = wooden_sword['speed']
#                             right_hand['power'] = wooden_sword['power']
#                             right_hand['defense'] = wooden_sword['defense']
#                             right_hand['luck'] = wooden_sword['luck']
#                             right_hand['hp'] = wooden_sword['hp']
#                             right_hand['name'] = wooden_sword['name']
#                             print(inventory_choice())
#                             break
#                         else:
#                             print('Ошибка')
#                             break
#                 elif choice == 4:
#                     print("Правая рука")
#                     print('У тебя есть: ')
#                     print('Напиши что хочешь одеть: ')
#                     while True:  # head['n']>0:
#                         choice = input()
#                         if choice == 'sword':
#                             right_hand['speed'] = wooden_sword['speed']
#                             right_hand['power'] = wooden_sword['power']
#                             right_hand['defense'] = wooden_sword['defense']
#                             right_hand['luck'] = wooden_sword['luck']
#                             right_hand['hp'] = wooden_sword['hp']
#                             right_hand['name'] = wooden_sword['name']
#                             print(inventory_choice())
#                             break
#                         else:
#                             print('Ошибка')
#                             break
#                 elif choice == 5:
#                     print("Правая рука")
#                     print('У тебя есть: ')
#                     print('Напиши что хочешь одеть: ')
#                     while True:  # head['n']>0:
#                         choice = input()
#                         if choice == 'sword':
#                             right_hand['speed'] = wooden_sword['speed']
#                             right_hand['power'] = wooden_sword['power']
#                             right_hand['defense'] = wooden_sword['defense']
#                             right_hand['luck'] = wooden_sword['luck']
#                             right_hand['hp'] = wooden_sword['hp']
#                             right_hand['name'] = wooden_sword['name']
#                             print(inventory_choice())
#                             break
#                         else:
#                             print('Ошибка')
#                             break
#                 elif choice == 6:
#                     print("Правая рука")
#                     print('У тебя есть: ')
#                     print('Напиши что хочешь одеть: ')
#                     while True:  # head['n']>0:
#                         choice = input()
#                         if choice == 'sword':
#                             right_hand['speed'] = wooden_sword['speed']
#                             right_hand['power'] = wooden_sword['power']
#                             right_hand['defense'] = wooden_sword['defense']
#                             right_hand['luck'] = wooden_sword['luck']
#                             right_hand['hp'] = wooden_sword['hp']
#                             right_hand['name'] = wooden_sword['name']
#                             print(inventory_choice())
#                             break
#                         else:
#                             print('Ошибка')
#                             break
#                 elif choice == 7:
#                     print("Правая рука")
#                     print('У тебя есть: ')
#                     print('Напиши что хочешь одеть: ')
#                     while True:  # head['n']>0:
#                         choice = input()
#                         if choice == 'sword':
#                             right_hand['speed'] = wooden_sword['speed']
#                             right_hand['power'] = wooden_sword['power']
#                             right_hand['defense'] = wooden_sword['defense']
#                             right_hand['luck'] = wooden_sword['luck']
#                             right_hand['hp'] = wooden_sword['hp']
#                             right_hand['name'] = wooden_sword['name']
#                             print(inventory_choice())
#                             break
#                         else:
#                             print('Ошибка')
#                             break
#                 elif choice == 8:
#                     print("Правая рука")
#                     print('У тебя есть: ')
#                     print('Напиши что хочешь одеть: ')
#                     while True:  # head['n']>0:
#                         choice = input()
#                         if choice == 'sword':
#                             right_hand['speed'] = wooden_sword['speed']
#                             right_hand['power'] = wooden_sword['power']
#                             right_hand['defense'] = wooden_sword['defense']
#                             right_hand['luck'] = wooden_sword['luck']
#                             right_hand['hp'] = wooden_sword['hp']
#                             right_hand['name'] = wooden_sword['name']
#                             print(inventory_choice())
#                             break
#                         else:
#                             print('Ошибка')
#                             break
#         elif choice == 2:
#             print("")
#             break
#         elif choice == 3:
#             print(menu_choice())
#             break
#         else:
#             print('Ошибка')
#             break
#     return

#


def battle_choice(hero, enemy):
    print('Привет!!--' + hero.MyName_name + hero.name_character)
    while hero.hp > 0 or enemy.hp > 0:
        print('Твой противник :' + enemy.name_character + '---' + str(enemy.hp))
        print('Твой герой :' + hero.name_character + '---' + str(hero.hp))
        print('Что ты будешь делать? ')
        print('1 - Атака')
        print('2 - Оборона')
        print('3 - Таран')
        while True:
            choice = int(input('Сделай выбор :'))
            if choice == 1:
                attack_choice_hero(hero,enemy)
                hero.hp = hero.hp - hero.damage
                enemy.hp = enemy.hp - enemy.damage
                break
            elif choice == 2:
                defence_choice_hero(hero,enemy)
                hero.hp = hero.hp - hero.damage
                enemy.hp = enemy.hp - enemy.damage
                break
            elif choice == 3:
                ram_choice_hero(hero,enemy)
                hero.hp = hero.hp - hero.damage
                enemy.hp = enemy.hp - enemy.damage
                break
            else:
                print('Ошибка')
                break
    else:
        if enemy.hp <= 0:
            print('Поздравляю ты победил!!!')
            print('Твой противник :' + str(enemy.name_character) + '---' + str(enemy.hp))
            print('Твой герой :' + str(hero.MyName_name) + '---' + str(hero.hp))
            menu_choice(hero, enemy)
        elif hero.hp <= 0:
            print('Увы но ты проиграл(((')
            print('Твой противник :' + str(enemy.name_character) + '---' + str(enemy.hp))
            print('Твой герой :' + str(hero.MyName_name) + '---' + str(hero.hp))
            menu_choice(hero,enemy)
    return


print('Привет! Как тебя зовут?')
hero = Hero()
enemy = Enemy()
MyName = input()
hero.MyName_name = MyName
ork = Ork()
elf = Elf()
ppl = Ppl()
dwarf = Dwarf()
hobbit = Hobbit()
goblin = Goblin()
print('Рад познакомиться ' + MyName)
print(hero_choice(ork, elf, ppl, dwarf, hobbit, goblin, enemy))
