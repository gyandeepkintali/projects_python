
# Online Python - IDE, Editor, Compiler, Interpreter
import random
from game_data import data
run = True
score = 0
while run: 
    account_a = random.choice(data)
    account_b = random.choice(data) 
    if account_a==account_b:
        account_b = random.choice(data)
    
    
    def format_data(account):
        account_name = account["name"]
        account_descr = account["profession"]
        account_nation = account["origin"]
        return f"{account_name}, a {account_descr}, from {account_nation}"
    
    print(f"Compare A: {format_data(account_a)}")
    print("VS")
    print(f"Against B: {format_data(account_b)}")
    guess = input("who has more followers A or B? ").lower()
    
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    
    if a_follower_count > b_follower_count and guess == "a":
        score += 1
        print(f"correct thats one point for you, your score is {score}")
    elif b_follower_count > a_follower_count and guess == "b":
        score += 1
        print(f"correct thats one point for you, your score is {score}")
    else:
        print(f"incorrect, please try again, final score is {score}")
        run = False