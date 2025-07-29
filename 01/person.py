class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Cześć, mam na imię {self.name} , mam {self.age} i mieszkam w {self.city}")

Person_one = Person("Jan", 25, "Warszawie")
Person_two = Person("Anna", 30, "Krakowie")
Person_three = Person("Piotr", 35, "Gdańsku")

#Person_one.introduce()
#Person_two.introduce()
#Person_three.introduce() Można tak, na piechotę ;)
#albo:

People = [Person_one, Person_two, Person_three]
for Person in People:
    Person.introduce()