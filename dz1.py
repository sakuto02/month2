"""ДЗ №1"""

class Hero:
    hero = 'hero'

    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp


    def introduce(self):
        return f"Hello, my name is {self.name}, my lvl is {self.lvl}, my HP = {self.hp}"


    def is_adult(self):
        return self.lvl >= 10



hero1 = Hero('Joseph Joestar', 20, 10001)
hero2 = Hero('Joline Joestar', 7, 159)





print(hero1.introduce())
print(hero2.introduce())
print(hero1.is_adult())
print(hero2.is_adult())