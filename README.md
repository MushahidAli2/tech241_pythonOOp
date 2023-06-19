## Object-Oriented Programming (OOP)
### Classes
A class is a blueprint for creating objects (instances) that encapsulate data and behavior. Objects are instances of a class, and they can have their own unique data and behavior while adhering to the structure defined by the class.
```python
class Dog: #name of the class is best to be Capital
    animal_kind = "canine" # class variable


    def bark(self): # class function = methods
        self.animal_kind
        return "woof"
print(Dog.animal_kind)
print(Dog.bark(Dog))

#Instatiation of class


fido = Dog()
lassie = Dog()

print(type(fido)) #<class '__main__.Dog'>
print(fido.animal_kind) #canine
print(fido.bark()) #woof

print(type(lassie)) #<class '__main__.Dog'>
print(lassie.animal_kind) #canine
print(lassie.bark()) #woof

# Class variables can be overwritten
fido.animal_kind= "big dog"
print(fido.animal_kind) #big dog
print(lassie.animal_kind) #canine

# be careful of class variables

Dog.animal_kind = "Dolphin"
print(fido.animal_kind) #big dog
print(lassie.animal_kind) # Dolphin

print(lassie.bark()) #woof

```
## Four Pillars of OOP

### 1. Abstraction
Abstraction focuses on providing essential information and hiding unnecessary details, simplifying the complexity of the system. It allows creating abstract classes with some abstract methods that must be implemented by derived classes.
```python
# file name : animal.py
class Animal:


    def __init__(self):
        self.alive = True
        self.spin = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("one breath at a time, in and out")

    def eat(self):
        print("nom nom nom")

    def procreate(self):
        print(" time to fine a mate")

    def move(self):
        print(" onwards and upwards")

cat = Animal()
cat.breathe()
```
Purpose: Abstraction helps in managing complexity, enhancing reusability, and separating high-level concepts from implementation details.


### 2. Inheritance
Inheritance allows the creation of a new class (derived class or subclass) by inheriting the properties (attributes and methods) of an existing class (base class or superclass). The derived class can extend or override the inherited properties and can have its own unique properties.
```python
# file name: reptile.py
# Showcasing Inheritance

from animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__() #initialises the parent/base class -inherit everything from Animal
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]
        self.amiotic_eggs = None

    def __seak_heat(self):
        return (" its chilly outside, ineed a sunbed")

    def _show_seek_heat(self):
        print(self.__seak_heat())

    def hunt(self):
        print("Hunting prey")

    def use_venom(self):
        print("if i have it, may as well use it")

    def attarct_mate_through_scent(self):
        print("time to put on the aftershave")

bulbasaur = Reptile()
bulbasaur.hunt()
bulbasaur.breathe()
bulbasaur._show_seek_heat()

```
Purpose: Inheritance promotes code reuse, modularity, and the ability to create specialized classes based on existing ones.
### 3. Encapsulation
Encapsulation is the bundling of data and methods (behavior) within a class, hiding the internal details from the outside world. It provides data protection by controlling access to class members (attributes and methods) using access modifiers (public, private, protected).
```python
# file name : snake.py
# showing encapsulation

from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True
        self.venom = None
        self.limbs = False
        self.tetrapod = False

    def use_tongue_to_small(self):
        print("do i say it smells nice, or tastes nice..?")

sidney = Snake()
sidney.breathe() #Animal method
sidney._show_seek_heat()# reptile method
sidney.use_tongue_to_small() # snake method

# encapsulation is really goood from protecting important variables/ objects

# types of modifiers in python-
#Public - anyone, anywhere can us eit
#private - accessible only within the class itself
#protected - accessible within the class and its subclasses

```
Purpose: Encapsulation promotes data integrity and code organization by keeping related data and methods together.

### 4. Polymorphism
Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables the same method to be called on different objects, and the behavior is determined based on the actual type of the object.
```python
# polymorphism

from snake import Snake

class Python(Snake):


    def __init__(self):
        super().__init__()
        self.large= True
        self.two_lungs= True
        self.venom = False

    def digest_large_prey(self):
            print("ok, hand me the stretchy pants")

    def constrict(self):
            print("and...squeeeeeze")

    def climb(self):
            print("up we go")

    def shed_skin(self):
            print("I'm growing out of this now")

    def breathe(self):
            print("I am breathing but I am a Python!")




peter = Python()
peter._show_seek_heat()
```
Purpose: Polymorphism enhances flexibility, code reuse, and the ability to write generic code that can work with objects of different types.

These are the fundamental concepts of object-oriented programming (OOP). Understanding and applying these concepts can lead to code that is modular, maintainable, and flexible.

