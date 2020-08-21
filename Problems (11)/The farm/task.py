rupe = int(input())
if rupe < 23:
    print("None")
elif 23 <= rupe < 678:
    if rupe//23 == 1:
        print(" 1 chicken")
    else:
        print(str(rupe//23) +" chickens")
elif 678 <= rupe < 1296:
    print(str(rupe//678) +" goat")
elif 1296 <= rupe < 3848:
    if rupe//1296 == 1:
        print("1 pig")
    else:
        print(str(rupe//1296) +" pigs")
elif 3848 <= rupe < 6769:
    print(str(rupe//3848) +" cow")
else:
    if rupe//6769 == 1:
        print("1 sheep")
    else:
        print(str(rupe//6769) +" sheep")
