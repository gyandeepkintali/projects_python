
# Online Python - IDE, Editor, Compiler, Interpreter

def split_bill(total_bill, tip_percentage, number_of_people):
    tip_amount = (tip_percentage / 100) * total_bill
    total_amount = total_bill + tip_amount
    per_person_share = total_amount / number_of_people

    return {
        "Total Bill (Without Tip)": total_bill,
        "Tip Percentage": tip_percentage,
        "Tip Amount": round(tip_amount, 2),
        "Total Amount (With Tip)": round(total_amount, 2),
        "Per Person Share": round(per_person_share, 2)
    }

total_bill = float(input("Enter the total bill amount: "))
tip_percentage = float(input("Enter the tip percentage: "))
number_of_people = int(input("Enter the number of people: "))

result = split_bill(total_bill, tip_percentage, number_of_people)

for key, value in result.items():
    print(f"{key}: ${value}")