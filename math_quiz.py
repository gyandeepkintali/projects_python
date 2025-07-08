import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(["+", "-", "*"])

    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2

    return f"What is {num1} {operation} {num2}?", answer

def math_quiz():
    score = 0
    for _ in range(5):  # Ask 5 questions
        question, correct_answer = generate_question()
        user_answer = input(question + " ")

        try:
            if int(user_answer) == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was {correct_answer}.")
        except ValueError:
            print(f"Invalid input! The correct answer was {correct_answer}.")

    print(f"\nYour final score: {score}/5")

if __name__ == "__main__":
    math_quiz()
