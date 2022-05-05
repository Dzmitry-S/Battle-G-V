import random
import time

# выбор героя
#ork = 1
#elf = 2
#ppl = 3

delta = {'ram':0, 'fight':0,'defense':0}
hero = {'speed':0,'power':0,'hp':0,'name':0,'defense':0}
enemy = {'speed':0,'power':0,'hp':0,'name':0,'defense':0}
location ={'menu':0,'battle':0,'inventory':0,'profile':0,'shop':0}

# герои и их характеристика

ork_name = 'Орк'
elf_name = 'Ельф'
ppl_name = 'Человек'

ork = {}
ork['speed'] = 30
ork['power'] = 70
ork['defense'] = 50
ork['hp'] = 1000
ork['name'] = ork_name

elf = {}
elf['speed'] = 70
elf['power'] = 40
elf['defense'] = 55
elf['hp'] = 1000
elf['name'] = elf_name

ppl = {}
ppl['speed'] = 55
ppl['power'] = 60
ppl['defense'] = 60
ppl['hp'] = 1000
ppl['name'] = ppl_name

# приветствие

damage_hero = (ork['power']*2+ppl['speed']*1.5)*1.5
print(damage_hero)
ppl['hp']= ppl['hp']-damage_hero*1.5
print(ppl['hp'])