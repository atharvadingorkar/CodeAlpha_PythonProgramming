import random
def display_hangman(tries):
    """Display the hangman ASCII art based on remaining tries."""
    stages = [
        # Final state: head, torso, both arms, both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # Head, torso, both arms, one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # Head, torso, both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        # Head, torso, one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        # Head, torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # Head
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # Initial empty state
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]

def play_hangman():
    """Main game function."""
    # List of predefined words
    words = ["python", "programming", "computer", "keyboard", "challenge"]
    
    # Select a random word
    word = random.choice(words)
    word_letters = set(word)  # Letters in the word
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()  # Letters guessed by the player
    
    # Game variables
    lives = 6
    word_completion = "_" * len(word)  # Display of guessed letters
    
    print("\n🎮 Welcome to Hangman! 🎮")
    print("Try to guess the word one letter at a time.")
    print(f"You have {lives} incorrect guesses available.")
    print("=" * 40)
    
    # Main game loop
    while lives > 0 and len(word_letters) > 0:
        # Display current game state
        print(display_hangman(lives))
        print(f"\nWord: {' '.join(word_completion)}")
        print(f"Guessed letters: {' '.join(sorted(used_letters))}")
        print(f"Lives remaining: {lives}")
        print("-" * 40)
        
        # Get player's guess
        guess = input("Guess a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single valid letter!")
            continue
        
        # Check if letter was already guessed
        if guess in used_letters:
            print("⚠️  You've already guessed that letter! Try again.")
            continue
        
        # Add the guessed letter to used letters
        used_letters.add(guess)
        
        # Check if the guessed letter is in the word
        if guess in word_letters:
            print(f"✅ Good guess! '{guess}' is in the word!")
            word_letters.remove(guess)
            
            # Update the word completion display
            word_completion = ''.join([letter if letter in used_letters else '_' for letter in word])
        else:
            print(f"❌ Sorry, '{guess}' is not in the word!")
            lives -= 1
    
    # Game over - check win/lose condition
    print("\n" + "=" * 40)
    if lives == 0:
        print(display_hangman(0))
        print(f"\n💀 Game Over! You lost!")
        print(f"The word was: {word}")
    else:
        print(f"\n🎉 Congratulations! You won!")
        print(f"You guessed the word: {word}")
        print(f"Lives remaining: {lives}")
    
    print("=" * 40)

def main():
    """Main function to run the game with replay option."""
    while True:
        play_hangman()
        
        # Ask if player wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing Hangman! Goodbye! 👋")
            break

# Run the game
if __name__ == "__main__":
    main()