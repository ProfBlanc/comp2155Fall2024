class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f"{self.name} is {self.age} years old and is {self.height} inches tall"

    # create our getters and setters aka accessors and mutators
    # to enforce restrictions.

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value if isinstance(value, str) and len(value) >= 3 else ""

    # your turn. code other two getters and setters. you decide the restrictions

    @property
    def age(self): return self.__age
    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >=0 and value <= 120:
            self.__age = value
        else:
            raise ValueError(f"{value} is not valid or not within range of 0 to 120")

    def run(self):
        return f"{self.name} is running!"
    def jump(self):
        return f"{self.name} is jumping!"

class SuperHero(Person):
    def __init__(self, name, age, height, super_hero_name, planet, power):
        Person.__init__(self, name, age, height)
        # super().__init__(name, age, height)
        self.plant = planet
        self.power = power
        self.super_hero_name = super_hero_name

    def fight(self, who="a bad guy"):
        return f"{self.super_hero_name} is fighting {who}"

    def run(self):
        return f"{self.super_hero_name} is running to save the day"
    def jump(self):

        return self.super_hero_name + super().jump().split(self.name)[1]


hero = SuperHero("Bruce Wayne", 50, 70, "Batman",
                 "Earth", "Rich")

print(hero.fight("Joker"))
print(hero.run())
print(hero.jump())



class Lion:
    def __init__(self, name, teeth):
        self.name = name
        self.teeth = teeth


# Your turn: add a toString method to SuperHero, states all attributes and their values

class Tiger:
    def __init__(self, stripes, weight):
        self.weight = weight
        self.stripes = stripes
class Liger(Lion, Tiger):
    pass

value = Liger("a", "b")

