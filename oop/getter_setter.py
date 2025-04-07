# make property protected
class User:
  def __init__(self, username: str, age: int, email: str, password: str):
    self.username = username
    # private attributes
    self.__age = age
    # protected attributes
    self._email = email
    self._password = password
    # self.is_logged_in = False
    # self.is_admin = False
    # self.is_superuser = False
    # self.is_active = True
    # self.is_staff = False
    # self.is_anonymous = False
    # self.is_authenticated = False
    # self.is_verified = False
    # self.is_banned = False
    # self.is_suspended = False
    # self.is_deleted = False
    # self.is_blocked = False

  def get_email(self):
    return self._email
  def set_email(self, email):
    self._email = email
  def get_password(self):
    return self._password
  def set_password(self, password):
    self._password = password
  def get_username(self):
    return self.username

user1 = User("jakanak", 21, "jk@gmail.com", "ph123!")

print(user1.username)
print(user1._email)
# print(user1.__age) # this will raise an error
print(user1.get_email())
print(user1.get_password())
print(user1.get_username())

# updating
user1.set_email("jhkan@exmp.com")
user1.set_password("jhk@1234")
print("...............AFTER UPDATE.............")
# AFTER UPDATE  
print(user1.get_email())
print(user1.get_password())
  