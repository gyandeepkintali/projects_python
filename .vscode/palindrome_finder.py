name = input("Enter your name: ")
def is_palindrome(s):
    length = len(s)
    i = 0
    while i <length//2:
        if s[i] != s[length - i - 1]:
            return False
        i += 1
    return True
if is_palindrome(name):
    print(f"{name} is a palindrome.")
else:
    print(f"{name} is not a palindrome.")


