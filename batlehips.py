import random
import time
import os

def GetNumberFromUser(message, errormessage):
    ValidInputGiven = False
    while ValidInputGiven == False:
        stringInput = input(message)
        if stringInput.isdigit() == False:
            print(errormessage)
        else:
            ValidInputGiven = True
    integer = int(stringInput)
    return integer

def MainMenu():
    #draw the main menu for the game and return the user choice
    acceptableMenuChoices = ["E", "H", "I", "C", "O", "Q"]
    theChoice = ""
    while(theChoice not in acceptableMenuChoices):
    
        print('''

    *********************************
    **       Batlehips menyu       **
    **                             **
    *********************************
    **                             **
    **    E - Easy mode            **
    **    H - Hard mode            **
    **    I - Impossible mode      **
    **    C - Custom mode          **
    **    O - Options              **
    **                             **
    **    Q - Quit                 **
    **                             **
    **   (c) 42 AD rozzer thing    **
    *********************************
        ''')
    
        theChoice = input("Choose ur thing idk: ").upper()
    
    return theChoice

def OptionsMenu():
    acceptableMenuChoices = ["T", "S", "I", "B"]
    theChoice = ""
    while(theChoice not in acceptableMenuChoices):
    
        print('''

    *********************************
    **       Opchions menyu        **
    **                             **
    *********************************
    **                             **
    **    T - RTX ON/OFF           **
    **    S - Sound ON/OFF         **
    **    I - Custom imports       **
    **                             **
    **    B - Back                 **
    **                             **
    **                             **
    **                             **
    **   (c) 42 AD rozzer thing    **
    *********************************
        ''')
    
        theChoice = input("Choose ur option thing idk: ").upper()
    
    return theChoice


time.sleep(0.5)
os.system('cls')
time.sleep(0.5)

# kinda prints a loading screen for some reason
TimeCounter = 0
for Waiting in range(20):
    print("Loading")
    print("")
    print("∎" * TimeCounter)
    time.sleep(random.random())
    os.system('cls')
    TimeCounter += 1

time.sleep(0.5)
os.system('cls')
time.sleep(0.5)



# making it so the game can last more than one game

while True:

    os.system("cls")
    print("  __ )          |    |    |         ___|   |     _)        ")
    print("  __ \    _` |  __|  __|  |   _ \ \___ \   __ \   |  __ \  ")
    print("  |   |  (   |  |    |    |   __/       |  | | |  |  |   | ")
    print(" ____/  \__,_| \__| \__| _| \___| _____/  _| |_| _|  .__/  ")
    print("                                                    _|     ")

    print("")
    print("-----------------------------------------------------------")
    print("")
    time.sleep(0.5)

    userChoice = MainMenu()

    if(userChoice == "E"):
        print("sure thing bucko, loading...")
        GridSize = 5
        time.sleep(0.5)

    elif(userChoice == "H"):
        print("epic gamer, loading...")
        GridSize = 10
        time.sleep(0.5)

    elif(userChoice == "I"):
        print("It's your funeral, loading...")
        GridSize = 20
        time.sleep(0.5)

    elif(userChoice == "C"):
        GridSize = GetNumberFromUser("How big do you want the board?: ", "You need a number -_-")
        if GridSize > 20:
            print("too big bucko")
            GridSize = 20
        elif GridSize < 5:
            print("too smoll mis amigo")
            GridSize = 5
        time.sleep(0.5)

    elif(userChoice == "O"):
        OptionsThing = OptionsMenu()
        if(OptionsThing == "B"):
            continue
        else:
            print("options have been update yay")
            time.sleep(1)
            continue

    elif(userChoice == "Q"):
        print("okey cya")
        break

    # takes the size of the grid that the user wants

    totalgoes = GridSize * round(GridSize/4)
    
    totalgoeshad = 0
    
    battleshiprow = random.randint(0, GridSize - 1)
    battleshipcolumn = random.randint(0, GridSize - 1)
    
    # makes an empty list that makes an ocean of coordinates
    ocean = []
    
    # making the board
    for i in range(1, GridSize + 1):
        ocean.append(["~"] * GridSize)
    
    # renders ocean thing to screen thing
    def RenderOcean():
        for row in ocean:
            print(" ".join(row))
    
    print("you have " + str(totalgoes) + " goes for this game")
    
    # to make the game last more than one round
    while True:
    
        # takes in the coordinates for the user's guess
        RowAnswer = GetNumberFromUser("please put your row answer here from 1 to grid size: ", "You need a number -_-")
    
        ColumnAnswer = GetNumberFromUser("please put your column answer here as well from 1 to grid size: ", "YOU NEED AN INPUT HOW MANY TIMES")
    
        totalgoeshad += 1
        
        if totalgoeshad == totalgoes:
            print("hold on you've used up all your goes")
            break
        
        if RowAnswer > GridSize or ColumnAnswer > GridSize:
            print("l ur answer too big fix it 菜菜菜菜菜菜菜菜")
            continue
        if RowAnswer <= 0 or ColumnAnswer <= 0:
            print("I forcefully require u to keep ur answer above 0 pls")
            continue
        
        # puts an 'x' for the user's grid coordinate
        ocean[RowAnswer - 1][ColumnAnswer - 1] = "X"
    
        RenderOcean()
    
        # checks if the user hit the battleship
        if RowAnswer == battleshiprow and ColumnAnswer == battleshipcolumn:
            print("You obliterated the battleship you murdering psychopath!")
    
            # stops the loop repeating
            break
        
        else:
            print("hahahahahahaha ur so bad you missed hahahahahahaha, jk try again")
    while True:   
        answer = input('Do you want to play again?: (y/n): ')

        if answer in ('y', 'n'):
            break
        print("it's a simple instruction come on")
    if answer == 'y':
        os.system("cls")
        continue
    else:
        print("okey bye")
        break
