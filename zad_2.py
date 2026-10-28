from datetime import date


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return (
            f"Student: {self.name}, marks: {self.marks}"
        )


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Library: {self.city}, {self.street}, "
            f"{self.zip_code}, open: {self.open_hours}, "
            f"phone: {self.phone}"
        )


class Employee:
    def __init__(
        self,
        first_name,
        last_name,
        hire_date,
        birth_date,
        city,
        street,
        zip_code,
        phone,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Employee: {self.first_name} {self.last_name}, "
            f"hired: {self.hire_date}, born: {self.birth_date}, "
            f"{self.city}, {self.street}, {self.zip_code}, "
            f"phone: {self.phone}"
        )


class Book:
    def __init__(
        self,
        library,
        publication_date,
        author_name,
        author_surname,
        number_of_pages,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Book: {self.author_name} {self.author_surname}, "
            f"pages: {self.number_of_pages}, published: "
            f"{self.publication_date}, library: {self.library}"
        )


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n".join(str(b) for b in self.books)
        return (
            f"Order date: {self.order_date}\n"
            f"Employee: {self.employee}\n"
            f"Student: {self.student}\n"
            f"Books:\n{books_str}"
        )


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
