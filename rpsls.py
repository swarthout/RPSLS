import random
#These are the rules of the game. I use this as a database of possible options and a way of determining who wins.
#
rules = [['paper','covers','rock'],
         ['paper','disproves','spock'],
         ['scissors','cuts', 'paper'],
         ['scissors','decapitates','lizard'],
         ['spock','smashes','scissors'],
         ['spock','vaporizes','rock'],
         ['lizard','eats','paper'],
         ['lizard','poisions','spock'],
         ['rock','crushes','lizard'],
         ['rock','crushes','scissors']]
#This is the class where the hand and the win status are stored 
#
class player():
    win = False
    
    def makechoice(self,choice):
        self.hand = choice
    def youwin(self):
        self.win = True
    
human = player()
computer = player()

def gameloop():

    aipick = rules[random.randrange(0,10,2)][0] #This will return either RPSLS

    computer.makechoice(aipick) 

    human.makechoice(input("3,2,1... Rock! Paper! Scissors! Lizard! Spock! Pick one: ").lower())



    print("You picked: %s \nComputer picked: %s" %(human.hand,computer.hand))

    if human.hand == computer.hand:
        print("You tie!")
    else:
        def findwinner(player1,player2):
            for x in range(len(rules)):
                if rules[x][0] == player1.hand and rules[x][2] == player2.hand:
                    player1.youwin()
                    return 0
            player2.youwin()
            return 0
        findwinner(human,computer)

        if human.win:
            for x in range(len(rules)):
                if rules[x][0] == human.hand and rules[x][2] == computer.hand:
                    print(" ".join(rules[x]))
            print("You win!")
        if computer.win:
            for x in range(len(rules)):
                if rules[x][2] == human.hand and rules[x][0] == computer.hand:
                    print(" ".join(rules[x]))
            print("You lose!")
    playagain = input("Do you want to play again? (Y/N): ").lower()

    if playagain == 'y':
        gameloop()
gameloop()





