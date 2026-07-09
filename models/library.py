
import json
from models.book import Book

class Library:
    def __init__(self):
        self.books = []
        self.load_books()

    def save_books(self):

        books_data = []

        for book in self.books:
            books_data.append(book.to_dict())

        with open("data/books.json", "w") as file:
            json.dump(books_data, file, indent=4)

    def display_table_header(self):
        print("{:<10} {:<30} {:<25} {:<12}".format(
            "Book ID", "Title", "Author", "Status"))
        print("-" * 80)

    # Add a new book
    def add_book(self, book):

        for b in self.books:
            if b.book_id == book.book_id:
                print("\nBook ID already exists!")
                return

        self.books.append(book)
        self.save_books()
        print(f"\n'{book.title}' added successfully!")

    # Display all books
    def display_books(self):

        if not self.books:
            print("\nNo books available.")
            return

        print("\n================ Library Books ================")

        self.display_table_header()

        for book in self.books:
            book.display_row()

        
    # Search a book by title
    def search_book(self, title):
        if not self.books:
            print("\nNo books available.")
            return

        found = False
        print("\nSearch results")

        self.display_table_header()

        for book in self.books:

            if title.lower() in book.title.lower():

                book.display_row()
                found = True

        if not found:
            print("Book not found.")

    # Search by Book ID
    def search_book_by_id(self, book_id):
        if not self.books:
            print("\nNo books available.")
            return

        for book in self.books:

            if book.book_id == book_id:

                print("\nBook Found\n")

                self.display_table_header()

                book.display_row()

                return

        print("\nBook ID not found.")

    # Search by Author
    def search_by_author(self, author):
        if not self.books:
            print("\nNo books available.")
            return

        found = False

        print("\nBooks by Author\n")

        self.display_table_header()

        for book in self.books:

            if author.lower() in book.author.lower():

                book.display_row()
                found = True

        if not found:
            print("Author not found.")

    # Remove a book by Book ID
    def remove_book(self, book_id):
        if not self.books:
            print("\nNo books available.")
            return

        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                self.save_books()
                print(f"\n'{book.title}' removed successfully!")
                return

        print("\nBook ID not found.")

    #Edit Book
    def edit_book(self, book_id):
        if not self.books:
            print("\nNo books available.")
            return

        for book in self.books:

            if book.book_id == book_id:

                print("\nLeave blank if you don't want to change the value.")

                new_title = input("Enter New Title: ").strip()
                new_author = input("Enter New Author: ").strip()

                if new_title:
                    book.title = new_title

                if new_author:
                    book.author = new_author
                self.save_books()
                print(f"\n'{book.title}' updated successfully!")
                return

        print("\nBook ID not found.")

     # Count Books
    def total_books(self):

        print(f"\nTotal Books : {len(self.books)}")


    def load_books(self):

        try:
            with open("data/books.json", "r") as file:
                books_data = json.load(file)

            self.books = []

            for data in books_data:
                book = Book.from_dict(data)
                self.books.append(book)

        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []


    def issue_book(self, book_id, member):

        for book in self.books:

            if book.book_id == book_id:


                if book.available:

                    book.issue_book()

                    member.borrow_book(book_id)

                    self.save_books()

                    print("\nBook issued successfully!")

                    return


                else:

                    print("\nBook already issued.")

                    return


        print("\nBook not found.")


    def return_book(self, book_id,member):

        for book in self.books:

            if book.book_id == book_id:


                if not book.available:

                    book.return_book()

                    member.return_book(book_id)

                    self.save_books()

                    print("\nBook returned successfully!")

                    return


                else:

                    print("\nBook was not issued.")

                    return


        print("\nBook not found.")



    def display_available_books(self):

        if not self.books:

            print("\nNo books available.")

            return


        found = False

        print("\n================ Available Books ================")

        self.display_table_header()


        for book in self.books:

            if book.available:

                book.display_row()

                found = True


        if not found:

            print("No available books.")


    
    def display_issued_books(self):

        if not self.books:

            print("\nNo books available.")

            return


        found = False

        print("\n================ Issued Books ================")

        self.display_table_header()


        for book in self.books:

            if not book.available:

                book.display_row()

                found = True


        if not found:

            print("No issued books.")