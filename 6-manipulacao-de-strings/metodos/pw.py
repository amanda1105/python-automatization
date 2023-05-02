#! python3
# Um programa para repositório de senhas que não é seguro

import pyperclip
import sys
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

# o primeiro argumento da linha de comando é o nome da conta
account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for' + account + ' copied to clipboard.')
else:
    print('There is no account named' + account)
