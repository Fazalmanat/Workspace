# class Secret:
#     def __init__(self):
#         self.__secret="Top Secret Data Breached!"
#     def hack(self):
#         print(self.__secret)
# attack=Secret()
# attack.hack()

# from abc import ABC,abstractmethod
# class Animal(ABC):
#     @abstractmethod 
#     def sound(self):
#         pass
    
# class Dog(Animal):
#     def sound(self):
#         print("Barking")
# d=Dog()
# d.sound()

class Library:
    def __init__(self): 
        self.books = []  
    def add_book(self):
        book = input("Enter book name: ")
        self.books.append(book)
        print("Book added successfully")
    def show_books(self):
        print("\nBooks in library:")
        for book in self.books:
            print(book)
    def borrow_book(self):
        book = input("Enter book name to borrow: ")
        if book in self.books:
            self.books.remove(book)
            print("Book borrowed successfully")
        else:
            print("Book is not available")
    def return_book(self):
        book = input("Enter book name to return: ")
        self.books.append(book)
        print("Book returned successfully")
library = Library()
while True:
            print("\n===== LIBRARY =====")
            print("1. Add Book")
            print("2. Show Books")
            print("3. Borrow Book")
            print("4. Return Book")
            print("5. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                library.add_book()
            elif choice == 2:
                library.show_books()
            elif choice == 3:
                library.borrow_book()
            elif choice == 4:
                library.return_book()
            elif choice == 5:
                print("Thank you")
                break
            else:
                print("Invalid choice") 

