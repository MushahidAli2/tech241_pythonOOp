# classes

#creating a class - this is like a template
class Dog: #name of the class is best to be Capital
    animal_kind = "canine" # class variable


    def bark(self): # class function = methods
        self.animal_kind
        return "woof"

# print(Dog.animal_kind)
# print(Dog.bark(Dog))

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


