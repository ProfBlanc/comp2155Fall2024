class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    # restrictions, getters and setters, decorator method
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self.__name = value
        else:
            raise ValueError(f"{value} is invalid")
    # your turn
    # code getters and setters for age and height
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >0 and value < 100:
            self.__age = value
        else:
            raise ValueError(f"{value} is invalid. Not int or not between 1 and 99")

    def run(self):
        return f"{self.name} is running"
    def jump(self):
        return f"{self.name} is jumping {self.height/4.0} inches high"
    def __str__(self):
        return f"{self.name} is {self.age} years old and has a height of {self.height} inches"

class SuperHero(Person):
    def __init__(self, name, age, height, superhero_name, power, planet):
        Person.__init__(self, name, age, height)
        # super().__init__(name, age, height)
        self.superhero_name = superhero_name
        self.power = power
        self.planet = planet
    def jump(self):
        # return f"{self.superhero_name} is jumping"
        return   self.superhero_name +   super().jump().split(self.name)[1]

    def run(self, towards_someone_or_something):
        return f"{self.superhero_name} is running towards {towards_someone_or_something}"

    def __str__(self):
        return super().__str__() + (f". Hero name is {self.superhero_name} with "
                                    f"the super power of {self.power}, born on {self.planet}.")

    def fight(self, opponent):
        return f"{self.superhero_name} is fighting {opponent}"

batman = SuperHero("Bruce Wayne", 50, 70,
                   "Batman", "Being Rich", "Earth" )

print(batman.jump())
print(batman.run("Joker"))
print(batman)
print(batman.fight("Penguin"))


class Lion:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
class Tiger:
    def __init__(self, teeth, stripes):
        self.teeth = teeth
        self.stripes = stripes

class Liger(Lion, Tiger):
    pass

value = Liger("a", "b")
