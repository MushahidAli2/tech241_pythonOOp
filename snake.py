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

