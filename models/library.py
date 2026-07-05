class Library:
    def __init__(self):
        self.books = []

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

                print(f"\n'{book.title}' updated successfully!")
                return

        print("\nBook ID not found.")

     # Count Books
    def total_books(self):

        print(f"\nTotal Books : {len(self.books)}")