# Paige LaFave         4/26/2024

# This script is a mock script of playing the game 'Candy Land'. You will be able to play with multiple people or against a computer (2 - 4 players).
    # The player has the option of playing the game, reading the rules, or quitting the program. 

#Sources:
    # (1) https://realpython.com/python-enumerate/ 
        # By Bryan Weber
        # Created 2012 - 2014
        # last accessed on 4/26/2025

    # (2) https://python-course.eu/tkinter/labels-in-tkinter.php 
        # By Bernd Klein
        # Created on 2/1/2022
        # last accessed on 4/26/2024

    # (3) https://www.geekyhobbies.com/candy-land-board-game-rules-and-instructions-for-how-to-play/
        # By Eric Mortensen
        # Last Updated 2024
        # last accessed on 4/26/2024

    # (4) https://instructions.hasbro.com/en-us/instruction/Candy-Land-Game
        # By Hasbro
        # Lasted Updated 2024
        # last accessed on 4/26/2024

    # (5) https://pypi.org/project/colorama/#files
        # By pypi
        # Created 10/24/2022
        #last accessed 4/26/2024

    # (6) https://www.wikihow.com/Play-Candy-Land 
        # By Glenn Carreau
        # Created 2/23/2023
        # last accessed on 4/26/2024


import random
import colorama
import tkinter as tk

colorama.init()

# ========================== Utility Functions ==========================

def print_title():
    """Prints the title material for the game."""
    print("Welcome to Candy Realm!")
    print()
    print("Created by: Paige LaFave")
    print("[COM S 127 Section A]")
    print()

def print_rules():
    """Displays the rules of the game."""
    print("Candy Realm Game Rules:")
    print("1. The game can be played with 2-4 players (including computer players).")
    print("2. This version uses a deck of cards with:")
    print("   - Single Space Cards: Move to the next space of that color.")
    print("   - Double Space Cards: Move to the second next space of that color.")
    print("   - Sweet Treat Cards: Move to the specific sweet treat location.")
    print("   - Licorice Cards: Skip your next turn.")
    print("3. The objective is to reach the end of the board first.")
    print("4. The program will automatically handle turns and movements for you.")
    print()

def play_options():
    """Allows the player to choose between playing, viewing the rules, or quitting."""
    choice = input("Please choose an option: (P)lay, (R)ules, or (Q)uit: ").strip().lower()
    return choice

# ========================== Board and Deck Setup ==========================

def create_game_board():
    """Creates the game board with color-coded spaces and sweet treat locations."""
    space_colors = [colorama.Fore.BLUE, colorama.Fore.MAGENTA, colorama.Fore.RED, 
                    colorama.Fore.GREEN, colorama.Fore.ORANGE, colorama.Fore.YELLOW]
    sweet_treats = {'Licorice1': 49, 'Licorice2': 32, 'Licorice3': 12, 
                    'Marshmallow': 8, 'Gingerbread': 55, 'Ice Cream': 15, 'Gumdrop': 64}
    
    board = [''] * 84  # Create a board with 84 spaces

    # Assign colors to spaces not occupied by sweet treats
    for i in range(len(board)):
        if i not in sweet_treats.values():
            board[i] = random.choice(space_colors) + ' ' + colorama.Style.RESET_ALL

    # Assign sweet treat names to specific board locations
    for key, value in sweet_treats.items():
        board[value] = random.choice(space_colors) + key + colorama.Style.RESET_ALL

    return board

def create_deck():
    """Creates a shuffled deck of cards for the game."""
    colors = ['Blue', 'Purple', 'Red', 'Green', 'Orange', 'Yellow']
    sweet_treats = {'Licorice1': 49, 'Licorice2': 32, 'Licorice3': 12, 
                    'Marshmallow': 8, 'Gingerbread': 55, 'Ice Cream': 15, 'Gumdrop': 64}
    
    deck = []

    # Single space cards (3 for each color)
    for color in colors:
        deck.extend([(color, 1)] * 3)

    # Double space cards (3 for each color)
    for color in colors:
        deck.extend([(color, 2)] * 3)

    # Sweet treat cards (one for each sweet treat)
    for treat in sweet_treats.keys():
        deck.append(('Pink', treat))

    # Shuffle the deck
    random.shuffle(deck)
    return deck, []

