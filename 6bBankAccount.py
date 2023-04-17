import sqlite3
import random as r

class BankAccount:
  def __init__(self, balance: float, firstName: str, lastName: str, account_number: str):
    self.balance = balance
    self.firstName = firstName
    self.lastName = lastName
    self.account_number = account_number
  
  def addAccount(self):
    c.execute("""CREATE TABLE IF NOT EXISTS bankAccounts (
      firstName text,
      lastName text,
      accountNumber text,
      balance float
    )""")
    c.execute("INSERT INTO bankAccounts VALUES(?, ?, ?, ?)", (self.firstName, self.lastName, self.account_number, self.balance))
    conn.commit()

  def deposit(self, amount: float):
    try:
      if amount < 0:
        raise ValueError('Error! You cannot depost negative funds')
      self.balance += amount
      return self.balance
    except ValueError as err:
      print(err)
  
  def withdraw(self, amount: float):
    try: 
      if amount > self.balance:
        raise ValueError('Insufficient funds')
      if amount < 0:
        raise ValueError('Error! You cannot withdraw negative funds')
      self.balance -= amount
      return self.balance
    except ValueError as err:
      print(err)

  def __str__(self):
    return f"""
    Account Owner: {self.firstName} {self.lastName}
    Account Number: {self.account_number}
    Balance: {self.balance}
    """

print("Welcome to the bank database")
exit = False 
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS bankAccounts (
  firstName text,
  lastName text,
  accountNumber text,
  balance float
)""")
stock1 = BankAccount(10000, "Emmanuel", "Zeta", 1111)
stock1.addAccount()
stock2 = BankAccount(20000, "Manny", "Zeta", 2222)
stock2.addAccount()
while exit == False:
  journey = ""
  while journey not in ['A','B','C','D']:
    journey = input("""
    Please enter the letter corresponding to what you want to do
    A - Add a bank account
    B - Remove a bank account
    C - Deposit money from a bank account
    D - Withdraw money from a bank account
    ENTER: """).upper()
    if journey == "A":
      print("Welcome to ADD ACCOUNT")
      firstName = input("Please input the client's first name: ").capitalize()
      lastName = input("Please input the client's last name: ").capitalize()
      accountNumber = r.randint(1000000,9999999)
      confirmAddAccount = input(f"""
      Please confirm the following:
      First name: {firstName}
      Last name: {lastName}
      Y/N: """).upper()
      if confirmAddAccount == 'N':
        print("Returning back to home page ...")
      elif confirmAddAccount == 'Y':
        c.execute("INSERT INTO bankAccounts VALUES(?, ?, ?, ?)", (firstName, lastName, accountNumber, 0))
        conn.commit()
        print("Success! New account has been added")
        c.execute("SELECT * FROM bankAccounts WHERE accountNumber=?", (accountNumber,))
        account = c.fetchone()
        print(f"""
    Account Owner: {account[0]} {account[1]}
    Account Number: {account[2]}
    Balance: {account[3]}
    """)
      else:
        print("Uh oh. There seems to be an error")
    elif journey == "B":
      print("Welcome to REMOVE ACCOUNT")
      removeAccountNumber = input("Please enter the account number of the account you would like to close: ")
      c.execute("SELECT * FROM bankAccounts WHERE accountNumber=?", (removeAccountNumber,))
      account = c.fetchone()
      if account:
        confirmRemoveAccount = input(f"""
        Please confirm the following account you wish to remove:
        Account Owner: {account[0]} {account[1]}
        Account Number: {account[2]}
        Balance: {account[3]}
        Y/N: """).upper()
        if confirmRemoveAccount == 'Y':
          c.execute("DELETE FROM bankAccounts WHERE accountNumber=?", (removeAccountNumber,))
          conn.commit()
          print("Account has been removed.")
      else:
        print("Account not found.")
    elif journey == "C":
      print("Welcome to DEPOSIT")
      accountNumber = input("Please enter the account number: ")
      c.execute("SELECT * FROM bankAccounts WHERE accountNumber=?", (accountNumber,))
      account = c.fetchone()
      if account:
          # Create a BankAccount instance with the data from the database
          bankAccount = BankAccount(account[3], account[0], account[1], account[2])
          print(bankAccount)
          depositAmount = float(input("Please enter how much you would like deposited: "))
          depositConfirm = input(f"Please confirm Y/N: ").upper()
          if depositConfirm == "N":
            print("Request cancelled")
          elif depositConfirm == "Y":
            newBalance = bankAccount.deposit(depositAmount)
            c.execute(f"UPDATE bankAccounts SET balance = ? WHERE accountNumber = ?",(newBalance, accountNumber))
            print(f"Your new balance is: £{newBalance}")
          else:
            print("Something went wrong.")
      else:
          print("Account not found.")
    elif journey == "D":
      print("Welcome to Withdraw")
      accountNumber = input("Please enter the account number: ")
      c.execute("SELECT * FROM bankAccounts WHERE accountNumber=?", (accountNumber,))
      account = c.fetchone()
      if account:
          # Create a BankAccount instance with the data from the database
          bankAccount = BankAccount(account[3], account[0], account[1], account[2])
          print(bankAccount)
          withdrawAmount = float(input("Please enter how much you want to withdraw: "))
          withdrawConfirm = input(f"Please confirm Y/N: ").upper()
          if withdrawConfirm == "N":
            print("Request cancelled")
          elif withdrawConfirm == "Y":
            newBalance = bankAccount.withdraw(withdrawAmount)
            c.execute(f"UPDATE bankAccounts SET balance = ? WHERE accountNumber = ?",(newBalance, accountNumber))
            print(f"Your new balance is: £{newBalance}")
          else:
            print("Something went wrong.")
      else:
          print("Account not found.")


    exitConfirmation = input("Would you like to do anything else? Please enter Y/N: ").upper()
    exit = True if exitConfirmation == "N" else False