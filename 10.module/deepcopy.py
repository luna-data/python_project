import copy

original_list = [1, [2, 3], 4]

deep_copy = copy.deepcopy(original_list)

print(deep_copy)
print(original_list[1] is deep_copy[1])