import sqlite3
from time import sleep

# This line allows python to connect to the contactBook database
# connect takes in a single argument: 1- the directory for the db as shown below or 2- :memory: to store in end memory
# conn = sqlite3.connect('6ContactBook/contactBook.db')

conn = sqlite3.connect(':memory:')

# This will allow you to communicate with the database
c = conn.cursor()

# The execute method allows you to run SQL queries
# Below is a script to create the table. It's called contacts and it has 4 columns with it's corresponding data type.
c.execute("""CREATE TABLE contacts (
  firstName text,
  lastName text,
  age integer,
  number text
)""")

# This script adds a contact called Emmanuel Zeta to the database
# c.execute("INSERT INTO contacts VALUES ('Emmanuel', 'Zeta', 22, '01234567891')")
c.execute("INSERT INTO contacts VALUES ('Emmanuel', 'Zeta', 22, '0111')")
c.execute("INSERT INTO contacts VALUES ('Manny', 'Zeta', 23, '0222')")

# c.execute("SELECT * FROM contacts")

# print(c.fetchall())

# c.fetchone()
# c.fetchmany(NUMBER)
# c.fetchall()

print("Welcome to your contact book!")
exit = ""

while exit != "N":
  journey = ""
  while journey != "A" and journey != "B" and journey != "C":
    journey = input("""Please select from the following:
      A - Add a contact
      B - Remove a contact
      C - View all contacts
      Please enter: 
      """)
    journey = journey.upper()

  print("Loading ...")

  #The sleep function is to simulate loading
  sleep(3)

  # Add contact journey
  if journey == "A":
    print("Welcome to Add Contact. Please have your contacts first and last names, age and phone number ready")
    firstName = input("Please enter your contact's first name: ")
    lastName = input("Please enter your contact's last name: ")
    age = int(input("Please enter your contact's age: "))
    phoneNumber = input("Please enter your contact's phone number: ")
    addConfirm = input(f"""Can you confirm that would like to add the following contact:
      First name = {firstName},
      Last name = {lastName},
      Age: {age},
      Phone Number: {phoneNumber}
    Y/N: """)
    addConfirm = addConfirm.upper()
    if addConfirm != 'Y':
      print("Uh oh!")
    else:
      c.execute(f"INSERT INTO contacts VALUES ('{firstName}', '{lastName}', '{age}', '{phoneNumber}')")
      # This commits the change to the database
      conn.commit()
      print("Contact added")
  # Delete contact journey
  elif journey == "B":
    print("Welcome to Remove Contact. Would you like to view your contacts before removing?")
    removeConfirm = input("Y/N: ")
    removeConfirm = removeConfirm.upper()
    if removeConfirm == "Y":
      c.execute("SELECT * FROM contacts")
      print(c.fetchall())
    contactToDelete = input("Please enter the phone number of the contact you would like to delete: ")
    print(contactToDelete)
    c.execute(f"SELECT * FROM contacts WHERE number = '{contactToDelete}'")
    print(c.fetchall())
    removeConfirm2 = input("Please confirm that this is the contact you would like to remove Y/N: ")
    removeConfirm2 = removeConfirm2.upper()
    if removeConfirm2 == "Y":
      c.execute(f"DELETE FROM contacts WHERE number = '{contactToDelete}'")
      # This commits the change to the database
      conn.commit()
      print("Contact succesfully deleted")
    else:
      print("Uh Oh")
  else:
    c.execute("SELECT * FROM contacts")
    print(c.fetchall())
  exit = input("Would you like to do something else? Y/N: ")
  exit = exit.upper()

# This closes the connection to the database.
conn.close()