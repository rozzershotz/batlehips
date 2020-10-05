GridSize = int(input("how big do you want the board?: "))

ocean = []

for i in range(1, GridSize + 1):
    ocean.append(["~"] * GridSize)

for row in ocean:
    print(" ".join(row))

RowAnswer = int(input("please put your row answer here from 0 to grid size: "))
ColumnAnswer = int(input("please put your column answer here as well from 0 to grid size: "))

ocean[RowAnswer][ColumnAnswer] = "x"


for row in ocean:
    print(" ".join(row))