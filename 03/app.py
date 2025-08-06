class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def describe(self):
        return (f" {self.name} pracuje na stanowisku {self.position} ")



class Teacher(Employee):
    def __init__(self, name, position, subject):
        super().__init__(name, position)
        self.subject = subject


    def describe(self):
        base = super().describe()
        return (f" {base} i uczy {self.subject} ")
# tu nie jestem przekonany co do poprawności w użyciu super, ponieważ treść zadania sugeruje
# całkowite nadpisanie describe w Teacher, a nie dziedziczenie i dodawanie kolejnego atrybutu
# uważam, ze wcześniejsza wersja pliku bardziej pasowała w logikę zadania ;P albo ja nie rozumiem polecenia :D
# ale czekam na Twój komentarz :)

e1 = Employee("Jerzy Ogórek", "Rolnik") 
e2 = Employee("Tomasz Problem", "Programista")
e3 = Employee("Michał Szpak", "Ornitolog")
e4 = Employee("Witold Boligłowa", "Farmaceuta")
t1 = Teacher("Maria Ojczenasz", "Katechetka", "Religii")
t2 = Teacher("Henryk Namysł", "Filozof", "Filozofii")
t3 = Teacher("Brajanek Wnuczek", "Historyk", "Historiii")
t4 = Teacher("Dorota Niuważny", "Chemik(Kobieta-chemik)", "Chemii")

all = [e1,e2,e3,e4,t1,t2,t3,t4]
for _ in all:
    print(_.describe())
