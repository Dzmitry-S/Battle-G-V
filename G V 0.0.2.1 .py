import random
import time

# выбор героя
#ork = 1
#elf = 2
#ppl = 3

delta = {'ram':0, 'fight':0,'defense':0}
hero = {'speed':0,'power':0,'hp':0,'name':0,'defense':0,'luck':0}
enemy = {'speed':0,'power':0,'hp':0,'name':0,'defense':0,'luck':0}
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

def attack_choise_hero():
    while True:
        choise_enemy = random.randint(1,3)
        if choise_enemy == 1: # если атака/атака
            damage_hero = (enemy['power']*2+enemy['luck']*2+enemy['speed']*1.5)*2
            damage_enemy  = (hero['power']*2+hero['luck']*2+hero['speed']*1.5)*2
            break
        elif choise_enemy == 2:
            damage_hero = (enemy['defense']*3+enemy['power']+enemy['luck']*2)*2
            damage_enemy = (hero['power']*2+hero['luck']*2+hero['speed']*1.5)/2
            break
        elif choise_enemy == 3:
            damage_hero = (enemy['speed']*2+enemy['power']*2+enemy['luck'])*3
            damage_enemy = (hero['power']*2+hero['luck']*2+hero['speed']*1.5)*1.5
            break
    return;

def defence_choise_hero():
    while True:
        choise_enemy = random.randint(1,3)
        if choise_enemy == 1: # если атака/атака
            damage_hero = (enemy['power']*2+enemy['luck']*2+enemy['speed']*1.5)/2
            damage_enemy  = (hero['defense']*3+hero['luck']*2+hero['power'])*2
            break
        elif choise_enemy == 2:
            damage_hero = 0
            damage_enemy = 0
            break
        elif choise_enemy == 3:
            damage_hero = enemy['speed']*2+enemy['power']*2+enemy['luck']
            damage_enemy = hero['defense']*3+hero['luck']*2+hero['power']
            break
    return;

def ram_choise_hero():
    while True:
        choise_enemy = random.randint(1,3)
        if choise_enemy == 1: # если атака/атака
            damage_hero = (enemy['power']*2+enemy['luck']*2+enemy['speed']*1.5)*1.5
            damage_enemy  = (hero['power']*2+hero['luck']+hero['speed']*2)*3
            break
        elif choise_enemy == 2:
            damage_hero = enemy['defense']*3+enemy['power']+enemy['luck']*2
            damage_enemy = hero['power']*2+hero['luck']+hero['speed']*2
            break
        elif choise_enemy == 3:
            damage_hero = enemy['speed']*2+enemy['power']*2+enemy['luck']
            damage_enemy = hero['power']*2+hero['luck']+hero['speed']*2
            break
    return;




#

def hero_choice():
    print('Выбери за кого ты будешь драться:')
    print('1 - Орк')
    print('2 - Человек')
    print('3 - Эльф')
    while True:
        choise = int(input('Сделай выбор ? :'))
        if choise == 1:
            hero['speed'] = ork ['speed']
            hero['power'] = ork['power']
            hero['hp'] = ork['hp']
            hero['name'] = ork['name']
            hero['defense'] = ork['defense']
            hero['luck'] = ork['luck']
            print(menu_choise())
            break
        elif choise == 2:
            hero['speed'] = elf['speed']
            hero['power'] = elf['power']
            hero['hp'] = elf['hp']
            hero['name'] = elf['name']
            hero['defense'] = elf['defense']
            hero['luck'] = elf['luck']
            print(menu_choise())
            break
        elif choise == 3:
            hero['speed'] = ppl['speed']
            hero['power'] = ppl['power']
            hero['hp'] = ppl['hp']
            hero['name'] = ppl['name']
            hero['defense'] = ppl['defense']
            hero['luck'] = ppl['luck']
            print(menu_choise())
            break
        else:
            print("Ошибка!")
    return;


#

def enemy_choise():
    while True:
        choise = random.randint(1,3)
        if choise == 1:
            enemy['speed'] = ork['speed']
            enemy['power'] = ork['power']
            enemy['hp'] = ork['hp']
            enemy['name'] = ork['name']
            enemy['defense'] = ork['defense']
            enemy['luck'] = ork['luck']
            break
        elif choise == 2:
            enemy['speed'] = elf['speed']
            enemy['power'] = elf['power']
            enemy['hp'] = elf['hp']
            enemy['name'] = elf['name']
            enemy['defense'] = elf['defense']
            enemy['luck'] = elf['luck']
            break
        elif choise == 3:
            enemy['speed'] = ppl['speed']
            enemy['power'] = ppl['power']
            enemy['hp'] = ppl['hp']
            enemy['name'] = ppl['name']
            enemy['defense'] = ppl['defense']
            enemy['luck'] = elf['luck']
            break
        return;


#



def menu_choise():
    print('Приветствую тебя '+myName+hero['name'])
    print('Сделай выбор:')
    print('1 - снаряжение')
    print('2 - магазин')
    print('3 - профиль')
    print('4 - в бой')
    while True:
        choise = int(input('Сделай выбор ? :'))
        if choise == 1:
            print(inventory_choise())
            break
        elif choise == 2:
            print(shop_choise())
            break
        elif choise == 3:
            print(profile_choise())
            break
        elif choise == 4:
            print(battle_choise())
            break
        else:
            print('Ошибка')
    return;



#



def battle_choise():
    print('Привет!!--'+myName+' '+hero['name']+'--')
    print('Твой противник --'+enemy['name']+'--')
    print(battle())
            while hero['hp'] > 0 or enemy['hp']>0:
                print('Твой противник :' + enemy['name'] + '---' + enemy['hp'])
                print('Твой герой :' + hero['name'] + '---' + hero['hp'])
                print('Что ты будешь делать? ')
                print('1 - Атака')
                print('2 - Оборона')
                print('3 - Таран')
                while True:
                    choise = int(input('Сделай выбор :'))
                    if choise == 1:
                        print(attack_choise_hero())
                        hero['hp'] = hero['hp'] - damage_hero
                        enemy['hp'] = enemy['hp'] - damage_enemy
                        break
                    elif choise == 2:
                        print(defence_choise_hero())
                        hero['hp'] = hero['hp'] - damage_hero
                        enemy['hp'] = enemy['hp'] - damage_enemy
                        break
                    elif choise == 3:
                        print(ram_choise_hero())
                        hero['hp'] = hero['hp'] - damage_hero
                        enemy['hp'] = enemy['hp'] - damage_enemy
                        break
                    else:
                        print('Ошибка')
            else:
                print('Твой противник :' + enemy['name'] + '---' + enemy['hp'])
                print('Твой герой :' + hero['name'] + '---' + hero['hp'])
                if enemy['hp']<=0:
                    print('Поздравляю ты победил!!!')
                    print(menu_choise())
                elif hero['hp']<=0:
                    print('Увы но ты проиграл(((')
                    print(menu_choise())
                    return;
            return;
    return;
















print('Привет! Как тебя зовут?')
myName = input()
print('Рад познакомиться ' + myName)
print(hero_choice()+enemy_choise())



