import copy

original_list = [1, [2, 3], 4]
shallow_copy = copy.copy(original_list)

print(shallow_copy)
print(original_list[1] is shallow_copy[1])