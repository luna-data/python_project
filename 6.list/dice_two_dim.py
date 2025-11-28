rows = 6
cols = 6
table = []

for row in range(rows):
    table += [[0] * cols]

for row in range(rows):
    for col in range(cols):
        table [row][col] = (row+1+col+1)

print(table)