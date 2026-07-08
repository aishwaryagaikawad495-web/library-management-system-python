import json
from models.member import Member


class MemberManager:

    def __init__(self):

        self.members=[]

        self.load_members()



    def save_members(self):

        data=[]

        for member in self.members:
            data.append(member.to_dict())


        with open("data/members.json","w") as file:

            json.dump(data,file,indent=4)



    def add_member(self,member):

        for m in self.members:

            if m.member_id == member.member_id:

                print("\nMember ID already exists!")

                return


        self.members.append(member)

        self.save_members()

        print("\nMember added successfully!")



    def display_members(self):

        if not self.members:

            print("\nNo members found.")

            return


        print("\n=========== Members ===========")

        print("{:<12} {:<30} {:<15}".format(
            "ID",
            "Name",
            "Books"
        ))

        print("-"*60)


        for member in self.members:

            member.display_row()



    def search_member(self,member_id):

        for member in self.members:

            if member.member_id == member_id:

                print("\nMember Found")

                print(member.name)

                return


        print("\nMember not found")



    def remove_member(self,member_id):

        for member in self.members:

            if member.member_id == member_id:

                self.members.remove(member)

                self.save_members()

                print("\nMember removed")

                return


        print("\nMember not found")



    def load_members(self):

        try:

            with open("data/members.json","r") as file:

                data=json.load(file)


            for item in data:

                self.members.append(
                    Member.from_dict(item)
                )

        except:

            self.members=[]


    def get_member(self, member_id):

        for member in self.members:

            if member.member_id == member_id:

                return member


        return None