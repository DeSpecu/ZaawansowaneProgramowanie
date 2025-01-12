class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"City: {self.city}, Street: {self.street}, Zip-Code: {self.zip_code}. "
                f"Open hours: {self.open_hours}, Phone: {self.phone}.")

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Employee: {self.first_name} {self.last_name}, Hire Date: {self.hire_date}, "
                f"Bith Date: {self.birth_date}, Address: {self.city}, {self.street}, {self.zip_code}, "
                f"Phone: {self.phone}.")

class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Author: {self.author_name} {self.author_surname}, Publication Date: {self.publication_date}, "
                f"Nr of Pages: {self.number_of_pages}, Available at: {self.library}.")

class Order:
    def __init__(self, employee, student, books, order_date):
        if not all(isinstance(book, Book) for book in books):
            raise ValueError("Not a book")
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_details = "\n".join([str(book) for book in self.books])
        return (f"Student: {self.student}, Employee: {self.employee}, Order Date: {self.order_date}. "
                f"Books:\n{books_details}")

library1 = Library("Warszawa", "Głowna 10", "00-001", "8:00-18:00", "123-456-789")
library2 = Library("Krakow", "Krzywa 6", "30-001", "9:00-17:00", "987-654-321")

book1 = Book(library1, "2020-01-15", "John", "Doe", 300)
book2 = Book(library1, "2019-06-23", "Jane", "Smith", 250)
book3 = Book(library2, "2018-11-10", "Alice", "Brown", 200)
book4 = Book(library2, "2021-05-05", "Bob", "White", 350)
book5 = Book(library1, "2022-08-19", "Charlie", "Black", 400)

employee1 = Employee("Adam", "Nowak", "2020-02-01", "1990-07-15", "Warszawa", "Główna 11", "00-002", "123-111-222")
employee2 = Employee("Ewa", "Kowalska", "2018-03-12", "1985-05-20", "Krakow", "Krzywa 6", "30-002", "987-222-333")
employee3 = Employee("Piotr", "Zielinski", "2021-09-05", "1992-09-10", "Warszawa", "Główna 12", "00-003", "123-333-444")

student1 = "Anna Maj"
student2 = "Marek Ptak"
student3 = "Kasia Wilk"

order1 = Order(employee1, student1, [book1, book2], "2023-01-10")
order2 = Order(employee2, student2, [book3, book4, book5], "2023-02-15")

print(f"Library 1: {library1}\n Library 2: {library2}")
print(f"Employee 1: {employee1}\n Employee 2: {employee2}\n Employee 3: {employee3}")
print(f"Book 1: {book1}\n Book 2: {book2}\n Book 3: {book3}\n Book 4: {book4}\n Book 5: {book5}")
print(f"Order 1: {order1}\n Order 2: {order2}")