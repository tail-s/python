# PascalCase / camelCase / snake_case

class User:
    def __init__(self, user_id, username):
        # print("new user being created")
        self.id = user_id
        self.username = username
        self.followers = 0 # default value

user_1 = User("001", "Sojin")
user_2 = User("002", "Jack")

print(user_1.followers)





