import random
list_of_cards_og = ["An Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
class Player:
    def __init__(self, name, starting_amount = 500):
        self.name = name
        self.starting_amount = starting_amount 
# ace function finds if the player has an ace and prompts them for value.
    def ace(self, card_list):
        secondary_string_for_cards = "Your cards are "
        preliminary_string_for_cards = "Your cards are "
        for w in range(len(card_list)):
            if w != len(card_list) - 1:
                preliminary_string_for_cards += str(card_list[w]) + ", "
            else:
                preliminary_string_for_cards += "and, " + str(card_list[w]) + "."
        print(preliminary_string_for_cards)
        for x in range(len(card_list)):
            if card_list[x] == "An Ace":
                new_card_value = input("""Congratulations one of your cards is an ace. That means it can have either a value of 1 or 11 which would you prefer? """)
                while not(new_card_value == "1" or new_card_value == "11"):
                    new_card_value = input("You did not input a 1 or an 11 please try again. ")
                else:
                    new_card_value = int(new_card_value)
                    card_list[x] = new_card_value
            elif card_list[x] == "Jack" or card_list[x] == "Queen" or card_list[x] == "King":
                print("Congratulations one of your cards is a {} that means they have a value of 10".format(card_list[x]))
                card_list[x] = 10
        
        if 1 in card_list or 11 in card_list:
            for w in range(len(card_list)):
                if w == len(card_list) - 1:
                    secondary_string_for_cards += "and, " + str(card_list[w]) + "."
                else:
                    secondary_string_for_cards += str(card_list[w]) + ", "
            print(secondary_string_for_cards)
        return card_list
    
    def sum(self, card_list):
        total = 0
        for x in card_list:
            total += x
        return total
                

    
    def game_play(self):
        x = True
        while x:
            bet = input("You have {} dollars. How much would you like to gamble (int only)? ".format(self.starting_amount))
            try:
                bet = int(bet)
            except:
                pass
            while not (type(bet) == int):
                try:
                    bet = int(bet)
                except:
                    print("You did not input an integer please try again.")
                    bet = input("How much would you like to gamble " )
            while bet > self.starting_amount:
                bet = input("Your bet ({}) is greater than the amount of money you have ({}). Pleae input a new bet amount. ".format(bet, self.starting_amount))
                try:
                    bet = int(bet)
                except:
                    break
            if type(bet) == int:
                if bet < self.starting_amount:
                    x = False
        print("Congrats your bet of {} was taken.".format(bet))

        second_card = random.choice(list_of_cards_og)
        first_card = random.choice(list_of_cards_og)
        list_of_cards = [first_card, second_card]
        list_of_cards = self.ace(list_of_cards)
        print("Your total is {} would you like another card?".format(self.sum(list_of_cards)))
        print("Remember you want to get as close to 21 as possible, if you go over you lose and forfeit your bet.")
        maint = True
        total_player_value = self.sum(list_of_cards)
        while maint:
            if total_player_value > 21:
                print ("You have gone over 21, you lose your bet.")
                maint = False
            elif total_player_value < 21:
                another = input("Would you like another card (y/n)? ")
                if another == "y":
                    list_of_cards.append(random.choice(list_of_cards_og))
                    list_of_cards = self.ace(list_of_cards)
                    total_player_value = self.sum(list_of_cards)
                    print ("New total is {}".format(total_player_value))
                elif another == "n":
                    maint = False
                else:
                    print("Improper input you must input 'y' or 'n'.")
            elif total_player_value == 21:
                print("Congratulations you have 21 aka blackjack.")
                maint = False
        return total_player_value, bet

def dealer_sum(card_list):
        total = 0
        for x in card_list:
            total += x
        return total

def dealer_converter(dealer_list):
    for x in range(len(dealer_list)):
        if dealer_list[x] == "Jack" or dealer_list[x] == "Queen" or dealer_list[x] == "King":
            dealer_list[x] = 10
        if dealer_list[x] == "An Ace":
            dealer_list[x] = 11
    return dealer_list
            
def dealer_play():
    dealer_first_card = random.choice(list_of_cards_og)
    dealer_second_card = random.choice(list_of_cards_og)
    dealer_list = [dealer_first_card, dealer_second_card]
    dealer_list = dealer_converter(dealer_list)
    dealer_total = dealer_sum(dealer_list)
    while dealer_total < 17:
        if dealer_total < 7:
            dealer_list.append(random.choice(list_of_cards_og))
            dealer_list = dealer_converter(dealer_list)
            dealer_total = dealer_sum(dealer_list)
        elif dealer_total < 11:
            for x in range(len(dealer_list)):
                if dealer_list[x] == "An Ace":
                    dealer_list[x] = 11
                    dealer_total = dealer_sum(dealer_list)
            if dealer_total < 11:
                dealer_list.append(random.choice(list_of_cards_og))
                dealer_list = dealer_converter(dealer_list)
                dealer_total = dealer_sum(dealer_list)
        else:
            dealer_list.append(random.choice(list_of_cards_og))
            dealer_list = dealer_converter(dealer_list)
            dealer_total = dealer_sum(dealer_list)
    return dealer_total


        


name_of_player = input("What is your name: ")
name_of_player = name_of_player.title()

print("""Hello {} welcome to Black Jack your default starting amount will be $500 would you 
like to start with a different amount?""".format(name_of_player))

new_amount = input("If yes what amount, if no please press enter. (please only input a positive integer if not you will recieve default value) ")
try:
    new_amount = int(new_amount)
except:
    pass

if  type(new_amount) == str:
    player1 = Player(name_of_player)
else:
    player1 = Player(name_of_player, int(new_amount))

print('Ok your starting amount is ${}'.format(player1.starting_amount))

keep_going = input("Are you ready to play (y/n)? ")


while "y" in keep_going:
    player_card_value, player_bet = player1.game_play()
    dealer_total = dealer_play()
    if player_card_value > 21:
        player1.starting_amount -= player_bet
        print("The amount of money you have left is {}".format(player1.starting_amount))
    elif dealer_total > 21:
        print ("Dealer has busted (dealer earned {}), you win {}".format(dealer_total, player_bet))
        player1.starting_amount += player_bet
        print ("Your new total is {}".format(player1.starting_amount))
    elif player_card_value < dealer_total:
        player1.starting_amount -= player_bet
        print("I'm sorry you lose this round, the dealer had {}, and you had {}.".format(dealer_total, player_card_value))
        print("You bet {} and lost, your new total is {}.".format(player_bet, player1.starting_amount))
    elif player_card_value > dealer_total:
        player1.starting_amount += player_bet
        print("Congratulations you beat the dealer. You had {} and the dealer had {}".format(player_card_value, dealer_total))
        print("You bet {} and won, your new total is {}.".format(player_bet, player1.starting_amount))
    else:
        print("Looks like there was a tie. You both had {}".format(dealer_total))
        print("Since there was a tie you total amount of money of {} has remained the same.".format(player1.starting_amount))
    if player1.starting_amount < 1:
        print("You have ran out of money. Please play again.")
        keep_going = "n"
    else:
        keep_going = input("Would you like to keep going (y/n). ")
        if keep_going != "y":
            print("Ok thanks for playing you ended the game with {} dollars.".format(player1.starting_amount))




