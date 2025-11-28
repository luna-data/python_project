matrix = {(1,2): 1, (2,2): 2, (3,2): 3}

for r in range(5):
  for c in range(5):
    print(matrix.get((r,c),0), end = " ")
  print()