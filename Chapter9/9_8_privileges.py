class Users:
    def __init__(self, first_name, last_name, info):
        self.user_info = {}
        self.user_info['first_name'] = first_name
        self.user_info['last_name'] = last_name
        for key, value in info.items():
            self.user_info[key] = value

    def descirbe_user(self):
        print(self.user_info)

    def greet_user(self):
        name = self.user_info['first_name'] + " " + self.user_info['last_name']
        print(name + ", you are so cool.")


class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Admin user have these privileges: ")
        print(self.privileges)


class Admin(Users):
    def __init__(self, first_name, last_name, info):
        super().__init__(first_name, last_name, info)
        self.previleges = Privileges()


user_info = {'age': 24}
user = Admin("Martin", "Zheng", user_info)
user.descirbe_user()
user.greet_user()
user.previleges.show_privileges()
