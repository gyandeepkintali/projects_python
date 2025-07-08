def calculator_logo():
    logo = """

    ╔═════════════════════╗
    ║     Fancy Calc      ║
    ╠═════════════════════╣
    ║  [7] [8] [9]  [/]   ║
    ║  [4] [5] [6]  [*]   ║
    ║  [1] [2] [3]  [-]   ║
    ║      [0]      [+]   ║
    ╚═════════════════════╝
    """
    return logo

print(calculator_logo())



def subtract(n1, n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def add(n1,n2):
    return n1 + n2

def divide(n1,n2):
    return n1 / n2
number_1 = float(input("what is your first number : "))
select = "y"
while select != "n":
    print("+\n-\n*\n/\n")
    operator = input("what is your opperator")
    number_2 = int(input("what is your second number : "))
    if operator == "+":
        result = add(number_1, number_2)
    elif operator == "-":
        result = subtract(number_1, number_2)
    elif operator == "*":
        result = multiply(number_1, number_2)
    elif operator == "/":
        result = divide(number_1, number_2)
    print(f"{number_1} {operator} {number_2} = {result}")
    select = input("if you want to continue, type y, if not type n ")
    if select == "y":
        number_1 = result
    