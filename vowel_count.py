n=input()
l=len(n)
c=0
for i in range(l):
    if n[i]=='a' or n[i]=='e' or n[i]=='i' or n[i]=='o' or n[i]=='u' or n[i]=='A' or n[i]=='E' or n[i]=='I' or n[i]=='O' or n[i]=='U' :
        c+=1
print(c)
    