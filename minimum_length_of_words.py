n=input()
s=n.split()
k=len(s)
min=len(s[0])
for i in range(1,k):
    x=s[i]
    c=len(x)
    if min>c:
        min=c
print(min)
    