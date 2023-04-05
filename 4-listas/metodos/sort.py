spam = [2, 5, 3.15, 1, -6]

print(spam)
spam.sort()
print(spam)

animals = ['cat', 'dog', 'ants', 'dinoussaur']

print(animals)
animals.sort()
print(animals)
# arruma em ordem decrescente e trata todos como lowercase
animals.sort(reverse=True, key=str.lower)
print(animals)
