from models.book import Book
from models.library import Library

from models.member import Member
from models.member_manager import MemberManager


def display_menu():
    print("\n===================================")
    print("      Library Management System")
    print("===================================")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book by Title")
    print("4. Search Book by ID")
    print("5. Search by Author")
    print("6. Remove Book")
    print("7. Edit Book")
    print("8. Total Books")
    print("9. Add Member")
    print("10. View Members")
    print("11. Search Member")
    print("12. Remove Member")
    print("13. Issue Book")
    print("14. Return Book")
    print("15. Exit")


def main():

    library = Library()
    member_manager = MemberManager()

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
                book_id = int(input("Enter Book ID : "))
                library.search_book_by_id(book_id)
            except ValueError:
                print("Invalid Book ID.")

        elif choice == "5":

            author = input("Enter Author Name : ")

            library.search_by_author(author)
        
        elif choice == "6":

            try:
                book_id = int(input("Enter Book ID : "))
                library.remove_book(book_id)

            except ValueError:
                print("Invalid Book ID.")

        elif choice == "7":

            try:
                book_id = int(input("Enter Book ID to Edit: "))
                library.edit_book(book_id)

            except ValueError:
                print("Invalid Book ID.") 

        elif choice == "8":
            library.total_books()

        elif choice == "9":

            print("\n------ Add New Member ------")

            try:
                member_id = int(input("Enter Member ID: "))

            except ValueError:
                print("Member ID must be a number.")
                continue


            name = input("Enter Member Name: ").strip()


            if name == "":
                print("Member name cannot be empty.")
                continue


            member = Member(member_id, name)
            member_manager.add_member(member)


        elif choice == "10":

            print("\n------ Member List ------")

            member_manager.display_members()


        elif choice == "11":

            print("\n------ Search Member ------")

            try:
                member_id = int(input("Enter Member ID: "))

            except ValueError:
                print("Invalid Member ID.")
                continue


            member_manager.search_member(member_id)


        elif choice == "12":

            print("\n------ Remove Member ------")

            try:
                member_id = int(input("Enter Member ID: "))

            except ValueError:
                print("Invalid Member ID.")
                continue


            member_manager.remove_member(member_id)

        elif choice=="13":

            try:

                book_id=int(input("Enter Book ID: "))
                member_id=int(input("Enter Member ID: "))


            except ValueError:

                print("Invalid ID")
                continue


            member = member_manager.get_member(member_id)


            if member:

                library.issue_book(book_id, member)
                member_manager.save_members()

            else:

                print("Member not found")


        elif choice == "14":

            print("\n------ Return Book ------")

            try:

                book_id = int(input("Enter Book ID: "))
                member_id = int(input("Enter Member ID: "))

            except ValueError:

                print("Invalid ID")
                continue


            member = member_manager.get_member(member_id)


            if member:

                library.return_book(book_id, member)

                # Save updated member data after removing borrowed book
                member_manager.save_members()


            else:

                print("Member not found")


        elif choice == "15":
            print("\nThank you for using Library Management System.")
            break

        else:

            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()