"""
Person
    name, age, height
    run, jump

SuperHero
    based on Person
    additional characters
        superhero_name, power, planet
    run, jump, fight

"""
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    @property  # getter aka accessor
    def name(self):
        return self.__name
    @name.setter  # aka mutator
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self.__name = value
        else:
            raise ValueError(f"{value} is not valid. ")
    # your turn. create the getters and setters
    # for height and age. Enforce your own restriction
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >=1 and value <= 100:
            self.__age = value
        else:
            raise ValueError("Invalid age. Must be between 1 and 100")
    def __str__(self):
        return (f"{self.name} is {self.age} years old "
                f"and is {self.height} inches tall")
    def run(self):
        return f"{self.name} is running"
    def jump(self):
        return f"{self.name} is jumping {self.height / 4} inches high"

class SuperHero(Person):
    def __init__(self, name, age, height, superhero_name,
                 super_power, planet):
        # Person.__init__(self, name=name, age=age, height=height)
        super().__init__(name, age, height)

        self.superhero_name = superhero_name
        self.super_power = super_power
        self.planet = planet

    #overriding a method aka replacing the bahaviour of a method
    def jump(self):
        return self.superhero_name + super().jump().split(self.name)[1]

    def run(self, enemy):
        return f"{self.superhero_name} is running towards {enemy}"

    def fight(self, enemy):
        return f"{self.superhero_name} is fighting {enemy}"

    def __str__(self):
        return (f"{super().__str__()}. SuperHero Name is {self.superhero_name} "
                f"with the super power of {self.super_power} and "
                f"was born on {self.planet}")

batman = SuperHero("Bruce Wayne", 50, 70,
                   "Batman", "Wealth",
                   "Earth")
bruce = Person("Bruce Wayne", 50, 70)
print(batman.jump())
print(bruce.jump())
print(batman.run("Joker"))
print(batman)
