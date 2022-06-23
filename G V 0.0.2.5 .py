import random
from G_V_character import  ParentCharacter, Enemy,Hero,Ork,Elf,Ppl,Dwarf,Hobbit,Goblin


def attack_choice_hero():
    while True:
        choice_enemy = random.randint(1,3)
        if choice_enemy == 1: # если атака/атака
            hero['damage_hero'] = (enemy['power']*2+enemy['luck']*2+enemy['speed']*1.5)*2
            enemy['damage_enemy'] = (hero['power']*2+hero['luck']*2+hero['speed']*1.5)*2
            break
        elif choice_enemy == 2:
            hero['damage_hero'] = (enemy['defense']*3+enemy['power']+enemy['luck']*2)*2
            enemy['damage_enemy'] = (hero['power']*2+hero['luck']*2+hero['speed']*1.5)/2
            break
        elif choice_enemy == 3:
            hero['damage_hero'] = (enemy['speed']*2+enemy['power']*2+enemy['luck'])*3
            enemy['damage_enemy'] = (hero['power']*2+hero['luck']*2+hero['speed']*1.5)*1.5
            break
    return

def defence_choice_hero():
    while True:
        choice_enemy = random.randint(1,3)
        if choice_enemy == 1:# если атака/атака
            hero['damage_hero'] = (enemy['power']*2+enemy['luck']*2+enemy['speed']*1.5)/2
            enemy['damage_enemy'] = (hero['defense']*3+hero['luck']*2+hero['power'])*2
            break
        elif choice_enemy == 2:
            hero['damage_hero'] = 0
            enemy['damage_enemy'] = 0
            break
        elif choice_enemy == 3:
            hero['damage_hero'] = enemy['speed']*2+enemy['power']*2+enemy['luck']
            enemy['damage_enemy'] = hero['defense']*3+hero['luck']*2+hero['power']
            break
    return

def ram_choice_hero():
    while True:
        choice_enemy = random.randint(1,3)
        if choice_enemy == 1: # если атака/атака
            hero['damage_hero'] = (enemy['power']*2+enemy['luck']*2+enemy['speed']*1.5)*1.5
            enemy['damage_enemy'] = (hero['power']*2+hero['luck']+hero['speed']*2)*3
            break
        elif choice_enemy == 2:
            hero['damage_hero'] = enemy['defense']*3+enemy['power']+enemy['luck']*2
            enemy['damage_enemy'] = hero['power']*2+hero['luck']+hero['speed']*2
            break
        elif choice_enemy == 3:
            hero['damage_hero'] = enemy['speed']*2+enemy['power']*2+enemy['luck']
            enemy['damage_enemy'] = hero['power']*2+hero['luck']+hero['speed']*2
            break
    return




#

def hero_choice():
    print('Выбери за кого ты будешь драться:')
    print('1 - Орк'
          '2 - Эльф'
          '3 - Человек'
          '4 - Гном'
          '5 - Хоббит'
          '6 - Гоблин')
    while True:
        choice = int(input('Сделай выбор ? :'))
        if choice == 1:
            Hero = Ork
            break
        elif choice == 2:
            Hero = Elf
            break
        elif choice == 3:
            Hero = Ppl
            break
        elif choice == 4:
            Hero = Dwarf
            break
        elif choice == 5:
            Hero = Hobbit
            break
        elif choice == 5:
            Hero = Goblin
            break
        else:
            print("Ошибка!")
    menu_choice()
    return


#

def enemy_choice():
    while True:
        choice = random.randint(1,6)
        if choice == 1:
            Enemy = Ork
            break
        elif choice == 2:
            Enemy = Elf
            break
        elif choice == 3:
            Enemy = Ppl
            break
        elif choice == 4:
            Enemy = Dwarf
            break
        elif choice == 5:
            Enemy = Hobbit
            break
        elif choice == 5:
            Enemy = Goblin
            break
    return


#



def menu_choice():
    print('Приветствую тебя '+myName+hero['name'])
    print('Сделай выбор:')
    print('1 - снаряжение')
    print('2 - магазин')
    print('3 - профиль')
    print('4 - в бой')
    while True:
        choice = int(input('Сделай выбор ? :'))
        if choice == 1:
            print(inventory_choice())
            break
        elif choice == 2:
            print(shop_choice())
            break
        elif choice == 3:
            print(profile_choice())
            break
        elif choice == 4:
            print(battle_choice())
            break
        else:
            print('Ошибка')
    return



#


