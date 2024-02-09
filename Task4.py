import random

# Function to determine the winner based on user and computer choices
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
     return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play the game
def play_game():
    # Getting user's choice
    user_choice = input("Enter your choice select from (rock, paper, or scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    # Generating computer's choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    # Printing user's and computer's choices
    print(f"\nYour choice: {user_choice.capitalize()}")
    print(f"Computer's choice: {computer_choice.capitalize()}")

    # Determining the winner
    result = determine_winner(user_choice, computer_choice)
    print("\n" + result)

# Main function
def main():
    print("Welcome to Rock, Paper, Scissors!")

    # Playing the game
    play_game()

    # Asking user if they want to play again
    while True:
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing! Have a great day!")
            break
        play_game()

# Running the main function if the script is executed directly
if __name__ == "__main__":
    main()
