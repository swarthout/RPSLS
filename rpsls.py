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
validpicks = ['rock','paper','scissors','lizard','spock']
#This is the class where the hand and the win status are stored 
#
class player():
    win = False
    hand = ""
    win_count = 0
    lose_count = 0
    tie_count = 0
    total_games = 0
    win_percentage = 0.00
    history = []
    def getpercentage(self):
        self.total_games = self.win_count+self.lose_count+self.tie_count
        if self.total_games !=0:
            self.win_percentage  = (self.win_count/(self.total_games))*100
        else:
            self.win_percentage = 0.00
    def makechoice(self,choice):
        self.hand = choice
    def youwin(self):
        self.win = True
        self.win_count +=1
    def youlose(self):
        self.win = False
        self.lose_count +=1
    def youtie(self):
        self.win = False
        self.tie_count+=1
    def reset(self):
        
        self.hand = ""
        self.win = False
    def showrecord(self):
        print("Your record: %d-%d-%d \nWin Percentage: %.2f"%(self.win_count,self.lose_count,self.tie_count,self.win_percentage))
human = player()
computer = player()

difficulty = input("Welcome to RSPLS! Do you want to play against: \n\n1.) A random guesser\n2.) A mildly intelligent AI\nEnter 1 or 2: ")
while difficulty != '1' and difficulty != '2':
    difficulty= input("Not a valid input! Enter difficulty level (1 or 2): ")

def gameloop():
    
    def most_common(lst):
        max = 0
        maxitemlist = []
        for x in set(lst):
            count =  lst.count(x)
            if count >= max:
                max = count
                maxitemlist.append(x)
        return maxitemlist
    favoritepicks = most_common(human.history)
    counterpicks = []
    for favorite in favoritepicks:
        for rule in rules:
            if rule[2] == favorite:
                counterpicks.append(rule[0])
    
    randompick = validpicks[random.randrange(len(validpicks))] #This will return either RPSLS
    if len(counterpicks)!=0:
        learnedpick = counterpicks[random.randrange(len(counterpicks))]
    else:
        learnedpick = randompick
    
    
    
    if difficulty == "1":
        computer.makechoice(randompick)
    if difficulty == "2":
        computer.makechoice(learnedpick)
            
    while human.hand == "": #This will loop until the player puts in a valid input
        humanpick = input("3,2,1... Rock! Paper! Scissors! Lizard! Spock! Pick one: ").lower()
        if humanpick in validpicks:
            human.makechoice(humanpick)
            human.history.append(humanpick)
    	
    
        else:
            print('Not a valid input! Try again...')
                        
	 

    print("You picked: %s \nComputer picked: %s" %(human.hand,computer.hand))

    if human.hand == computer.hand:
        print("You tie!")
        human.youtie()
        computer.youtie()
    else:
        def findwinner(player1,player2):
            for x in range(len(rules)):
                if rules[x][0] == player1.hand and rules[x][2] == player2.hand:
                    player1.youwin()
                    player2.youlose()
                    return 0
            player2.youwin()
            player1.youlose()
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
    human.getpercentage()
    human.showrecord()
    human.reset()
    computer.reset()
    
    
    playagain = input("Do you want to play again? (Y/N): ").lower()
    

    if playagain == 'y':
        
        gameloop()
    else:
        print(("Games Played: %d "%human.total_games))
        human.showrecord()
        print("Goodbye!\n")
        quit()
gameloop()

