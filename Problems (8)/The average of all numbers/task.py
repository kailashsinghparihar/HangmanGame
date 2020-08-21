# put your python code here
f1 = int(input())
f2 = int(input())
count = 0
ad = 0
for i in range(f1, f2+1):
    if i%3==0:
        count = count + 1
        ad = ad + i
print(ad/count)
