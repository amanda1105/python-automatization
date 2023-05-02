#! python3
# bulletPointAdder.py - Acrescenta marcadores da Wikipedia no início de cada linha de texto do clipboard.
# TODO: Separa as linhas e acrescenta asteristicos.

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):  # percorre todos os índices da lista "lines" em um loop
    # acresenta um asteristico em cada string da lista "lines"
    lines[i] = '*' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
