import random

# ─────────────────────────────────────────
#  STEP 1: Card & Deck Setup
# ─────────────────────────────────────────
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {
    'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,
    'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
    'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11
}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.deck = [Card(s, r) for s in suits for r in ranks]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

    def __str__(self):
        return f"Deck of {len(self.deck)} cards"


# ─────────────────────────────────────────
#  STEP 2: Hand (with Ace adjustment)
# ─────────────────────────────────────────
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# ─────────────────────────────────────────
#  STEP 3: Chips / Betting
# ─────────────────────────────────────────
class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# ─────────────────────────────────────────
#  STEP 4: Game Logic Functions
# ─────────────────────────────────────────
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input(f"\n💰 Chips available: {chips.total}. Place your bet: "))
            if chips.bet > chips.total:
                print("⚠️  Bet exceeds available chips! Try again.")
            elif chips.bet <= 0:
                print("⚠️  Bet must be greater than zero.")
            else:
                break
        except ValueError:
            print("⚠️  Please enter a valid number.")


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    """Returns True if player hits, False if player stands."""
    while True:
        choice = input("\n➡️  Hit or Stand? (h/s): ").strip().lower()
        if choice == 'h':
            hit(deck, hand)
            return True
        elif choice == 's':
            print("🖐️  Player stands. Dealer's turn.")
            return False
        else:
            print("⚠️  Invalid input. Enter 'h' to hit or 's' to stand.")


def show_cards(player, dealer, hide_dealer=True):
    print("\n" + "═" * 35)
    print("🂠  DEALER'S HAND")
    print("─" * 35)
    if hide_dealer:
        print("  [ Hidden Card ]")
        print(f"  {dealer.cards[-1]}")
    else:
        for card in dealer.cards:
            print(f"  {card}")
        print(f"  ▶ Dealer Total: {dealer.value}")

    print("\n🃏  PLAYER'S HAND")
    print("─" * 35)
    for card in player.cards:
        print(f"  {card}")
    print(f"  ▶ Player Total: {player.value}")
    print("═" * 35)


def check_bust(hand):
    return hand.value > 21


def check_winner(player, dealer, chips):
    print("\n" + "═" * 35)
    if dealer.value > 21:
        print("🎉  Dealer BUSTS! You WIN!")
        chips.win_bet()
    elif dealer.value > player.value:
        print("😞  Dealer wins. Better luck next time!")
        chips.lose_bet()
    elif dealer.value < player.value:
        print("🎉  Player WINS! Nicely done!")
        chips.win_bet()
    else:
        print("🤝  It's a TIE! Your bet is returned.")
    print(f"\n💰  Your chips: {chips.total}")
    print("═" * 35)


# ─────────────────────────────────────────
#  STEP 5: Main Game Loop
# ─────────────────────────────────────────
def play_blackjack():
    print("=" * 35)
    print("   🃏  WELCOME TO BLACKJACK!  🃏")
    print("=" * 35)

    chips = Chips(total=100)
    playing = True

    while True:
        if chips.total <= 0:
            print("\n💸 You're out of chips! Game over.")
            break

        # Setup round
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        dealer_hand = Hand()

        # Deal initial 2 cards each
        for _ in range(2):
            player_hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())

        # Take bet
        take_bet(chips)

        # Show initial cards
        show_cards(player_hand, dealer_hand, hide_dealer=True)

        # Check for player blackjack
        if player_hand.value == 21:
            print("\n🎰  BLACKJACK! Instant win!")
            chips.win_bet()
            print(f"💰  Your chips: {chips.total}")
        else:
            # Player's turn
            while playing:
                still_going = hit_or_stand(deck, player_hand)
                show_cards(player_hand, dealer_hand, hide_dealer=True)

                if check_bust(player_hand):
                    print("\n💥  Player BUSTS!")
                    chips.lose_bet()
                    print(f"💰  Your chips: {chips.total}")
                    break

                if not still_going:
                    # Dealer's turn
                    while dealer_hand.value < 17:
                        hit(deck, dealer_hand)

                    show_cards(player_hand, dealer_hand, hide_dealer=False)

                    if check_bust(dealer_hand):
                        print("\n💥  Dealer BUSTS!")
                        chips.win_bet()
                        print(f"💰  Your chips: {chips.total}")
                    else:
                        check_winner(player_hand, dealer_hand, chips)
                    break

        # Play again?
        again = input("\n🔄  Play again? (y/n): ").strip().lower()
        if again != 'y':
            print(f"\n👋  Thanks for playing! You finished with {chips.total} chips.")
            break


if __name__ == "__main__":
    play_blackjack()
