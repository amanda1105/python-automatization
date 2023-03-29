while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is your password? (it is a color)')
    password = input()
    if password == 'red':
        print('Access granted')
        break
