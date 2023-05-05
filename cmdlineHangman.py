import random

def get_random_word():
    words = ['apple', 'banana', 'grapefruit', 'kiwi', 'orange', 'pineapple', 'strawberry']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def main():
    print("Welcome to Hangman!")
    word = get_random_word()
    guessed_letters = []
    attempts = 7

    print("You have 7 attempts to guess the word.")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts remaining.")
        else:
            print("Correct!")

        current_display = display_word(word, guessed_letters)
        print(current_display)

        if "_" not in current_display:
            print("Congratulations! You've guessed the word correctly!")
            break

    if attempts == 0:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    main()
