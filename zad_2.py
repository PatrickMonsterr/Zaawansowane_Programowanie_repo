from models.Book import Book
from models.Employee import Employee
from models.Library import Library
from models.Order import Order
from models.Student import Student

from datetime import date


lib1 = Library("Warszawa", "Marszalkowska", "00-001", "9-17", "123456789")
lib2 = Library("Krakow", "Florianska", "31-001", "10-18", "987654321")

emp1 = Employee("Jan", "Kowalski", date(2020, 1, 1), date(
    1980, 5, 5), "Warszawa", "Marszalkowska", "00-001", "111")
emp2 = Employee("Anna", "Nowak", date(2021, 2, 2), date(
    1985, 6, 6), "Krakow", "Florianska", "31-001", "222")
emp3 = Employee("Piotr", "Zielinski", date(2019, 3, 3), date(
    1975, 7, 7), "Gdansk", "Dluga", "80-001", "333")

s1 = Student("Student1", [60, 70])
s2 = Student("Student2", [30, 40])
s3 = Student("Student3", [90, 100])

book1 = Book(lib1, date(2000, 1, 1), "A", "B", 100)
book2 = Book(lib1, date(2001, 2, 2), "C", "D", 200)
book3 = Book(lib2, date(2002, 3, 3), "E", "F", 300)
book4 = Book(lib2, date(2003, 4, 4), "G", "H", 400)
book5 = Book(lib1, date(2004, 5, 5), "I", "J", 500)

order1 = Order(emp1, s1, [book1, book2], date(2023, 1, 1))
order2 = Order(emp2, s2, [book3, book4, book5], date(2023, 2, 2))

print(order1)
print()
print(order2)
