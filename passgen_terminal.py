import string
import random

n = int(input("Enter the length of the password:"))

password = ''.join(random.choices(string.ascii_letters +string.digits + "!@#$%^&*()", k=n))

print("Password: " + str(password))
