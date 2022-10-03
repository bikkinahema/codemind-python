n=int(input())
for i in range(n):
    s=input()
    d=0
    for i in (s):
        if (i.isdigit()):
            d+=1
    if d>0:
        print("Yes")
    else:
        print("No")