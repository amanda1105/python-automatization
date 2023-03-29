print('Hello! What is your name?')
name = input()
print('Cool! And how old are you?')
age = input()

if name == 'Amanda':
    print('Hi, Amanda!')
elif int(age) < 12:
    print('You are not Amanda, kiddo.')
elif int(age) > 2000:
    print('Unlike you, Amanda is not a undead, immortal vampire')
elif int(age) > 100:
    print('You are not Alice, grannie.')
else:
    print('You are nothing, then...')
