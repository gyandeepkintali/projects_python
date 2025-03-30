
# Online Python - IDE, Editor, Compiler, Interpreter
import random
import string

letters = list(string.ascii_lowercase)
numbers = list(map(str, range(10)))
special_keys = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

try:
    nr_letter = int(input("Enter the number of letters: "))
    nr_num = int(input("Enter the number of numbers: "))
    nr_sym = int(input("Enter the number of symbols: "))
    if nr_letter < 0 or nr_num < 0 or nr_sym < 0:
        raise ValueError("Numbers must be non-negative.")
except ValueError as e:
    print(f"Invalid input: {e}")
    exit()

password = ""

for _ in range(nr_letter):
    password += random.choice(letters)

for _ in range(nr_num):
    password += random.choice(numbers)

for _ in range(nr_sym):
    password += random.choice(special_keys)

# Shuffle the password to ensure randomness
password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)

print(f"Your password is: {password}")

    

