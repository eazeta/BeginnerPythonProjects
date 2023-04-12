import sqlite3
from time import sleep

# This line allows python to connect to the contactBook database
# connect takes in a single argument: 1- the directory for the db as shown below or 2- :memory: to store in end memory
conn = sqlite3.connect('6ContactBook/contactBook.db')

# This will allow you to communicate with the database
c = conn.cursor()

# The execute method allows you to run SQL queries
# Below is a script to create the table. It's called contacts and it has 4 columns with it's corresponding data type.
# c.execute("""CREATE TABLE contacts (
#   firstName text,
#   lastName text,
#   age integer,
#   number blob
# )""")

# This script adds a contact called Emmanuel Zeta to the database
# c.execute("INSERT INTO contacts VALUES ('Manny', 'Zeta', 22, '01234567891')")

# c.execute("SELECT * FROM contacts")

# print(c.fetchall())

# c.fetchone()
# c.fetchmany(NUMBER)
# c.fetchall()

print("Welcome to your contact book!")
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

sleep(3)

if journey == "A":
  print("Welcome to Add Contact. Please have your contacts first and last names, age and phone number ready")
  firstName = input("Please enter your contact's first name: ")
  lastName = input("Please enter your contact's last name: ")
  age = int(input("Please enter your contact's age: "))
  phoneNumber = input("Please enter your contact's phone number: ")
  confirm = input(f"""Can you confirm that would like to add the following contact:
    First name = {firstName},
    Last name = {lastName},
    Age: {age},
    Phone Number: {phoneNumber}
  Y/N: """)
  confirm = confirm.upper()
  if confirm != 'Y':
    print("Uh oh!")
  else:
    c.execute(f"INSERT INTO contacts VALUES ('{firstName}', '{lastName}', '{age}', '{phoneNumber}')")
    print("Contact added")

# CHECK
print("CHECK")

c.execute("SELECT * FROM contacts")
print(c.fetchall())

# It's important that the script ends with the following:
# This commits the change to the database
conn.commit()

# This closes the connection to the database.
conn.close()