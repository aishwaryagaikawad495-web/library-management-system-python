from models.book import Book
from models.member import Member
from models.library import Library


def main():
    print("===================================")
    print("  Welcome to Library Management")
    print("===================================")

    # Create Library Object
    library = Library()

    # Create Book Objects
    book1 = Book(101, "Python Programming", "Guido van Rossum")
    book2 = Book(102, "Clean Code", "Robert C. Martin")

    # Create Member Object
    member = Member(1, "Aishwarya")

    print("\nMember Details")
    member.display_member()

    # Add books to library
    library.add_book(book1)
    library.add_book(book2)

    print("\nBooks in Library")
    library.display_books()


if __name__ == "__main__":
    main()