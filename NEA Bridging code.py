import itertools
import random
import os

#GLOBAL VARIABLES

player_1_cards = [] # empty list is created
player_2_cards = []

class Menu(object):
    logins = []
    
    def __init__(self, player_number):

        self.player_number = player_number # initialises variables
        self.login_attempts = 0 

    def question(self):
        
        attempts= 0

        while attempts < 3: # runs loop up to 3  times
            choice = input("Enter 1 for register \nEnter 2 for login")
           
            if choice == "1":
                self.register()
                break   # breaks out of loop
                
            elif choice == "2":
                self.login()
                break   # breaks out of loop
              
            else:
                print("invalid choice")
                attempts += 1   # adds another attempt if invalid input

    def register(self):

        register_username = input("Enter your username")
        register_password = input("Enter your password")
        if register_username + ".txt" not in os.listdir():
            
            with open (register_username + ".txt","w") as file:

                file.write(register_username + "\n")    # opens file in write mode and stores a username
                file.write(register_password + "\n")    # and password on different lines

            self.question()

        else:
            print("Username is already in use. Pick a different username")
            self.register()

    def login(self):

        login_username = input("Enter your username")
        login_password = input("Enter your password")

        self.login_authentication(login_username,login_password)

    def login_authentication(self,username,password):



        if username + ".txt" in os.listdir():    # checking if username exists

            
# opens file in read mode and closes it after instructions are executed
            with open(username + ".txt","r") as file:
                                                       # makes a variable called file
                user_details = file.read().splitlines()  # creates a list where each line is an element in a list

            if password == user_details[1]: # comparing the passwords
                if username not in Menu.logins:
                    print("correct details")
                    Menu.logins.append(username)    # checks if player has logged in before

                    if self.player_number == 1: # checks if player 2 has not logged in yet

                        player_2.question()

                else:
                    print("user is already logged in")

                        

            else:

                print("incorrect username and password")    # incorrect password or username
                self.login_attempts +=1     # adds another input
                if self.login_attempts < 3: # allows up to 3 attempts
                    self.login()

        else:
            print("incorrect username and password")    # either incorrect username or both details are incorrect
            self.login_attempts +=1
            if self.login_attempts < 3:
                self.login()

def get_deck_of_cards():
    total = 30
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    colours = ['red', 'black', 'yellow']
    deck = list(itertools.product(numbers, colours))   # combines the colours and numbers into a tuple in the list
    random.shuffle(deck)    # shuffles deck

    # unpacks the tuple and combines the colour and number together with an '_' between it
    deck = [card_colour + "_" + card_number for card_number,
            card_colour in deck]   
    return deck


class Game(object):
    cards = get_deck_of_cards()
    played_cards = []
    rounds = 0

    def __init__(self, player_number):
        self.player_number = player_number

    def main(self):
        while Game.rounds < 30:     # loops through 30 times (30 cards)
            # asks a user to select a card by clicking enter
            input("\nPlayer {}: Select Card".format(self.player_number))

# removes first index of the list and stores in a variable called picked_card.
# this variable is equal to the 1st element of the list called cards and the first element is removed from that list
            picked_card = Game.cards.pop(0) 
            Game.played_cards.append(picked_card)               
            Game.rounds += 1

            if self.player_number == 1:
                player_2_game.main()
            else:   # everytime a card is chosen, it is stored 
                print("\n" + check_round_winner(Game.played_cards[Game.rounds - 2], Game.played_cards[Game.rounds - 1]))
                player_1_game.main()    # prints players' cards

        

    @staticmethod   # this function does not use the self parameter (__init__ function)
    def check_winner():
        if len(player_1_cards) > len(player_2_cards):   #calculates overall winner
            winner = "player 1"
            winner_cards = player_1_cards
        else:
            winner = "player 2"
            winner_cards = player_2_cards


        print("\n{} wins!!!".format(winner.title()))
        print("{}'s cards:".format(winner.title()))
        print(*list("<" + card +">" for card in winner_cards))  # for design
        
        with open("winner.txt","w")as file: # opens file in write mode and stores winners details
            file.write(winner + "\n")
            for card in winner_cards:
                file.write(card + "\n")

            file.write("number of cards: " + str(len(winner_cards)))

        add_highscore(Menu.logins[0],player_1_cards, 1) # calls function for player 1
        add_highscore(Menu.logins[1],player_2_cards, 2) # calls function for player 2

