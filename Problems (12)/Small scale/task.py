list_ = []
while True:
    try:
        x = float(input())
        list_.append(x)
    except ValueError:
        break

print(min(list_))
