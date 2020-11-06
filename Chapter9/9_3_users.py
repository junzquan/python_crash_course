class Users:
    def __init__(self, first_name, last_name, **info):
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

user1 = Users("Martin", "Zheng", age=24)
user1.descirbe_user()
user1.greet_user()
