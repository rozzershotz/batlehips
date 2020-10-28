from random import randint

# takes the size of the grid that the user wants
GridSize = int(input("how big do you want the board?: "))
if GridSize > 20:
    print("too big bucko")
    GridSize = 20
    
elif GridSize < 5:
    print("too smoll mis amigo")
    GridSize = 5

totalgoes = GridSize * round(GridSize/4)

totalgoeshad = 0

battleshiprow = randint(0, GridSize - 1)
battleshipcolumn = randint(0, GridSize - 1)

# battleshipcolumn = 5
# battleshiprow = 5

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
    RowAnswer = int(input("please put your row answer here from 1 to grid size: "))
    ColumnAnswer = int(input("please put your column answer here as well from 1 to grid size: "))

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
        print("hahahahahahaha ur so bad you missed hahahahahahaha, but try again")

