n=input()
s=n.split()
k=len(s)
max=0
for i in range(0,k):
    x=s[i]
    c=len(x)
    if max<c:
        max=c
print(max,end=' ')
    