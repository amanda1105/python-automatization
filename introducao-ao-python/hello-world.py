# Este programa diz hello e pergunta seu nome.

print('Hello world!')

print('What is your name?')  # pergunta o nome
myName = input()

print('It is nice to meet you, ' + myName)
print('The lenght of your name is:')
print(len(myName))

print('What is your age?')  # pergunta a idade
myAge = input()

print('You will be ' + str(int(myAge) + 1) + ' in a year.')
