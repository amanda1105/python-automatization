while True:
    print('Who are you?')
    name = input()
    if name != 'Amanda':
        continue
    print('Hello, Amanda! What is theh password? (It is a color)')
    password = input()
    if password == 'red':
        break
print('Access granted.')
