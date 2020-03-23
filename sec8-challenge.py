class BankAcc():
  balance=0

  def __init__(self,name):
    self.owner = name

  def add(self, amount):
    print(f'balance was {self.balance}')
    self.balance += amount
    print(f"added ${amount} to balance.\n Balance is now {self.balance}")

  def withdraw(self, amount):
    print(f"balance was {self.balance}")
    if self.balance>=amount:
      self.balance-=amount
      print(f"withdrew ${amount}.\n balance is now {self.balance}")
    else:
      print(f"attempting to withdraw ${amount}. \nInsufficent funds")

  def __str__(self):
    return f"BankAcc Object:\n  Owner:{self.owner}\n  Balance:{self.balance}"

acc1 = BankAcc("Frank")
print(acc1)
acc1.add(140)
acc1.withdraw(30)
acc1.withdraw(200)
print(acc1)
