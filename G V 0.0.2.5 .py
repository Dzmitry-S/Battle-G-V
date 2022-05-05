import random
from G_V_character import Ork, ParentCharacter

# выбор героя
#ork = 1
#elf = 2
#ppl = 3

delta = {'ram':0, 'fight':0,'defense':0}
hero = {'speed':0,'power':0,'hp':0,'name':0,'defense':0,'luck':0,'damage_hero':0}
enemy = {'speed':0,'power':0,'hp':0,'name':0,'defense':0,'luck':0,'damage_enemy':0}
location = {'menu':0,'battle':0,'inventory':0,'profile':0,'shop':0}

#

wood_helmet_name = 'Деревянный шлем'
wooden_sword_name = 'Деревянный меч'



#

wood_helmet = {}
wood_helmet['speed'] = 0
wood_helmet['power'] = 0
wood_helmet['defense'] = 10
wood_helmet['luck'] = 0
wood_helmet['hp'] = 100
wood_helmet['name'] = wood_helmet_name

wooden_sword = {}
wooden_sword['speed'] = 0
wooden_sword['power'] = 10
wooden_sword['defense'] = 0
wooden_sword['luck'] = 0
wooden_sword['hp'] = 0
wooden_sword['name'] = wooden_sword_name




#

head_name = '-'
right_hand_name = '-'
left_hand_name = '-'
torso_name = '-'
trousers_name = '-'
legs_name = '-'
accessory_1_name = '-'
accessory_2_name = '-'
accessory_3_name = '-'

#

head = {}
head['speed'] = 0
head['power'] = 0
head['defense'] = 0
head['luck'] = 0
head['hp'] = 0
head['name'] = head_name
head['n'] = 1

right_hand = {}
right_hand['speed'] = 0
right_hand['power'] = 0
right_hand['defense'] = 0
right_hand['luck'] = 0
right_hand['hp'] = 0
right_hand['name'] = right_hand_name
right_hand['n'] = 1

left_hand = {}
left_hand['speed'] = 0
left_hand['power'] = 0
left_hand['defense'] = 0
left_hand['luck'] = 0
left_hand['hp'] = 0
left_hand['name'] = left_hand_name
left_hand['n'] = 1

torso = {}
torso['speed'] = 0
torso['power'] = 0
torso['defense'] = 0
torso['luck'] = 0
torso['hp'] = 0
torso['name'] = torso_name
torso['n'] = 1

trousers = {}
trousers['speed'] = 0
trousers['power'] = 0
trousers['defense'] = 0
trousers['luck'] = 0
trousers['hp'] = 0
trousers['name'] = trousers_name
trousers['n'] = 1

legs = {}
legs['speed'] = 0
legs['power'] = 0
legs['defense'] = 0
legs['luck'] = 0
legs['hp'] = 0
legs['name'] = legs_name
legs['n'] = 1

accessory_1 = {}
accessory_1['speed'] = 0
accessory_1['power'] = 0
accessory_1['defense'] = 0
accessory_1['luck'] = 0
accessory_1['hp'] = 0
accessory_1['name'] = accessory_1_name
accessory_1['n'] = 1

accessory_2 = {}
accessory_2['speed'] = 0
accessory_2['power'] = 0
accessory_2['defense'] = 0
accessory_2['luck'] = 0
accessory_2['hp'] = 0
accessory_2['name'] = accessory_2_name
accessory_2['n'] = 1

accessory_3 = {}
accessory_3['speed'] = 0
accessory_3['power'] = 0
accessory_3['defense'] = 0
accessory_3['luck'] = 0
accessory_3['hp'] = 0
accessory_3['name'] = accessory_3_name
accessory_3['n'] = 1


# герои и их характеристика

ork_name = 'Орк'
elf_name = 'Ельф'
ppl_name = 'Человек'

ork = {}
ork['speed'] = 30
ork['power'] = 70
ork['defense'] = 50
ork['luck'] = 20
ork['hp'] = 1000
ork['name'] = ork_name

elf = {}
elf['speed'] = 70
elf['power'] = 40
elf['defense'] = 55
elf['luck'] = 40
elf['hp'] = 1000
elf['name'] = elf_name

ppl = {}
ppl['speed'] = 55
ppl['power'] = 60
ppl['defense'] = 60
ppl['luck'] = 35
ppl['hp'] = 1000
ppl['name'] = ppl_name

#

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
    print('1 - Орк')
    print('2 - Эльф')
    print('3 - Человек')
    while True:
        choice = int(input('Сделай выбор ? :'))
        if choice == 1:
            auto_hero = Ork()
            break
        elif choice == 2:
            auto_hero = elf
            break
        elif choice == 3:
            auto_hero = ppl
            break
        else:
            print("Ошибка!")
    # hero['speed'] = auto_hero['speed']
    # hero['power'] = auto_hero['power']
    # hero['hp'] = auto_hero['hp'] можно у брать
    # hero['name'] = auto_hero['name']
    # hero['defense'] = auto_hero['defense']
    # hero['luck'] = auto_hero['luck']
    menu_choice()
    return


#

def enemy_choice():
    while True:
        choice = random.randint(1,3)
        if choice == 1:
            auto_enemy = ork
            break
        elif choice == 2:
            auto_enemy = elf
            break
        elif choice == 3:
            auto_enemy = ppl
            break
    enemy['speed'] = auto_enemy['speed']
    enemy['power'] = auto_enemy['power']
    enemy['hp'] = auto_enemy['hp']
    enemy['name'] = auto_enemy['name']
    enemy['defense'] = auto_enemy['defense']
    enemy['luck'] = auto_enemy['luck']
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
myName = input()
print('Рад познакомиться ' + myName)
print(enemy_choice())
print(hero_choice())





