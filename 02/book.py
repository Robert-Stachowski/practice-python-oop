class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return (f' "{self.title}" - {self.author} ( {self.year} )')

b1 = Book("Turbo Pascal dla pierwotniaków", "Robert Es", "1982") 
b2 = Book("PHP dla Strażaków ;)", "Robert Es", "1998") 
b3 = Book("C+ dla opornych", "Robert Es", "1989") 
b4 = Book("Jak żyć bez Pythona?", "Robert Es", "2025") 
b5 = Book("Czy kodzenie to nałóg?", "Robert Es", "1999") 
b6 = Book("Gotuj z Mysql", "Robert Es", "2004") 

single = [b1,b2,b3,b4,b5,b6]
for book in single:
    print(book)