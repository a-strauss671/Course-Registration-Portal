class LoggedInUser:
    def __init__(self, user_info):
        # self.first_name = user_info["first_name"]
        # self.last_name = user_info["last_name"]
        self.username = user_info["username"]
        # self.password = user_info["password"]
        # self.department = user_info["department"]
        # self.email = user_info["email"]
        # self.phone_number = user_info["phone_number"]
        # self.birthday = user_info["birthday"]
        self.user_type = user_info["user_type"]

    def get_user_type(self):
        return self.user_type

    def get_username(self):
        return self.username