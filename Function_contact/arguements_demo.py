trup = ('a', 2, 4, "f", 'g')
dir_01 = {'a': 1, 'b': 2, 'c': 3}


def args_demo(*args):
    print(*args)
    print(args)


def dir_demo(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
    print(kwargs)


def return_demo(i):
    if i < 10:
        j = i * return_demo(i+1)
        print(j)
        return j
    else:
        return 5


args_demo(*trup)
# dir_demo({'a': 1, 'b': 2, 'c': 3})
print('''换行

''')
dir_demo(**dir_01)

return_demo(4)