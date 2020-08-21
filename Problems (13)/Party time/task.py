try:
    my_list = []
    while True:
        my_list.append(input())
except EOFError:
    my = []
    for i in my_list:
        if i != '.':
            my.append(i)
        else:
            break
    print(my)
    print(len(my))
