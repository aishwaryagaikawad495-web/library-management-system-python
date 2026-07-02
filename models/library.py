class Library:
    def __init__(self):
        self.books = []

    # Add a new book
    def add_book(self, book):
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

    # Remove a book by Book ID
    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print("\nBook removed successfully!")
                return

        print("\nBook ID not found.")