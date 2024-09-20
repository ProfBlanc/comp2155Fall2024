class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def __str__(self):
        return (f"{self.name} is {self.age} years old "
                f"and is {self.height} inches tall")

    # accessor and mutators aka getters and setters

    @property # define a method, disguised as a method
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        if isinstance(value, int) and value > 0 and value < 100:
            self.__age = value
        else:
            raise ValueError(f"{value} is invalid")
    # Your turn. add getters and setters for name and height
    # You decide the limitations
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) and value > 0 and value < 80:
            self.__height = value
        else:
            raise ValueError(f"{value} is invalid")

    def run(self):
        return f"{self.name} is running"
    def jump(self):
        return f"{self.name} is jumping"


class SuperHero(Person):
    def __init__(self, name, age, height, superhero_name,
                 super_power, planet):

        Person.__init__(self, name, age, height)
        # super().__init__(name, age, height)
        self.superhero_name = superhero_name
        self.super_power = super_power
        self.planet = planet


    def jump(self):
        return (f"{self.superhero_name} is "
                f"jumping {self.height / 4} inches high")

    def run(self, enemy):
        return f"{self.superhero_name} is running towards {enemy}"
    def __str__(self):
        return super().__str__() + (f". "
                                    f"{self.superhero_name} has the "
                                    f"power of {self.super_power} "
                                    f"and was born on {self.planet}")

bruce = Person("Bruce", 50, 70)
print(bruce)
print(bruce.run())
print(bruce.jump())

batman = SuperHero("Bruce Wayne", 50, 70,
                   "Batman", "Wealth",
                   "Earth")
print(batman.jump())
print(batman.run("Joker"))
print(batman)




class Lion:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
class Tiger:
    def __init__(self, stripes, teeth):
        self.stripes = stripes
        self.teeth = teeth

class Liger(Lion, Tiger):
    pass

mystery = Liger("a","b")
