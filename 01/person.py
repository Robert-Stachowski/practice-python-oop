class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Cześć, mam na imię {self.name} , mam {self.age} i mieszkam w {self.city}")

person_one = Person("Jan", 25, "Warszawie")
person_two = Person("Anna", 30, "Krakowie")
person_three = Person("Piotr", 35, "Gdańsku")

#person_one.introduce()
#person_two.introduce()
#person_three.introduce() Można tak, na piechotę ;)
#albo:

people = [person_one, person_two, person_three]
for _ in people:
    _.introduce()