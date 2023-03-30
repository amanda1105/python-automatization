def spam():
    eggs = 'spam local'
    print(eggs)  # exibe 'spam local'


def bacon():
    eggs = 'bacon local'  # exibe 'bacon local'
    print(eggs)
    spam()
    print(eggs)  # exibe 'bacon local'


eggs = 'global'
bacon()
print(eggs)  # exibe 'global'
