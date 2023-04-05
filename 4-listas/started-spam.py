spam = ['cat', 'bat', 'rat', 'elephant']

print('Hello ' + spam[0])
print('The ' + spam[1] + ' ate the ' + spam[0] + '.')

print(spam[-2])  # puxa as informações de trás para frente

# slices
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])

print(len(spam))  # tamanho de uma lista

del spam[2]  # deleta da lista
print(spam)
