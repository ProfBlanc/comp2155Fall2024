class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    # valid using a method
    # @property : disguise this method
    # as a property
    @property  # getter aka accessor
    def age(self):
        return self.__age  # private

    @age.setter
    def age(self, value):
        if isinstance(value, int) and value > 0 and value < 100:
            self.__age = value
        else:
            raise ValueError(f"{value} is invalid")

    def __str__(self):
        return f"{self.name} is {self.age} years old and is {self.height} inches tall"

    def run(self):
        return f"{self.name} is running"
    def jump(self):
        return f"{self.name} is jumping {self.height/4} inches high"


class SuperHero(Person):
    def __init__(self, name, age, height, superhero_name, superhero_power, planet):
        # Person.__init__(self, name, age, height)
        super().__init__(name, age, height)
        self.superhero_name = superhero_name
        self.superhero_power = superhero_power
        self.planet = planet

    def jump(self):
        return f"{self.superhero_name} is running"
    def run(self, enemy):
        return f"{self.superhero_name} is running towards {enemy}"

    def __str__(self):
        return super().__str__() + ". " + (f"Superhero name is { self.superhero_name}"
                f" and has = {self.superhero_power} as power and "
                f"was born on {self.planet}")


bruce = Person("Bruce", 50, 70)
print(bruce)
print(bruce.run())
print(bruce.jump())


batman = SuperHero("Bruce Wayne", 50, 70, "Batman",
                   "Money", "earth")
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
class Liger(Lion, Tiger, Person):
    pass
mystery = Liger("Mystery", 50)
print(mystery)
