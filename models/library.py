class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def display_books(self):
        if len(self.books) == 0:
            print("No books available.")
            return

        for book in self.books:
            book.display_book()