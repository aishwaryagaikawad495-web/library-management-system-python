import json
from models.user import User

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
                    item["role"]
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


    
    def register(self, username, password, role):

        for user in self.users:

            if user.username == username:

                print("\nUsername already exists!")

                return False

        user = User( username,password,role)

        self.users.append(user)


        self.save_users()

        print("\nRegistration successful!")

        return True


    def login(self, username, password):

        for user in self.users:

            if user.username == username and user.password == password:

                return user


        return None