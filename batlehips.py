from random import randint

# takes the size of the grid that the user wants
GridSize = int(input("how big do you want the board?: "))
if GridSize > 20:
    print("too big bucko")
    GridSize = 20
    
elif GridSize < 5:
    print("too smoll mis amigo")
    GridSize = 5

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

# to make the game last more than one round
while True:

    #takes in the coordinates for the user's guess
    RowAnswer = int(input("please put your row answer here from 0 to grid size: "))
    ColumnAnswer = int(input("please put your column answer here as well from 0 to grid size: "))

    #put's an 'x' for the user's grid coordinate
    ocean[RowAnswer][ColumnAnswer] = "X"

    RenderOcean()

# checks if the user hit the battleship
    if RowAnswer == battleshiprow and ColumnAnswer == battleshipcolumn:
        print("You obliterated the battleship you murdering sychopath!")

        # stops the loop repeating
        break

    else:
        print("hahahahahahaha ur so bad you missed hahahahahahaha, but try again")

