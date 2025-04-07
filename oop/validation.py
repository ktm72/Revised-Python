# make property protected
from datetime import datetime
class User:
  def __init__(self, username: str, age: int, email: str, password: str):
    self.username = username
    self.__age = age
    self._email = email
    self._password = password

  def get_email(self):
    print(f"accessing email at {datetime.now()}")
    return self._email
  def set_email(self, email):
    if not isinstance(email, str):
      raise TypeError("Email must be a string")
    if '@' not in email:
      raise ValueError("Invalid email address")
    print(f"updating email at {datetime.now()}")
    # if not email:
    #   raise ValueError("Email cannot be empty")
    self._email = email
  def get_password(self):
    return self._password
  def set_password(self, password):
    self._password = password
  def get_username(self):
    return self.username
  def get_age(self):
    return self.__age
  def set_age(self, age):
    self.__age = age

user1 = User("jakanak", 21, "jk@gmail.com", "ph123!")
print(user1.get_email())
print(user1.get_password())
print(user1.get_username())
print(user1.get_age())
# updating
print("...............AFTER UPDATE.............")
user1.set_age(24)
user1.set_email('2342@gmail.com')
print(user1.get_age())
print(user1.get_email())