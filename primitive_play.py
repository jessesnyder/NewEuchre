from random import shuffle as shuffle, randint as randint

# I think it's more straightforward, for the purposes of finding the winner
# and possibly for bidding, to use numerical values in place of rank name.

card_values = [9,10,11,12,13,14]

#When it's time to display, this dictionary can be used to get rank names.

card_values_and_ranks = {9:"9",10:"10",11:"jack",12:"queen",13:"king",14:"ace"}
suits = ["clubs","diamonds","spades","hearts"]

def create_deck():
    deck = []
    for suit in suits: 
        for value in card_values:
            card = {"suit": suit, "value": value}
            deck.append(card)
    local_deck = deck[:]
    shuffle(local_deck)
    return local_deck

class Player():
    def __init__(self, id):
        self.id = id
        self.hand = []
    def get_hand(self,current_deck):
        hand = current_deck[0:5]
        del current_deck[0:5]
        self.hand = hand
    def play(self):
        return {"id":self.id,"card":self.hand.pop()}

def create_players(current_deck):
    local_players = []
    for i in range (4):
        new_player = Player(i)
        new_player.get_hand(current_deck)
        local_players.append(new_player)
    return local_players

def find_high_card(trick):
    count = 0
    for play in trick:
        if count == 0:
            (winner, lead_suit, winning_value) = play["id"], play["card"]["suit"],play["card"]["value"]
        else:
            if (play["card"]["suit"] == lead_suit and play["card"]["value"]
                > winning_value):
                    winner = play["id"]
                    winning_value = play["card"]["value"]
        count += 1
    return winner

def play_game():
    current_deck = create_deck()
    players = create_players(current_deck)
    trick = []
    for player in players:
        trick.append(player.play()) # list of dictionaries with player and played card
    winner = find_high_card(trick)
    return winner, trick

games = int(input("How many games?"))

while games:
    winner, trick = play_game()
    for play in trick:
        print("Player " + str(play["id"]) + "/'s played card: " + str(play["card"]["value"]) + " of " + play["card"]["suit"])
        
    print("Player " + str(winner) + " is the winner.")
    games -= 1