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

E1 = Employee("Jerzy Ogórek", "Rolnik") 
E2 = Employee("Tomasz Problem", "Programista")
E3 = Employee("Michał Szpak", "Ornitolog")
E4 = Employee("Witold Boligłowa", "Farmaceuta")
T1 = Teacher("Maria Ojczenasz", "Katechetką", "Religii")
T2 = Teacher("Henryk Namysł", "Filozofem", "Filozofii")
T3 = Teacher("Brajanek Wnuczek", "Historykiem", "Historiii")
T4 = Teacher("Dorota Niuważny", "Chemiczką(Kobieta-chemik)", "Chemii")

All = [E1,E2,E3,E4,T1,T2,T3,T4]
for Employee in All:
    Employee.describe()
