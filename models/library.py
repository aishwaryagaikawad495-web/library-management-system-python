class Library:
    def __init__(self):
        self.books = []

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
            print("\nNo books available in the library.")
            return

        print("\n========== Library Books ==========")

        for book in self.books:
            book.display_book()

    # Search a book by title
    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print("\nBook Found!")
                book.display_book()
                return

        print("\nBook not found.")

    # Search by Book ID
    def search_book_by_id(self, book_id):

        for book in self.books:
            if book.book_id == book_id:
                print("\nBook Found")
                book.display_book()
                return

        print("\nBook ID not found.")

    # Search by Author
    def search_by_author(self, author):

        found = False

        for book in self.books:

            if book.author.lower() == author.lower():
                book.display_book()
                found = True

        if not found:
            print("\nAuthor not found.")

    # Remove a book by Book ID
    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print("\nBook removed successfully!")
                return

        print("\nBook ID not found.")
     # Count Books
    def total_books(self):

        print(f"\nTotal Books : {len(self.books)}")