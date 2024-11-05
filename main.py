import random
import string

def generate_password(length):
  """Generates a random password of the specified length.

  Args:
    length: The desired length of the password.

  Returns:
    A string representing the randomly generated password.
  """

  characters = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters) for i in range(length))
  return password

# Get the desired password length from the user
password_length = int(input("Enter the desired password length: "))

# Generate and print the password
password = generate_password(password_length)
print("Generated password:", password)