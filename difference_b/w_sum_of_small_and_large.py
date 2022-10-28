n=input()
w=n.split()
a=0
b=0
for i in w:
    mi=min(i)
    ma=max(i)
    c=ord(mi)
    d=ord(ma)
    a+=c
    b+=d
print(b-a)
    