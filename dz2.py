# Родительский класс Heroes
class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        return f"{self.name} готовится к бою!"

    def attack(self):
        return f"{self.name} атакует врага!"


# Дочерний класс Archer
class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            if self.precision >= 0.5:
                return f"{self.name} выпустила стрелу!Попадание! Осталось стрел: {self.arrows}"
            else:
                return f"{self.name} выпустила стрелу, но промахнулся! Осталось стрел: {self.arrows}"
        else:
            return f"{self.name} колчан пустой!"

    def rest(self):
        self.arrows += 5
        return f"{self.name} пополнила колчан. Теперь у нee {self.arrows} стрел."

    def status(self):
        return f"Имя: {self.name}, Здоровье: {self.hp}, Стрелы: {self.arrows}, Точность: {self.precision}"




archer = Archer("Артемида", 100, 10, 0.7)
print(archer.action())
print(archer.attack())
print(archer.rest())
print(archer.status())
