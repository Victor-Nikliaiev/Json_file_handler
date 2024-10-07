import typing
from json_file_handler import JsonFileHandler


user1 = {"name": "John", "age": 30, "city": "New York"}
user2 = {"name": "Jane", "age": 25, "city": "Los Angeles"}
user3 = {"name": "Bob", "age": 40, "city": "Chicago"}
wrong_data = 3

file = JsonFileHandler("users.json")
file.append(user1, user2, user3)

class User(typing.TypedDict):
    name: str
    age: int
    city: str

data: list[User] = file.load()

for index, user in zip(range(len(data)), data):
    print(f"({index+1}) Name: {user['name']}, Age: {user['age']}, City: {user['city']}")