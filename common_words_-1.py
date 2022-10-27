s1=input()
s2=input()
s3=s1.lower()
s4=s2.lower()
w1=s3.split()
w2=s4.split()
c=0
for i in w1:
    for j in w2:
        if i==j:
            c+=1
print(c)