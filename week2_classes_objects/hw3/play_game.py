import random


class Card():
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.val = value
        
    def __str__(self):
        return self.face + " of " + self.suit + ", value: " + str(self.val)


class DeckOfCards():
    def __init__(self):
        self.deck = []
        self.suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        self.play_idx = 0
        
        for suit in self.suits:
            i = 0
            for i in range(len(self.faces)):
                self.deck.append(Card(suit, self.faces[i], self.values[i]))
                
                
    def shuffle_deck(self):
        random.shuffle(self.deck)
        self.play_idx = 0
        

    def print_deck(self, message="Deck:"):
        print(message)
        for card in self.deck:
            print(card.face, "of", card.suit, end=", ")
        print("\n---")
        
    def get_card(self):
        self.play_idx += 1
        return self.deck[self.play_idx - 1]
         #adjusts for aces 
def adjust_for_aces(score, ace_count):
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
    return score

    while score > 21 and aces > 0:
        score -= 10
        aces -= 1 
    
    return score 

#starts the game 
def play_game():
    # Creates a new deck
    deck = DeckOfCards()
    deck.print_deck("Deck before shuffled:")

    # Shuffles deck 
    deck.shuffle_deck()
    deck.print_deck("Deck after shuffled:")

    # Draws two cards for player
    card1 = deck.get_card()
    card2 = deck.get_card()
    print("Card number 1 is:", card1)
    print("Card number 2 is:", card2)

    # Draws two dealer cards 
    dealercard1 = deck.get_card()
    dealercard2 = deck.get_card()

    # Calculates initial player total
    totalscore = card1.val + card2.val
    ace_count = sum(1 for card in [card1, card2] if card.face == "Ace")
    totalscore = adjust_for_aces(totalscore, ace_count)
    print("Your total score is:", totalscore)

    # Ask if they want a hit and continues accordingly 
    def hit_prompt(totalscore, ace_count):
        while True:
            answer = input("Do you want a hit? (yes/no): ").lower()
            if answer == "yes":
                new_card = deck.get_card()
                print("Card drawn is:", new_card)
                totalscore += new_card.val
                if new_card.face == "Ace":
                    ace_count += 1
                totalscore = adjust_for_aces(totalscore, ace_count)
                print("Your new total score is:", totalscore)

                if totalscore > 21:
                    print("Unlike Phineas and Ferb, you have been BUSTED. You lose!")
                    return totalscore  # Player loses
            elif answer == "no":
                return totalscore
            else:
                print("Please enter 'yes' or 'no'.")

    totalscore = hit_prompt(totalscore, ace_count)

    if totalscore > 21:
        return  # Player busts, game over

    # Dealer's turn uses dealer logic 
    print("\nDealer's cards are", dealercard1, "and", dealercard2)
    dealer_score = dealercard1.val + dealercard2.val
    dealer_ace_count = sum(1 for card in [dealercard1, dealercard2] if card.face == "Ace")
    dealer_score = adjust_for_aces(dealer_score, dealer_ace_count)
    print("Dealer's total score is:", dealer_score)

    while dealer_score < 17:
        new_card = deck.get_card()
        print("Dealer draws:", new_card)
        dealer_score += new_card.val
        if new_card.face == "Ace":
            dealer_ace_count += 1
        dealer_score = adjust_for_aces(dealer_score, dealer_ace_count)

    print("Dealer's final score is:", dealer_score)

    # Determine winner
    if dealer_score > 21:
        print("The dealer has fallen down to the pits of bustedness, and you stand victorious over the cliff edge")
    elif dealer_score > totalscore:
        print("The dealer laughs down over your broken body, for you have lost this conquest!")
    elif dealer_score < totalscore:
        print("You are the mightiest of all and have won this most intense battle of wills")
    else:
        print("Till the death, you must face off again, for this round was a tie")

#asks player if they want to play another game 
def another_game():
    while True:
        answer2 = input("Would you like to play another game? (yes/no): ").lower()
        if answer2 == "yes":
            return True
        elif answer2 == "no":
            print("Lame, guess we'll meet next time you set out on a daring quest")
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def main():
    print("Come play Black Jack if you dare!")
    while True: 
        play_game()
        if not another_game():
            break


main()