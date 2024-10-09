import random, time

print("Hello, welcome to the casino!")

picker = input("What game would you like to play? ")

if picker == "blackjack":
    # Function to deal a card
    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)

    # Function to calculate the score
    def calculate_score(hand):
        if sum(hand) == 21 and len(hand) == 2:
            return 0
        if 11 in hand and sum(hand) > 21:
            hand.remove(11)
            hand.append(1)
        return sum(hand)

    # Function to play the game
    def play_game():
        player_hand = []
        computer_hand = []

        for _ in range(2):
            player_hand.append(deal_card())
            computer_hand.append(deal_card())

        game_over = False

        while not game_over:
            player_score = calculate_score(player_hand)
            computer_score = calculate_score(computer_hand)

            print(f"Your cards: {player_hand}, current score: {player_score}")
            print(f"Computer's first card: {computer_hand[0]}")

            if player_score == 0 or computer_score == 0 or player_score > 21:
                game_over = True
            else:
                should_continue = input("Type 'y' to get another card, 'n' to pass: ")
                if should_continue == 'y':
                    player_hand.append(deal_card())
                else:
                    game_over = True

        while computer_score != 0 and computer_score < 17:
            computer_hand.append(deal_card())
            computer_score = calculate_score(computer_hand)

        print(f"Your final hand: {player_hand}, final score: {player_score}")
        print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

        if player_score > 21:
            return "You went over. You lose!"
        elif computer_score > 21:
            return "Computer went over. You win!"
        elif player_score == computer_score:
            return "It's a draw!"
        elif player_score == 0:
            return "Blackjack! You win!"
        elif computer_score == 0:
            return "Computer got a Blackjack. You lose!"
        elif player_score > computer_score:
            return "You win!"
        else:
            return "You lose!"

    print(play_game())  # Call the play_game function

if picker == "slot":
    import random

# Define the slot machine symbols
symbols = ['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Bar', 'Seven']

# Define the slot machine reels
reels = 3

# Define the player's balance
balance = 100

# Function to spin the reels
def spin_reels():
    return [random.choice(symbols) for _ in range(reels)]

# Function to check for wins
def check_wins(reels):
    if reels[0] == reels[1] == reels[2]:
        if reels[0] == 'Seven':
            return 100
        elif reels[0] == 'Bar':
            return 50
        else:
            return 10
    elif reels[0] == reels[1] or reels[0] == reels[2] or reels[1] == reels[2]:
        return 5
    else:
        return 0

# Main game loop
while True:
    print(f"Balance: ${balance}")
    bet = input("Enter your bet (or 'q' to quit): ")
    if bet.lower() == 'q':
        break
    try:
        bet = int(bet)
        if bet > balance:
            print("Insufficient balance!")
            continue
        if bet <= 0:
            print("Invalid bet!")
            continue
    except ValueError:
        print("Invalid input!")
        continue

    reels = spin_reels()
    print(f"You spun: {reels[0]} | {reels[1]} | {reels[2]}")
    win = check_wins(reels)
    if win > 0:
        print(f"You won ${win}!")
        balance += win
    else:
        print("Better luck next time!")
        balance -= bet

if picker == "roulett":
    import random

# Define the Roulette wheel
wheel = list(range(1, 37)) + [0]

# Define the player's balance
balance = 100

# Function to place a bet
def place_bet():
    while True:
        bet_amount = input("Enter your bet amount (or 'q' to quit): ")
        if bet_amount.lower() == 'q':
            return 0, None
        try:
            bet_amount = int(bet_amount)
            if bet_amount > balance:
                print("Insufficient balance!")
                continue
            if bet_amount <= 0:
                print("Invalid bet!")
                continue
            break
        except ValueError:
            print("Invalid input!")
            continue

    while True:
        bet_type = input("Enter your bet type (odd/even, red/black, or a number): ")
        if bet_type.lower() in ['odd', 'even', 'red', 'black']:
            break
        elif bet_type.isdigit() and 0 <= int(bet_type) <= 36:
            bet_type = int(bet_type)
            break
        else:
            print("Invalid bet type!")

    return bet_amount, bet_type

# Function to spin the wheel
def spin_wheel():
    return random.choice(wheel)

# Function to check for wins
def check_wins(bet_type, winning_number):
    if bet_type in ['odd', 'even']:
        if bet_type == 'odd' and winning_number % 2 != 0:
            return True
        elif bet_type == 'even' and winning_number % 2 == 0:
            return True
        else:
            return False
    elif bet_type in ['red', 'black']:
        if bet_type == 'red' and (winning_number in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]):
            return True
        elif bet_type == 'black' and (winning_number in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]):
            return True
        else:
            return False
    else:
        if bet_type == winning_number:
            return True
        else:
            return False

# Main game loop
while True:
    print(f"Balance: ${balance}")
    bet_amount, bet_type = place_bet()
    if bet_amount == 0:
        break

    winning_number = spin_wheel()
    print(f"The winning number is: {winning_number}")

    if check_wins(bet_type, winning_number):
        if bet_type in ['odd', 'even', 'red', 'black']:
            payout = bet_amount * 2
        else:
            payout = bet_amount * 36
        print(f"You won ${payout}!")
        balance += payout
    else:
        print("Better luck next time!")
        balance -= bet_amount