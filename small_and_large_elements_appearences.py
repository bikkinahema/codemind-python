n=input()
n=n.replace(" ","")
min=ord(n[0])
max=ord(n[0])
for i in n:
    if ord(i)<min:
        min=ord(i)
    if ord(i)>max:
        max=ord(i)
a=chr(min)
b=chr(max)
c=0
d=0
for i in n:
    if i==a:
        c+=1
    if i==b:
        d+=1
print(a,c,b,d,end=' ')
        