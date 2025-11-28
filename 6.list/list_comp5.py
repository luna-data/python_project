new_list = []
for x in range(1,31):
  for y in range(x, 31):
    for z in range(y, 31):
      if x**2 + y**2 == z**2:
        new_list.append((x,y,z))
print(new_list)