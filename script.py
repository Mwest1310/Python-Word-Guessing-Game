import random
# Sample of words to choose from.
words = ["python", "javascript", "java", "ruby", "html", "css", "sql", "swift", "kotlin", "typescript"]

def play_game():
    selected_word = random.choice(words)
    guesses_left = 12
    guessed_letters = []
    print("This is a word guessing game. You have 12 guesses to find the correct word. Each word is a type of coding language. Good luck!")

    while guesses_left > 0:
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue
        if len(guess) != 1:
            print("Please enter a single letter.")
            continue
        
        if guess in selected_word:
            for x in range(selected_word.count(guess)):
                guessed_letters.append(guess)
            print(f"Correct. The letter '{guess}' is in the word.")
            print(f"Guessed letters: {', '.join(guessed_letters)}")

        else:
            print("Incorrect. That letter is not in the word.")
            guesses_left -= 1
            print(f"You have {guesses_left} guesses left.")

        if all(letter in guessed_letters for letter in selected_word):
            print(f"You have correctly guessed the word '{selected_word}'.")
            return
        elif guesses_left == 0:
            print(f"You have run out of guesses. The correct word was '{selected_word}'.")
            return

wants_to_play = input("Do you want to play the word guessing game? (yes/no): ").lower()
if wants_to_play == "yes":
    play_game()