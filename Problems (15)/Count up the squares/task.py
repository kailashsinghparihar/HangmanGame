# put your python code here
try:
    my_list = []
    while True:
        my_list.append(int(input()))
except EOFError:
    s = 0
    my = []
    for i in my_list:
        s = s + i
        my.append(i)
        if s == 0:
            break
    d = 0
    for j in my:
        d = d + j*j
    print(d)
