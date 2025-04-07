# static property
class User:
  user_count = 0
  def __init__(self, username: str, email: str):
    self.__username = username
    self._email = email
    User.user_count += 1
  @property
  def get_user(self):
   return self.__username
  def show_user(self):
    print(f"Username: {self.__username}, Email: {self._email}")
  def get_user_count(self):
    return User.user_count

user1 = User("dk","dk@gmail.com" )
# user1.show_user()
user2 = User("pk","pk@gmail.com" )
# user2.show_user()
user3 = User("jk","jk@gmail.com" )
# user3.show_user()
# print(User.user_count)
# print(user3.get_user_count())

# static method
class BankAccount:
  interest_rate = 0.05
  def __init__(self, owner, balance: float):
    self.balance = balance
    self.owner = owner

  def _is_valid_amount(self, amount: float) -> bool:
    return isinstance(amount, (int, float)) and amount > 0


  def __log_transaction(self, transaction_type: str, amount: float):
    print(f"Logging {transaction_type} of {amount} for {self.owner.get_user}. new balance: {self.balance}")
  
  def deposit(self, amount: float):
    if not self._is_valid_amount(amount):
      raise ValueError("Amount must be positive and greater than zero")
    self.balance += amount
    self.__log_transaction("deposit", amount)
    return self.balance
  
  def withdraw(self, amount: float):
    if not self._is_valid_amount(amount):
      raise ValueError("Amount must be positive and greater than zero")
    if amount > self.balance:
      print("Insufficient funds")
    else:
      self.balance -= amount
      self.__log_transaction("withdraw", amount)
      return self.balance
  
  def transfer(self, amount: float, recipient):
    if not self._is_valid_amount(amount):
      raise ValueError("Amount must be positive and greater than zero")
    if amount > self.balance:
      print("Insufficient funds")
    else:
      self.balance -= amount
      recipient.deposit(amount)
      self.__log_transaction("transfer", amount)
      recipient.__log_transaction("received", amount)
      print(f"{self.owner.get_user} transferred {amount} to {recipient.owner.get_user}")
      print("Transfer done")
  
  @staticmethod
  def calculate_interest(amount: float) -> float:
    return amount * BankAccount.interest_rate
  def show_balance(self):
    print(f"{self.owner.get_user}'s Balance: {self.balance}")

account = BankAccount(user1, 1000)
account.show_balance()
account.deposit(550)
after_withdrawn = account.withdraw(200)
print(f"Interest on {account.owner.get_user}'s balance {after_withdrawn}: {BankAccount.calculate_interest(after_withdrawn)}")

account2 = BankAccount(user2, 500)
account2.show_balance()
account.transfer(200, account2)
# account.transfer(200, user3) # will raise an attribute error
account2.show_balance()
account.show_balance()