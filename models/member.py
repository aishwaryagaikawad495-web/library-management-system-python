class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def display_member(self):
        print("-----------------------")
        print(f"Member ID : {self.member_id}")
        print(f"Name      : {self.name}")
        print("-----------------------")