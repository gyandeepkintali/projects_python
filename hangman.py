
# Online Python - IDE, Editor, Compiler, Interpreter

word = "python"
guessed = "_" * len(word)
attempts = 6

while attempts > 0 and "_" in guessed:
    guess = input("Guess a letter: ").lower()
    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                print(guessed[:index])
                print(guessed[index+1:])
                guessed = guessed[:index] + letter + guessed[index + 1:]
    else:
        attempts -= 1
    print("Word:", guessed)
    print("Attempts left:", attempts)

if "_" not in guessed:
    print("You won! The word was:", word)
else:
    print("You lost! The word was:", word)

