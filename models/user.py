class User:

    def __init__(self, username, password, role, member_id):

        self.username = username
        self.password = password
        self.role = role
        self.member_id = member_id


    def to_dict(self):

        return {
            "username": self.username,
            "password": self.password,
            "role": self.role,
            "member_id": self.member_id
        }


    @classmethod
    def from_dict(cls, data):

        return cls(
            data["username"],
            data["password"],
            data["role"],
            data.get("member_id")
        )