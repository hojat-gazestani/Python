def spam():
    print(eggs) # ERROR!
    eggs = 'spam local'
    print(eggs)

eggs = 'global'
spam()
