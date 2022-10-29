s=input()
s=s.lower()
w=s.split()
c=0
for i in w:
    j=i[::-1]
    if i==j:
        c+=1
print(c)