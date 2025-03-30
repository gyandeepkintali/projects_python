
# Online Python - IDE, Editor, Compiler, Interpreter
import random

print("welcome to rock paper scissors")

user_choice = int(input("chose 0 for rock, 1 for paper and 2 for scissors: "))
computer_choice = random.randint(0,2)
print(f"computer chose {computer_choice}")

if user_choice>= 3:
    print("you typed an invalid number")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice > user_choice:
    print("you lose!")
elif computer_choice == 0 and user_choice == 2:
    print("you lose!")
elif user_choice == computer_choice:
    print("its a draw")
elif user_choice > computer_choice:
    print("you win")