def inventory_choice():
    print("Инвентарь")
    print("Уже одето: ")
    print("Голова: " + head['name'])
    print("Правая рука: " + right_hand['name'])
    print("Левая рука: " + left_hand['name'])
    print("Торс: " + torso['name'])
    print("штаны: " + trousers['name'])
    print("ноги: " + legs['name'])
    print("Дополнительные аксесуары: " + accessory_1['name'] + accessory_2['name'] + accessory_3['name'])
    print("список что есть: ")
    print("Нажми - 1 чтобы поменять снаряжение")
    print("Нажми -  2 чтобы посмотреть свое снаряжение")
    print("Нажми - 3 чтобы попасть в главное меню")
    while True:
        choice = int(input('Сделай выбор ? :'))
        if choice == 1:
            print("1 - Голова: " + head['name'])
            print("2 - Правая рука: " + right_hand['name'])
            print("3 - Левая рука: " + left_hand['name'])
            print("4 - Торс: " + torso['name'])
            print("5 - Штаны: " + trousers['name'])
            print("6 - Ноги: " + legs['name'])
            print("7 - ополнительные аксесуары:  " + accessory_1['name'] + accessory_2['name'] + accessory_3['name'])
            print("8 - Назад")
            while True:  #head['n']>0 or right_hand['n']>0 or left_hand['n']>0 or torso['n']>0 or trousers['n']>0 or legs['n']>0 or accessory_1['n']>0 or accessory_2['n']>0 or accessory_3['n']>0:
                choice = int(input())
                if choice == 1:
                    print("Голова ")
                    print('У тебя есть: ')
                    print('Напиши что хочешь одеть: ')
                    while True: # head['n']>0:
                        choice = input()
                        if choice == 'wood':
                            head['speed'] = wood_helmet['speed']
                            head['power'] = wood_helmet['power']
                            head['defense'] = wood_helmet['defense']
                            head['luck'] = wood_helmet['luck']
                            head['hp'] = wood_helmet['hp']
                            head['name'] = wood_helmet['name']
                            print(inventory_choice())
                            break
                        else:
                            print('Ошибка')
                            break
                elif choice == 2:
                    print("Правая рука")
                    print('У тебя есть: ')
                    print('Напиши что хочешь одеть: ')
                    while True:  # head['n']>0:
                        choice = input()
                        if choice == 'sword':
                            right_hand['speed'] = wooden_sword['speed']
                            right_hand['power'] = wooden_sword['power']
                            right_hand['defense'] = wooden_sword['defense']
                            right_hand['luck'] = wooden_sword['luck']
                            right_hand['hp'] = wooden_sword['hp']
                            right_hand['name'] = wooden_sword['name']
                            print(inventory_choice())
                            break
                        else:
                            print('Ошибка')
                            break
                elif choice == 3:
                    print("Правая рука")
                    print('У тебя есть: ')
                    print('Напиши что хочешь одеть: ')
                    while True:  # head['n']>0:
                        choice = input()
                        if choice == 'sword':
                            right_hand['speed'] = wooden_sword['speed']
                            right_hand['power'] = wooden_sword['power']
                            right_hand['defense'] = wooden_sword['defense']
                            right_hand['luck'] = wooden_sword['luck']
                            right_hand['hp'] = wooden_sword['hp']
                            right_hand['name'] = wooden_sword['name']
                            print(inventory_choice())
                            break
                        else:
                            print('Ошибка')
                            break
                elif choice == 4:
                    print("Правая рука")
                    print('У тебя есть: ')
                    print('Напиши что хочешь одеть: ')
                    while True:  # head['n']>0:
                        choice = input()
                        if choice == 'sword':
                            right_hand['speed'] = wooden_sword['speed']
                            right_hand['power'] = wooden_sword['power']
                            right_hand['defense'] = wooden_sword['defense']
                            right_hand['luck'] = wooden_sword['luck']
                            right_hand['hp'] = wooden_sword['hp']
                            right_hand['name'] = wooden_sword['name']
                            print(inventory_choice())
                            break
                        else:
                            print('Ошибка')
                            break
                elif choice == 5:
                    print("Правая рука")
                    print('У тебя есть: ')
                    print('Напиши что хочешь одеть: ')
                    while True:  # head['n']>0:
                        choice = input()
                        if choice == 'sword':
                            right_hand['speed'] = wooden_sword['speed']
                            right_hand['power'] = wooden_sword['power']
                            right_hand['defense'] = wooden_sword['defense']
                            right_hand['luck'] = wooden_sword['luck']
                            right_hand['hp'] = wooden_sword['hp']
                            right_hand['name'] = wooden_sword['name']
                            print(inventory_choice())
                            break
                        else:
                            print('Ошибка')
                            break
                elif choice == 6:
                    print("Правая рука")
                    print('У тебя есть: ')
                    print('Напиши что хочешь одеть: ')
                    while True:  # head['n']>0:
                        choice = input()
                        if choice == 'sword':
                            right_hand['speed'] = wooden_sword['speed']
                            right_hand['power'] = wooden_sword['power']
                            right_hand['defense'] = wooden_sword['defense']
                            right_hand['luck'] = wooden_sword['luck']
                            right_hand['hp'] = wooden_sword['hp']
                            right_hand['name'] = wooden_sword['name']
                            print(inventory_choice())
                            break
                        else:
                            print('Ошибка')
                            break
                elif choice == 7:
                    print("Правая рука")
                    print('У тебя есть: ')
                    print('Напиши что хочешь одеть: ')
                    while True:  # head['n']>0:
                        choice = input()
                        if choice == 'sword':
                            right_hand['speed'] = wooden_sword['speed']
                            right_hand['power'] = wooden_sword['power']
                            right_hand['defense'] = wooden_sword['defense']
                            right_hand['luck'] = wooden_sword['luck']
                            right_hand['hp'] = wooden_sword['hp']
                            right_hand['name'] = wooden_sword['name']
                            print(inventory_choice())
                            break
                        else:
                            print('Ошибка')
                            break
                elif choice == 8:
                    print("Правая рука")
                    print('У тебя есть: ')
                    print('Напиши что хочешь одеть: ')
                    while True:  # head['n']>0:
                        choice = input()
                        if choice == 'sword':
                            right_hand['speed'] = wooden_sword['speed']
                            right_hand['power'] = wooden_sword['power']
                            right_hand['defense'] = wooden_sword['defense']
                            right_hand['luck'] = wooden_sword['luck']
                            right_hand['hp'] = wooden_sword['hp']
                            right_hand['name'] = wooden_sword['name']
                            print(inventory_choice())
                            break
                        else:
                            print('Ошибка')
                            break
        elif choice == 2:
            print("")
            break
        elif choice == 3:
            print(menu_choice())
            break
        else:
            print('Ошибка')
            break
    return

