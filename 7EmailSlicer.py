#The purpose of this script is to ask the user to input an email and it will return the user name and the domain.

# A list of invalid characters
invalidCharacters = ['!', '#', '$', '%', '&', "'", '*', '+', '/', '=', '?', '^', '`', '{', '|', '}', '~', ' ', '..']

# The while True means that it will run until there is a break in the code which is an elegant way of conducting validation without having to repeat the email input.

while True:
  email = input("Please enter your email: ").lower()
  atSymbol = email.find('@')
  if email.count('@') != 1 or email[atSymbol -  1] == "." or email[0] == "." or any(char in invalidCharacters for char in email):
      print("Invalid email has been entered")
  elif len(email) > 10:
     print("Email cannot be longer that 256 characters")
  else:
    break

print(f"User name: {email[:atSymbol]}")
print(f"Domain: {email[atSymbol+1:]}")