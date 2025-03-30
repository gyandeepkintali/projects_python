
# Online Python - IDE, Editor, Compiler, Interpreter

print("welcome to treasure island")

pick = input("in lowercase letters, please type which way you would go, left or right: ")

if pick == "right":
    print("game over")
elif pick == "left":
    pick_2 = input("you have found a lake, in lower case letters, type what you want to do, swim or wait: ")
    if pick_2 == "swim":
        print("game over")
    elif pick_2 == "wait":
        pick_3 = input("you have found 3 doors, in lower case letters, type out which door you want to open, red yellow or blue: ")
        if pick_3 == "red":
            print("game over")
        elif pick_3 == "blue":
            print("game over")
        elif pick_3 == "yellow":
            print("you win")
        else:
            print("wrong input")
    else:
        print("wrong input")
else:
    print("wrong input")