import random

# выбор героя
ork = 1
elf = 2
ppl = 3

Action = ['run', 'fight']

# герои и их характеристика

ork_name = 'Орк'
elf_name = 'Ельф'
ppl_name = 'Человек'

ork = {}
ork['speed'] = 30
ork['power'] = 60
ork['hp'] = 70
ork['name'] = ork_name

elf = {}
elf['speed'] = 70
elf['power'] = 50
elf['hp'] = 35
elf['name'] = elf_name

ppl = {}
ppl['speed'] = 55
ppl['power'] = 55
ppl['hp'] = 65
ppl['name'] = ppl_name

# приветствие


print('Привет! Как тебя зовут?')
myName = input()

print('Рад познакомиться ' + myName + '! Давай начнем сражаться)')
print('Выбери за кого ты будешь драться:')
print('1 - Орк или 2 - Человек или 3 - Эльф?')

h = input()

if h == '1':
    print('Ты выбрал Орка')
    n = 'Орк'
    h = ork
elif h == '2':
    print('Ты выбрал Человека')
    n = 'Человек'
    h = ppl
elif h == '3':
    print('Ты выбрал Эльфа')
    n = 'Эльф'
    h = elf

# Выбор противника

e = random.randint(1, 3)

if e == 1:
    ne = 'Орк'
    e = ork
elif e == 2:
    e = ppl
    ne = 'Человек'
elif e == 3:
    e = elf
    ne = 'Эльф'

# Сражение

print('Сражение')

# начинаем битву
print("Встретились орк с эльфом и хоббитом и гоблином")

# первый раунд
print("Раунд 1")

# что будет делать Герой
hAction = Action[random.randint(0, 1)]
print(n + " будет делать " + hAction)

# что будет делать Противник
eAction = Action[random.randint(0, 1)]
print(ne + " будет делать " + eAction)

# считаем склько очков заработает  h
if (hAction == 'run'):  # если h будет убегать
    hPoints = h['speed'] * h['power'] + h['hp'] - 50

if (hAction == 'fight'):  # если h будет сражаться
    hPoints = h['power'] * h['speed'] + h['hp'] - 20

# считаем склько очков заработает  e
if (eAction == 'run'):  # если e будет убегать
    ePoints = e['speed'] * e['power'] + e['hp'] - 50

if (eAction == 'fight'):  # если h будет сражаться
    ePoints = e['power'] * e['speed'] + e['hp'] - 20

# смотрим кто победил
if (hPoints > ePoints):
    print("Победил " + n + "! Сумма его очков: ")
    print(hPoints)
    print(ne + " набрал ")
    print(ePoints)

elif (ePoints > hPoints):
    print("Победил " + ne + "! Сумма его очков: ")
    print(ePoints)
    print(n + " набрал ")
    print(hPoints)

else:
    print("Ничья! Оба набрали ")
    print(str(hPoints));

print (h['name'])
