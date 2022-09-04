import random

# Card deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Dealer and Player hand
dealer_hand = []
player_hand = []

isDrawing = True
dealerIsDrawing = True


def draw_card(hand):
    card = random.choice(cards)
    # Convert Ace to 1 if it causes a bust
    if card == 11:
        if card + sum(hand) > 21:
            card = 1
    hand.append(card)


def check_for_blackjack(points):
    if points == 21:
        return True


def check_for_bust(points):
    if points > 21:
        return True


def decide_winner(dealer_points, player_points):
    if player_points > dealer_points:
        print("Player wins")
    elif dealer_points > player_points:
        print("Dealer wins")
    else:
        print("It is a tie")


# Dealer and Player initial draw
for i in range(2):
    draw_card(dealer_hand)
    draw_card(player_hand)

print(f"Dealer has a hand of: {dealer_hand}, total: {sum(dealer_hand)}")
print(f"Player has a hand of: {player_hand}, total: {sum(player_hand)}")

# Check for Blackjack
if check_for_blackjack(sum(player_hand)) and check_for_blackjack(sum(dealer_hand)):
    isDrawing = False
    print("Both the dealer and player have blackjack...HOW?!")
elif check_for_blackjack(sum(player_hand)):
    isDrawing = False
    print("Player has blackjack!")
elif check_for_blackjack(sum(dealer_hand)):
    isDrawing = False
    print("Dealer has blackjack!")


# Ask player if they want to draw
while isDrawing:
    player_draw = input("Would you like to draw? Type 'y' for Yes or 'n' for No: ").lower()
    if player_draw == 'y':
        draw_card(player_hand)
        print(player_hand)
        print(sum(player_hand))
        # Check for player Blackjack when drawing
        if check_for_blackjack(sum(player_hand)):
            isDrawing = False
            print("Player has blackjack!")
        # Check if player bust
        elif check_for_bust(sum(player_hand)):
            isDrawing = False
            print("Player bust.")
    else:
        isDrawing = False
        # Check if dealer has score > 16

        while dealerIsDrawing:
            if sum(dealer_hand) < 16:
                draw_card(dealer_hand)
                if check_for_bust(sum(dealer_hand)):
                    dealerIsDrawing = False
                    print(f"Dealer has a hand of: {dealer_hand}, total: {sum(dealer_hand)}")
                    print("Dealer bust.")
                if check_for_blackjack(sum(dealer_hand)):
                    dealerIsDrawing = False
                    print(f"Dealer has a hand of: {dealer_hand}, total: {sum(dealer_hand)}")
                    print("Dealer has blackjack!")
            else:
                dealerIsDrawing = False
                print(f"Dealer has a hand of: {dealer_hand}, total: {sum(dealer_hand)}")
                print(f"Player has a hand of: {player_hand}, total: {sum(player_hand)}")
                decide_winner(sum(dealer_hand), sum(player_hand))


# Key tools
# While loop
# Function with outputs (returns)
