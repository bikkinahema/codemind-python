s1=input()
s2=input()
s1=s1.replace(" ","")
s2=s2.replace(" ","")
p=len(s1)
s1=s1.lower()
s2=s2.lower()
c=0
for i in s1:
    for j in s2:
        if i==j:
            c+=1
if c==p:
    print("True")
else:
    print("False")