# Animal Class

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

