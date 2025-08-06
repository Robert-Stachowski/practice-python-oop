class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
       return "Zwierzę wydaje dźwięk"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        return "Hau hau"

class Cat(Animal): 
    def __init__(self, name):
        super().__init__(name) 
    def make_sound(self):
        return "Miau miau"
    
class Bird(Animal): 
    def __init__(self, name):
        super().__init__(name) 
    def make_sound(self):
        return "Ćwir ćwir"

animals = [Dog("Mruczek"), Dog("Reksio"), Cat("Filemon"), Cat("Bonifacy"), Bird("Ptaszek 1"), Bird("Ptaszek 2")]

for a in animals:
    print(f"{a.name} wydaje dźwięk: {a.make_sound()}")