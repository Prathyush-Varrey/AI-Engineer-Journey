"""
6. Number Guessing Logic

Imagine the secret number is:

37

The user repeatedly enters guesses.

Your program should respond:

Guess: 20
Too low!

Guess: 50
Too high!

Guess: 37
Correct! You found it.

The program should continue asking until the user gets the correct answer.

Extra requirements

Keep track of the number of attempts.

Final output:

Correct! You found it in 3 attempts.

Focus: while loop + if/elif/else + counter.

Don't worry about generating a random number yet.
"""

secret = 37


guess_counter = 0



while True:

    guess_number = int(input("Enter A Number :"))
    print(f"Guess: {guess_number}")
    guess_counter += 1

    if secret > guess_number:
        print("Too low!")
        
    elif secret < guess_number:
        print("Too High!")
        
    else:
        print("Correct! You found it.")
        print(f"Correct! You found it in {guess_counter} attempts.")

        break
    