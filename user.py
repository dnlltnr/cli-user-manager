
class User():
    def __init__(self, id, name, email, age):
        self.id = id
        self.name = name
        self.email = email
        self.age = age

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Email: {self.email} | Age: {self.age}"
    
    