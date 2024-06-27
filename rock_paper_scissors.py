import random
from colorama import init, Fore, Style
import pyfiglet

# Initialize colorama
init(autoreset=True)

RULES = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

CHOICES = {
    'r': "rock",
    's': "scissors",
    'p': "paper"
}

def print_title():
    title = pyfiglet.figlet_format("Rock Paper Scissors")
    print(Fore.CYAN + title + Style.RESET_ALL)

def get_user_choice():
    while True:
        user_input = input(Fore.YELLOW + "Choose [r]ock, [p]aper, or [s]cissors: " + Style.RESET_ALL).lower()
        if user_input in CHOICES:
            return CHOICES[user_input]
        print(Fore.RED + "Invalid choice. Please choose 'r', 'p', or 's'.")

def get_computer_choice():
    return random.choice(list(RULES.keys()))

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    return "user" if RULES[user_choice] == computer_choice else "computer"

def display_round_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {Fore.GREEN}{user_choice}{Style.RESET_ALL}")
    print(f"Computer chose: {Fore.RED}{computer_choice}{Style.RESET_ALL}")
    if winner == "tie":
        print(Fore.CYAN + "It's a tie!\n")
    elif winner == "user":
        print(Fore.GREEN + "You win this round!\n")
    else:
        print(Fore.RED + "Computer wins this round!\n")

def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    display_round_result(user_choice, computer_choice, winner)
    return winner

def play_game():
    rounds = 0
    while True:
        try:
            rounds = int(input(Fore.YELLOW + "How many rounds would you like to play? " + Style.RESET_ALL))
            if rounds > 0:
                break
            else:
                print(Fore.RED + "Please enter a positive number.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")

    user_points = 0
    computer_points = 0

    for _ in range(rounds):
        winner = play_round()
        if winner == "user":
            user_points += 1
        elif winner == "computer":
            computer_points += 1
        print(f"{Fore.CYAN}Current Score: {Fore.GREEN}You {user_points} - {Fore.RED}{computer_points} Computer\n")

    if user_points > computer_points:
        print(Fore.GREEN + "Congratulations! You win the game!\n")
    elif user_points < computer_points:
        print(Fore.RED + "Computer wins the game! Better luck next time!\n")
    else:
        print(Fore.CYAN + "It's a tie game!\n")

def main():
    while True:
        try:
            print_title()
            play_game()
            play_again = input(Fore.YELLOW + "Do you want to play again? (y/n): " + Style.RESET_ALL).lower()
            if play_again != 'y':
                print(Fore.CYAN + "Thanks for playing! Goodbye!")
                break
        except KeyboardInterrupt:
            print(Fore.RED + "\n\nGame interrupted. Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
