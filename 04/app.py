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
    

animals = [Dog("Mruczek"), Dog("Reksio"), Cat("Filemon"), Cat("Bonifacy")]

for animal in animals:
    print(f"{animal.name} wydaje dźwięk: {animal.make_sound()}")