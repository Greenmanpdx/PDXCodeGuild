import random

class Cards:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '{} of {}s'.format(self.rank, self.suit)

class Deck:
    cards = {
        1:Cards('heart', 'ace'),
        2:Cards('heart', 'two'),
        3:Cards('heart', 'three'),
        4:Cards('heart', 'four'),
        5:Cards('heart', 'five'),
        6:Cards('heart', 'six'),
        7:Cards('heart', 'seven'),
        8:Cards('heart', 'eight'),
        9:Cards('heart', 'nine'),
        10:Cards('heart', 'ten'),
        11:Cards('heart', 'jack'),
        12:Cards('heart', 'queen'),
        13:Cards('heart', 'king'),
        14:Cards('diamond', 'ace'),
        15:Cards('diamond', 'two'),
        16:Cards('diamond', 'three'),
        17:Cards('diamond', 'four'),
        18:Cards('diamond', 'five'),
        19:Cards('diamond', 'six'),
        20:Cards('diamond', 'seven'),
        21:Cards('diamond', 'eight'),
        22:Cards('diamond', 'nine'),
        23:Cards('diamond', 'ten'),
        24:Cards('diamond', 'jack'),
        25:Cards('diamond', 'queen'),
        26:Cards('diamond', 'king'),
        27:Cards('spade', 'ace'),
        28:Cards('spade', 'two'),
        29:Cards('spade', 'three'),
        30:Cards('spade', 'four'),
        31:Cards('spade', 'five'),
        32:Cards('spade', 'six'),
        33:Cards('spade', 'seven'),
        34:Cards('spade', 'eight'),
        35:Cards('spade', 'nine'),
        36:Cards('spade', 'ten'),
        37:Cards('spade', 'jack'),
        38:Cards('spade', 'queen'),
        39:Cards('spade', 'king'),
        40:Cards('club', 'ace'),
        41:Cards('club', 'two'),
        42:Cards('club', 'three'),
        43:Cards('club', 'four'),
        44:Cards('club', 'five'),
        45:Cards('club', 'six'),
        46:Cards('club', 'seven'),
        47:Cards('club', 'eight'),
        48:Cards('club', 'nine'),
        49:Cards('club', 'ten'),
        50:Cards('club', 'jack'),
        51:Cards('club', 'king'),
        52:Cards('club', 'queen')
    }

    def __init__(self):
        self.deck_list = [x for x in range(1, 53)]

    def shuffle(self):
        random.shuffle(self.deck_list)

    def cut(self):
        place_to_cut = random.randrange(1, 52)
        bottom = self.deck_list[1:place_to_cut]
        top = self.deck_list[place_to_cut+1:]
        self.deck_list =  top + bottom

    def draw_card(self):
        card = self.deck_list.pop(0)
        return self.cards[card]





class Hand:

    def __init__(self, card1):
        self.in_hand = [card1]

    def add_card(self, card):
        self.in_hand.append(card)
    def display_hand(self):
        for card in self.in_hand:
            print(card)

    def dealer_display(self):
        print(self.in_hand[0])

class Game:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.deck.cut()

    def start_game(self):
        players = {
            }
        num_players = int(input('Enter the amount of players \n'))
        # first_draw = [self.deck.draw_card() for card in range(1, num_players+1)]
        for i in range(1, num_players+1):
            players[i] = Hand(self.deck.draw_card())
        players[0] = Hand(self.deck.draw_card())
        for i in range(1, num_players+1):
            players[i].in_hand.append(self.deck.draw_card())
        players[0].in_hand.append(self.deck.draw_card())

        print('Dealer')
        players[0].dealer_display()
        # score = self.score_hand(players[0])
        # print('score: {} \n'.format(score))

        for i in range(1, num_players +1):
            print('Player ' + str(i))
            players[i].display_hand()
            score = self.score_hand(players[i])
            print('score: ' + str(score))

        return players


    def score_hand(self, hand):
        score = 0
        num_aces = 0
        for card in hand.in_hand:
            if card.rank == 'two':
                score += 2
            if card.rank == 'three':
                score += 3
            if card.rank == 'four':
                score += 4
            if card.rank == 'five':
                score += 5
            if card.rank == 'six':
                score += 6
            if card.rank == 'seven':
                score += 7
            if card.rank == 'eight':
                score += 8
            if card.rank == 'nine':
                score += 9
            if card.rank == 'ten':
                score += 10
            if card.rank == 'jack':
                score += 10
            if card.rank == 'queen':
                score += 10
            if card.rank == 'king':
                score += 10
            if card.rank == 'Ace':
                num_aces += 1

        if num_aces > 0:
            if num_aces == 1:
                if score < 11:
                    score += 11
                else:
                    score += 1
            if num_aces == 2 :
                if score < 10:
                    score += 12
                else:
                    score += 2
            if num_aces == 3:
                if score < 9:
                    score += 13
                else:
                    score += 3
            if num_aces == 4:
                if score < 8:
                    score += 14
                else:
                    score += 4
        return score







