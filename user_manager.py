
from user import User

class UserManager():
    def __init__(self):
        self.next_id = 1
        self.users = []

    def create_user(self, name, email, age):
        new_user = User(self.next_id, name, email, age)
        self.next_id += 1
        self.users.append(new_user)
        return new_user
    
    def find_user(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    
    def delete_user(self, user):
        self.users.remove(user)
    
    def update_user(self, user, name, email, age):
        if name is not None:
            user.name = name
        if email is not None:
            user.email = email
        if age is not None:
            user.age = age

    def get_users(self):
        return self.users.copy()


    