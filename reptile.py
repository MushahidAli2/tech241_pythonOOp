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
