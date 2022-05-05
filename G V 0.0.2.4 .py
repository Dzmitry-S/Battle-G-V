import random

# выбор героя
#ork = 1
#elf = 2
#ppl = 3

delta = {'ram':0, 'fight':0,'defense':0}
hero = {'speed':0,'power':0,'hp':0,'name':0,'defense':0,'luck':0,'damage_hero':0}
enemy = {'speed':0,'power':0,'hp':0,'name':0,'defense':0,'luck':0,'damage_enemy':0}
location = {'menu':0,'battle':0,'inventory':0,'profile':0,'shop':0}
items = {}

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
            hero['speed'] = ork ['speed']
            hero['power'] = ork['power']
            hero['hp'] = ork['hp']
            hero['name'] = ork['name']
            hero['defense'] = ork['defense']
            hero['luck'] = ork['luck']
            menu_choice()
            break
        elif choice == 2:
            hero['speed'] = elf['speed']
            hero['power'] = elf['power']
            hero['hp'] = elf['hp']
            hero['name'] = elf['name']
            hero['defense'] = elf['defense']
            hero['luck'] = elf['luck']
            menu_choice()
            break
        elif choice == 3:
            hero['speed'] = ppl['speed']
            hero['power'] = ppl['power']
            hero['hp'] = ppl['hp']
            hero['name'] = ppl['name']
            hero['defense'] = ppl['defense']
            hero['luck'] = ppl['luck']
            menu_choice()
            break
        else:
            print("Ошибка!")
    return


#

def enemy_choice():
    while True:
        choice = random.randint(1,3)
        if choice == 1:
            enemy['speed'] = ork['speed']
            enemy['power'] = ork['power']
            enemy['hp'] = ork['hp']
            enemy['name'] = ork['name']
            enemy['defense'] = ork['defense']
            enemy['luck'] = ork['luck']
            break
        elif choice == 2:
            enemy['speed'] = elf['speed']
            enemy['power'] = elf['power']
            enemy['hp'] = elf['hp']
            enemy['name'] = elf['name']
            enemy['defense'] = elf['defense']
            enemy['luck'] = elf['luck']
            break
        elif choice == 3:
            enemy['speed'] = ppl['speed']
            enemy['power'] = ppl['power']
            enemy['hp'] = ppl['hp']
            enemy['name'] = ppl['name']
            enemy['defense'] = ppl['defense']
            enemy['luck'] = ppl['luck']
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
            print(menu_choice())
        elif hero['hp']<=0:
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





