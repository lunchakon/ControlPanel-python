import random
import string

def generate_password():
    #Generate Password random length for the password between 8 and 32 characters
    length = random.randint(8, 32)
    characters = string.ascii_letters + string.digits + string.punctuation

    # list comprehension : with random.choice
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print(generate_password())