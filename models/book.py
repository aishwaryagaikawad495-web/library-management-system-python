class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display_book(self):
        print("-" * 40)
        print(f"Book ID : {self.book_id}")
        print(f"Title   : {self.title}")
        print(f"Author  : {self.author}")
        print(f"Status  : {'Available' if self.available else 'Issued'}")
        print("-" * 40)

    # NEW METHOD
    def display_row(self):
        status = "Available" if self.available else "Issued"

        print("{:<10} {:<30} {:<25} {:<12}".format(
            self.book_id,
            self.title,
            self.author,
            status
        ))