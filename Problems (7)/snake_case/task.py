value = input()
if value.islower():
    print(value)
else:
    for ch in value:
        if ch.isupper():
            value = value.replace(ch, "_" + ch.lower())
    print(value.lower())
