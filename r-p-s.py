import random
import time
import os
from colorama import init, Fore, Style

# Initialize colorama
init()

# Function to print the choices with color
def print_choice(name, choice):
    if choice == "rock":
        color = Fore.RED
    elif choice == "paper":
        color = Fore.GREEN
    else:  # scissors
        color = Fore.BLUE

    print(f"{name}: {color}{choice}{Style.RESET_ALL}")

# Function to animate text
def animate_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()

# Function to determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "You lose!"

# Main game loop
def main():
    choices = ["rock", "paper", "scissors"]
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.YELLOW + "Rock, Paper, Scissors Game!" + Style.RESET_ALL)
        print("Choose your weapon:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 4:
                break
            if choice < 1 or choice > 4:
                raise ValueError("Invalid choice. Please choose a number between 1 and 4.")
        except ValueError as e:
            print(Fore.RED + str(e) + Style.RESET_ALL)
            time.sleep(2)
            continue

        player_choice = choices[choice - 1]
        computer_choice = random.choice(choices)

        # Display choices with a simple animation
        animate_text("Rock...")
        animate_text("Paper...")
        animate_text("Scissors...")
        animate_text("Shoot!")

        print_choice("You", player_choice)
        print_choice("Computer", computer_choice)

        # Determine and display the winner
        result = determine_winner(player_choice, computer_choice)
        print(Fore.CYAN + result + Style.RESET_ALL)

        input(Fore.YELLOW + "\nPress Enter to play again..." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
1
