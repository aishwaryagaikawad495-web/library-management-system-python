import json
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

class AuthManager:

    def __init__(self):

        self.users = []

        self.load_users()


    def load_users(self):

        try:

            with open("data/users.json", "r") as file:

                data = json.load(file)


            for item in data:

                user = User(
                    item["username"],
                    item["password"],
                    item["role"],
                    item.get("member_id")
                )

                self.users.append(user)


        except (FileNotFoundError, json.JSONDecodeError):

            self.users = []

    def save_users(self):

        data=[]

        for user in self.users:

            data.append(user.to_dict())


        with open("data/users.json","w") as file:

            json.dump(data,file,indent=4)


    
    def register(self, username, password, role, member_id=None):

        for user in self.users:

            if user.username == username:

                print("\nUsername already exists!")

                return False

        hashed_password = generate_password_hash(password)

        user = User(
            username,
            hashed_password,
            role,
            member_id
        )

        self.users.append(user)


        self.save_users()

        print("\nRegistration successful!")

        return True


    def login(self, username, password):

        for user in self.users:

            if user.username == username and check_password_hash(user.password,password):

                return user


        return None