class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def describe(self):
        print(f" {self.name} pracuje na stanowisku {self.position} ")



class Teacher(Employee):
    def __init__(self, name, position, subject):
        super().__init__(name, position)
        self.subject = subject


    def describe(self):
        print(f" {self.name} jest {self.position} i uczy {self.subject} ")

e1 = Employee("Jerzy Ogórek", "Rolnik") 
e2 = Employee("Tomasz Problem", "Programista")
e3 = Employee("Michał Szpak", "Ornitolog")
e4 = Employee("Witold Boligłowa", "Farmaceuta")
t1 = Teacher("Maria Ojczenasz", "Katechetką", "Religii")
t2 = Teacher("Henryk Namysł", "Filozofem", "Filozofii")
t3 = Teacher("Brajanek Wnuczek", "Historykiem", "Historiii")
t4 = Teacher("Dorota Niuważny", "Chemiczką(Kobieta-chemik)", "Chemii")

all = [e1,e2,e3,e4,t1,t2,t3,t4]
for Employee in all:
    Employee.describe()
