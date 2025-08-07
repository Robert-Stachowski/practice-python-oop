class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
       return "Zwierzę wydaje dźwięk"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        return f"{self.name} szczeka: Hau hau"

class Cat(Animal): 
    def __init__(self, name):
        super().__init__(name) 
    def make_sound(self):
        return f"{self.name} miauczy: Miau miau"
    
class Bird(Animal): 
    def __init__(self, name):
        super().__init__(name) 
    def make_sound(self):
        return f"{self.name} ćwierka: Ćwir ćwir"

animals = [Dog("Mruczek"), Dog("Reksio"), Cat("Filemon"), Cat("Bonifacy"), Bird("Ptaszek 1"), Bird("Ptaszek 2")]

for a in animals:
    print(a.make_sound())