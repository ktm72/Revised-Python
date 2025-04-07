# make property protected
from datetime import datetime
class User:
  def __init__(self, username: str, age: int, email: str, password: str):
    self.__username = username
    self.__age = age
    self._email = email
    self._password = password

  @property
  def email(self):
    print(f"accessing email at {datetime.now()}")
    return self._email
  @email.setter
  def email(self, email):
    if not isinstance(email, str):
      raise TypeError("Email must be a string")
    if '@' not in email:
      raise ValueError("Invalid email address")
    print(f"updating email at {datetime.now()}")
    self._email = email

  @property
  def password(self):
    return self._password
  @password.setter
  def password(self, password):
    self._password = password

  @property
  def username(self):
    return self.__username
  @username.setter
  def username(self, username):
    self.__username = username

  @property
  def age(self):
    return self.__age
  @age.setter
  def age(self, age):
    print(f"updating age at {datetime.now()}")
    self.__age = age

user1 = User("jakanak", 21, "jk@gmail.com", "ph123!")
print(user1.email)
print(user1.password)
print(user1.username)
print(user1.age)
# updating
print("...............AFTER UPDATE.............")
user1.age = 34
print(user1.age)
user1.email = '2342@gmail.com'
print(user1.email)