def check_round_winner(picked_card_1, picked_card_2):
    def add_cards(winner_cards):    # adds both players' card to the winner
        winner_cards.append(picked_card_1)
        winner_cards.append(picked_card_2)
        
    colours = ['red', 'yellow', 'black']
    splitted_card_1 = picked_card_1.split("_")
    splitted_card_2 = picked_card_2.split("_")
    message = "Player 1 card: " + picked_card_1 + "\n" + "Player 2 card: " + picked_card_2 + "\n"

    if splitted_card_1[0] == splitted_card_2[0]:    # checks if both players' colours are the same
        if int(splitted_card_1[1]) > int(splitted_card_2[1]):   # checks if player 1's card number is higher
            message += "Player 1 wins this round"
            add_cards(player_1_cards)
        elif int(splitted_card_2[1]) > int(splitted_card_1[1]): # checks if player 2's card number is higher
            message += "Player 2 wins this round"
            add_cards(player_2_cards)

    # checks if player1's colour beats player 2's colour
    elif splitted_card_1[0] == colours[(colours.index(splitted_card_2[0])+1)%len(colours)]:
        message+= "Player 1 wins this round"
        add_cards(player_1_cards)

    # checks if player2's colour beats player 1's colour
    elif splitted_card_2[0] == colours[(colours.index(splitted_card_1[0])+1)%len(colours)]:
        message+= "Player 2 wins this round"
        add_cards(player_2_cards)
    
    
    return message

def add_highscore(player_name,player_cards,player_number):

    with open ("top_scores.txt")as file:
        top_scores = file.read().splitlines()   # each variable is a list and each element is a line in the files
        
    with open ("top_players.txt")as file:
        top_players = file.read().splitlines()  
        
    with open ("top_cards.txt")as file:
        top_cards = file.read().splitlines()

    if len(player_cards) > int(top_scores[0]):
        
        del top_scores[0]  #deletes the lowest highscore
        del top_players[0] # deletes player with lowest amount of cards
        del top_cards[0] # deletes player's lowest amount of cards
        # converts each element in the list to an integer from a string
        top_scores = [int(x) for x in top_scores]   
        top_scores.append(len(player_cards))    # adds a new high score to the list 
        top_scores = sorted(top_scores) # sorts the highscores in ascending order
        index = top_scores.index(len(player_cards)) # finds the position of the player on the high scores list
        
        top_players.insert(index, player_name)  # inserts player's name into the high score list(1st, 2nd, 3rd)
        top_cards.insert(index, player_cards)

        with open("top_scores.txt", "w") as file:
            for score in top_scores:                # opens file in write mode and adds the top 5 scores
                file.write(str(score) + "\n")

        with open("top_players.txt", "w") as file:
            for player in top_players:              # opens file in write mode and adds the top 5 scores
                file.write(player + "\n")

        with open("top_cards.txt", "w") as file:
            for card in top_cards:                  # opens file in write mode and adds the top 5 scores
                file.write(str(card) + "\n")

    if player_number == 2:
        # calls  a function after both players high scores have been added to the list         
        display(top_scores, top_players, top_cards) 

def display(top_scores, top_players, top_cards):

    # removes speech marks and brackets when storing  in the vraiable
    top_cards = [i.replace("", "") for i in top_cards] 
    top_cards = [str(i)[1:-1] for i in top_cards]   # removes square brackets from the lists 
    for i in range(5):  # prints the top 5 players with their cards and score
        # prints out player's username, score and cards        
        print("\nUsername: {:15} Score: {:5} Cards: {:5}".format(top_players[4 - i], top_scores[4 - i], top_cards[4 - i]))  

if "__main__" == __name__:  # doesnt allow the program to be run from another file
    player_1 = Menu(1)
    player_2 = Menu(2)
    player_1.question()

    if len(Menu.logins) == 2:   # checks that both players have loggee in successfully
    
        player_1_game = Game(1)
        player_2_game = Game(2)
        player_1_game.main()
        Game.check_winner()
    
