from models import Users, ToDoItem

u = Users()
u.setUsername(input("Enter your username: "))
print(u.getUsername())