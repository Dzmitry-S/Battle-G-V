
class ParentCharacter:
    def __init__(self,money = 0,hp = 0,name_character= 'Unknown',speed = 0,power = 0,defense = 0,luck = 0,magic = 0,MyName_name = 'Unknown', damage = 0):
        self.money = money #пример
        self.hp = 0
        self.speed = 0
        self.name_character = 'Unknown'
        self.power = 0
        self.defense = 0
        self.luck = 0
        self.magic = 0
        self.MyName_name = 'Unknown'
        self.damage = 0
        return

class Enemy(ParentCharacter):
    def __init__(self, money=0, hp=0, name_character='Unknown', speed=0, power=0, defense=0, luck=0, magic=0, MyName_name = 'Unknown', damage = 0):
        super(Enemy, self).__init__(money=0, hp=0, name_character='Unknown', speed=0, power=0, defense=0, luck=0, magic=0,  MyName_name = 'Unknown', damage = 0)
        self.money = money  # пример
        self.hp = 0
        self.speed = 0
        self.name_character = 'Unknown'
        self.power = 0
        self.defense = 0
        self.luck = 0
        self.magic = 0
        self.MyName_name = 'Unknown'
        self.damage = 0


class Hero(ParentCharacter):
    def __init__(self, money=0, hp=0, name_character='Unknown', speed=0, power=0, defense=0, luck=0, magic=0, MyName_name = 'Unknown',  damage = 0):
        super(Hero, self).__init__(money=0, hp=0, name_character='Unknown', speed=0, power=0, defense=0, luck=0,magic=0, MyName_name='Unknown', damage=0)
        self.money = money  # пример
        self.hp = 0
        self.speed = 0
        self.name_character = 'Unknown'
        self.power = 0
        self.defense = 0
        self.luck = 0
        self.magic = 0
        self.MyName_name = 'Unknown'
        self.damage = 0


 #1
class Ork(ParentCharacter):
    def __init__(self,money = 0,hp = 0,name_character= 'Unknown',speed = 0,power = 0,defense = 0,luck = 0,magic = 0,MyName_name = 'Unknown', damage = 0):
        super(Ork, self).__init__(money = 0,hp = 0,name_character= 'Ork',speed = 0,power = 0,defense = 0,luck = 0,magic = 0,MyName_name = 'Unknown', damage = 0)
        self.hp = 1000
        self.speed = 30
        self.luck = 20
        self.name_character = 'Ork'   # параметр
        self.defense = 50
        self.power = 70
        self.MyName_name = 'Unknown'
        self.damage = 0

    # def attack (self, character):               #характер или действие что может делать
    #     character.hp = character.hp - self.power
    #
    # def say_hello(self):
    #     print('hello my name is : ', self.name_character)

#2
class Elf(ParentCharacter):
    def __init__(self, money=0, hp=0, name_character='Unknown', speed=0, power=0, defense=0, luck=0, magic=0, MyName_name = 'Unknown', damage = 0):
        super(Elf, self).__init__(money=0, hp=0, name_character='Elf', speed=0, power=0, defense=0, luck=0, magic=0, MyName_name = 'Unknown', damage = 0)
        self.hp = 1000
        self.speed = 60
        self.luck = 45
        self.name_character = 'Elf'
        self.defense = 30
        self.power = 50
        self.MyName_name = 'Unknown'
        self.damage = 0

#3
class Ppl(ParentCharacter):
    def __init__(self, money=0, hp=0, name_character='Unknown', speed=0, power=0, defense=0, luck=0, magic=0, MyName_name = 'Unknown', damage = 0):
        super(Ppl, self).__init__(money=0, hp=0, name_character='Ppl', speed=0, power=0, defense=0, luck=0, magic=0, MyName_name = 'Unknown', damage = 0)
        self.hp = 1000
        self.speed = 50
        self.luck = 40
        self.name_character = 'Ppl'
        self.defense = 40
        self.power = 60
        self.MyName_name = 'Unknown'
        self.damage = 0

#4
class Dwarf(ParentCharacter):
    def __init__(self,money = 0,hp = 0,name_character= 'Unknown',speed = 0,power = 0,defense = 0,luck = 0,magic = 0,MyName_name = 'Unknown', damage = 0):
        super(Dwarf, self).__init__(money=0, hp=0, name_character='Dwarf', speed=0, power=0, defense=0, luck=0, magic=0, MyName_name = 'Unknown', damage = 0)
        self.hp = 1000
        self.speed = 10
        self.luck = 40
        self.name_character = 'Dwarf'
        self.defense = 60
        self.power = 60
        self.MyName_name = 'Unknown'
        self.damage = 0

#5
class Hobbit(ParentCharacter):
    def __init__(self,money = 0,hp = 0,name_character= 'Unknown',speed = 0,power = 0,defense = 0,luck = 0,magic = 0,MyName_name = 'Unknown', damage = 0):
        super(Hobbit, self).__init__(money=0, hp=0, name_character='Hobbit', speed=0, power=0, defense=0, luck=0, magic=0, MyName_name = 'Unknown', damage = 0)
        self.hp = 1000
        self.speed = 65
        self.luck = 60
        self.name_character = 'Hobbit'
        self.defense = 20
        self.power = 20
        self.MyName_name = 'Unknown'
        self.damage = 0

#6

class Goblin(ParentCharacter):
    def __init__(self, money=0, hp=0, name_character='Unknown', speed=0, power=0, defense=0, luck=0, magic=0, MyName_name = 'Unknown', damage = 0):
        super(Goblin, self).__init__(money=0, hp=0, name_character='Goblin', speed=0, power=0, defense=0, luck=0, magic=0, MyName_name = 'Unknown', damage = 0)
        self.hp = 1000
        self.speed = 90
        self.luck = 50
        self.name_character = 'Goblin'
        self.defense = 30
        self.power = 20
        self.MyName_name = 'Unknown'
        self.damage = 0














if __name__ == '__main__':
    ork_name = input()
    ork = Ork(name_character = ork_name)
    ork.say_hello()
    ork1 = Ork()
    ork2 = Ork()
    print('ork2 has hp: ', ork2.hp)

    print("ork1 attack ork2")
    ork1.attack(ork2)
    print("ork2 has hp: ", ork2.hp)