#


def battle_choice():
    print('Привет!!--'+myName+str(hero['name']))
    print('Твой противник --'+ str(enemy['name']))
    while hero['hp'] >0 or enemy['hp']>0:
        print('Твой противник :' + str(enemy['name']) + '---' + str(enemy['hp']))
        print('Твой герой :' + str(hero['name']) + '---' + str(hero['hp']))
        print('Что ты будешь делать? ')
        print('1 - Атака')
        print('2 - Оборона')
        print('3 - Таран')
        while True:
            choice = int(input('Сделай выбор :'))
            if choice == 1:
                print(attack_choice_hero())
                hero['hp'] = hero['hp'] - hero['damage_hero']
                enemy['hp'] = enemy['hp'] - enemy['damage_enemy']
                break
            elif choice == 2:
                print(defence_choice_hero())
                hero['hp'] = hero['hp'] - hero['damage_hero']
                enemy['hp'] = enemy['hp'] - enemy['damage_enemy']
                break
            elif choice == 3:
                print(ram_choice_hero())
                hero['hp'] = hero['hp'] - hero['damage_hero']
                enemy['hp'] = enemy['hp'] - enemy['damage_enemy']
                break
            else:
                print('Ошибка')
                break
    else:
        if enemy['hp']<=0:
            print('Поздравляю ты победил!!!')
            print('Твой противник :' + str(enemy['name']) + '---' + str(enemy['hp']))
            print('Твой герой :' + str(hero['name']) + '---' + str(hero['hp']))
            hero['hp'] = 1000
            enemy['hp'] = 1000
            print(menu_choice())
        elif hero['hp']<=0:
            hero['hp'] = 1000
            enemy['hp'] = 1000
            print('Увы но ты проиграл(((')
            print('Твой противник :' + str(enemy['name']) + '---' + str(enemy['hp']))
            print('Твой герой :' + str(hero['name']) + '---' + str(hero['hp']))
            print(menu_choice())
    return



print('Привет! Как тебя зовут?')
MyName = input()
hero=Hero(MyName_name = MyName)
print('Рад познакомиться '+MyName)
print(enemy_choice())
print(hero_choice())





