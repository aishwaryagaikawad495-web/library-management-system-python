class Member:

    def __init__(self, member_id, name):

        self.member_id = member_id
        self.name = name
        self.borrowed_books = []


    def display_row(self):

        print("{:<12} {:<30} {:<15}".format(
            self.member_id,
            self.name,
            len(self.borrowed_books)
        ))


    def to_dict(self):

        return {
            "member_id": self.member_id,
            "name": self.name,
            "borrowed_books": self.borrowed_books
        }


    @classmethod
    def from_dict(cls,data):

        member = cls(
            data["member_id"],
            data["name"]
        )

        member.borrowed_books = data["borrowed_books"]

        return member