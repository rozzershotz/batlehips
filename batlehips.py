# takes the size of the grid that the user wants
GridSize = int(input("how big do you want the board?: "))

# makes an empty list that makes an ocean of coordinates
ocean = []

# making the board
for i in range(1, GridSize + 1):
    ocean.append(["~"] * GridSize)

# renders ocean thing to screen thing
def RenderOcean():
    for row in ocean:
        print(" ".join(row))

while True:

    #takes in the coordinates for the user's guess
    RowAnswer = int(input("please put your row answer here from 0 to grid size: "))
    ColumnAnswer = int(input("please put your column answer here as well from 0 to grid size: "))

    #put's an 'x' for the user's grid coordinate
    ocean[RowAnswer][ColumnAnswer] = "x"

    # line 11
    RenderOcean()