def draw_card(deck, played_cards):
    """Draws a card from the deck, reshuffling if necessary."""
    if not deck:
        deck, played_cards = reshuffle_deck(played_cards)
    
    card = deck.pop()
    played_cards.append(card)
    return card

def reshuffle_deck(played_cards):
    """Reshuffles the played cards back into the deck."""
    deck = played_cards.copy()
    played_cards.clear()
    random.shuffle(deck)
    return deck, played_cards

# ========================== Player Management ==========================

def find_players():
    """Creates player names based on user input and determines the number of computer players."""
    players = []
    total_players = int(input("How many players (2 - 4)? "))

    while total_players not in range(2, 5):
        print("Error. Invalid player amount.")
        total_players = int(input("How many players (2 - 4)? "))

    human_players = int(input("How many human players? "))
    while human_players > total_players or human_players < 1:
        print("Error. Invalid human player amount.")
        human_players = int(input("How many human players? "))

    # Collect human player names
    for i in range(human_players):
        name = input(f"Player {i+1} name? ").strip()
        while name in players:
            print("Name already chosen. Please choose another name.")
            name = input(f"Player {i+1} name? ").strip()
        players.append(name)

    # Add computer players
    for i in range(total_players - human_players):
        players.append(f"Computer {i+1}")

    return players

# ========================== Gameplay Functions ==========================

def move(player_position, card, board):
    """Moves the player based on the drawn card."""
    if card[0] == 'Pink':
        player_position = board.index(card[1]) + 1
    elif card[1] in ['Licorice1', 'Licorice2', 'Licorice3']:
        print("You drew a Licorice card! Your turn is skipped.")
    else:
        spaces = [i for i, space in enumerate(board) if space == player_position]
        for _ in range(card[1]):
            player_position = spaces[-1] if spaces else len(board)
    return player_position

def print_card(player, card):
    """Displays the card drawn and its movement instructions."""
    if card[1] == 1:
        print(f'{player} drew a single space card: Move to the next {card[0]} space.')
    elif card[1] == 2:
        print(f'{player} drew a double space card: Move to the second next {card[0]} space.')
    else:
        print(f'{player} drew a sweet treat card: Move to the {card[1]} location.')

def skip(card):
    """Checks if the drawn card is a Licorice card."""
    return card[1] in ['Licorice1', 'Licorice2', 'Licorice3']

def play_game(players, board):
    """Runs the main game loop, managing player turns and movements."""
    deck, played_cards = create_deck()
    player_positions = {player: -1 for player in players}

    while players:
        for player in players:
            print(f"{player}'s turn. Press Enter to draw a card.")
            input()

            current_position = player_positions[player]
            if current_position != -1 and board[current_position] in ['Licorice1', 'Licorice2', 'Licorice3']:
                print("You landed on a Licorice space! Your turn is skipped.")
                continue

            card = draw_card(deck, played_cards)
            print_card(player, card)

            if skip(card):
                continue

            player_positions[player] = move(player_positions[player], card, board)

            if player_positions[player] == len(board):
                print(f'Congratulations {player}, you won!')
                players.remove(player)

# ========================== Main Function ==========================

def main():
    print_title()
    choice = play_options()

    if choice == "p":
        board = create_game_board()
        window = tk.Tk()
        window.title("Candy Realm")

        players = find_players()
        play_game(players, board)

        window.mainloop()

    elif choice == 'r':
        print_rules()

    elif choice == 'q':
        print("Thanks for playing!")

    else:
        print("Error. Invalid response.")
        choice = play_options()

if __name__ == "__main__":
    main()