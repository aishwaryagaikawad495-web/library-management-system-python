from models.book import Book
from models.library import Library


def display_menu():
    print("\n===================================")
    print("      Library Management System")
    print("===================================")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")


def main():

    library = Library()

    while True:

        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":

            print("\n------ Add New Book ------")

            try:
                book_id = int(input("Enter Book ID: "))
            except ValueError:
                print("Book ID must be a number.")
                continue

            title = input("Enter Book Title: ").strip()
            author = input("Enter Author Name: ").strip()

            if title == "" or author == "":
                print("Title and Author cannot be empty.")
                continue

            book = Book(book_id, title, author)
            library.add_book(book)

        elif choice == "2":

            library.display_books()

        elif choice == "3":

            title = input("Enter Book Title to Search: ")
            library.search_book(title)

        elif choice == "4":

            try:
                book_id = int(input("Enter Book ID to Remove: "))
                library.remove_book(book_id)
            except ValueError:
                print("Invalid Book ID.")

        elif choice == "5":

            print("\nThank you for using Library Management System.")
            break

        else:

            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()