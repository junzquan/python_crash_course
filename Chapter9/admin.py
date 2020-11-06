from user import Users

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
        