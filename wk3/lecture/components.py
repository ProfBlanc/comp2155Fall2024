"""
validation using function-based properties
    decorators

inheritance
    creating a class BASED on another class
"""

# animal class
class Animal:
    def __init__(self, name, species, color):
        self.name = name
        self.species = species
        self.color = color
        self.sleep()
    def __str__(self):
        return f"Name={self.name}, Species={self.species}, Color={self.color}"

    def sleep(self):
        return "Animal is sleeping"
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = "Default value"
        if isinstance(value, str) and len(value) >= 3:
            self.__name = value

    @property
    def species(self):
        return self.__species
    @species.setter
    def species(self, value):
        self.__species = "feline"  # default value
        if value.lower() in "canine feline bird equine marsupial".split(" "):
            self.__species = value.lower()

# a1 = Animal(name="A Name", species='canine', color='a color')
# print(a1.species)
# a1.species = 'human'
# print(a1.species)

class Pet(Animal):

    def __init__(self, name, species, color, home, tail):
        # self.name = name
        # self.species = species
        # self.color = color

        #Animal.__init__(self, name, species, color)
        super.__init__(name, species, color)

        self.home = home
        self.tail = tail

    def get_fed(self, food):
        return "Owner has feed " + self.name + " " + food
    def sleep(self):
        return f"{self.name} will sleep for 2 hours"

# p1 = Pet(name="Scorpion", species='feline', color='yellow and black')
# print(p1)
# print(p1.get_fed("crickets"))
# print(p1.sleep())



class Person:
    # not instance attributes/properties
    # but they are class methods
    MIN_AGE = 0
    MAX_AGE = 120

    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        self.__age = value if value >= self.MIN_AGE and value <= self.MAX_AGE else self.MIN_AGE

    @staticmethod  # aka factory methods in other langs. a method that return a new instance of class
    def adult():
        return Person("Adult", 18)
    def __add__(self, other):
        # p1 + p2
        if isinstance(other, Person):
            return Person(self.name + "-" + other.name, (self.age + other.age)/2)
        else:
            return None
    def __str__(self):
        return f"Name={self.name}, Age={self.age}"



p1 = Person("Person", 30)
print(p1.MIN_AGE)
adult = Person.adult()

p3 = p1 + adult
print(p3)



# abstract class
# abstract = incomplete
# abstract class = dedicated base class
# what is a base class aka super class. a class that is used to create another class



# Shape
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)


"""
super   parent  based           older version of class


sub     child   derived         new version of class

"""
