import copy

spam = ['A', 'B', 'C', 'D', 'E', 'F']

cheese = copy.copy(spam)

print(cheese)
cheese[1] = 42
print(spam)
print(cheese)
