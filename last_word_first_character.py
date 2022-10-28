s=input()
w=s.split()
t=w[::-1]
for i in t:
    for j in i:
        print(j)
        break
    break