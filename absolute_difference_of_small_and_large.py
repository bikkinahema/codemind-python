n=input()
w=n.split()
for i in w:
    mi=min(i)
    ma=max(i)
    a=ord(mi)
    b=ord(ma)
    print(abs(a-b),end=' ')
