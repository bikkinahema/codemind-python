n=input()
s=input()
k=len(n)
for i in range(k):
    if n[i]==s:
        print("True")
        print(i)
        break
    
if n[i]!=s:
    print("False")