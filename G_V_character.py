class ParentCharacter:
    def __init__(self,money = 0,hp = 0,name_character= 'hhh',speed = 0,power = 0,defense = 0,luck = 0,magic = 0,MyName = 0):
        self.money = money #пример
        self.hp = hp
        self.speed = 0
        self.name_character = 'Unknown'
        self.power = 0
        self.defense = 0
        self.luck = 0
        self.magic = 0
        self.MyName = 'Unknown'
        return

class Ork(ParentCharacter):
    def __init__(self,money = 0,hp = 0,name_character= 'hhh',speed = 0,power = 0,defense = 0,luck = 0,magic = 0,MyName = 0):
        super(Ork, self).__init__(money = 0,hp = 0,name_character= 'hhh',speed = 0,power = 0,defense = 0,luck = 0,magic = 0,MyName = 0)
        self.hp = 1000
        self.speed = 30
        self.luck = 20
        self.name_character = name_character
        self.defense = 50
        self.power = 70

    def attack (self, character):
        character.hp = character.hp - self.power

    def say_hello(self):
        print('hello my name is : ', self.name_character)







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





# class Elf(ParentCharacter):
#     self.hp = 1000
#     self.speed = 60
#     self.luck = 45
#     self.name_character = 'Elf'
#     self.defense = 30
#     self.power = 50
#
# class Ppl(ParentCharacter):
#     self.hp = 1000
#     self.speed = 50
#     self.luck = 40
#     self.name_character = 'Ppl'
#     self.defense = 40
#     self.power = 60
#
# class Dwarf(ParentCharacter):
#     self.hp = 1000
#     self.speed = 10
#     self.luck = 40
#     self.name_character = 'Dwarf'
#     self.defense = 60
#     self.power = 60
#
# class Hobbit(ParentCharacter):
#     self.hp = 1000
#     self.speed = 65
#     self.luck = 60
#     self.name_character = 'Hobbit'
#     self.defense = 20
#     self.power = 20

