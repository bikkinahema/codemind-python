n=int(input())
l=list(map(int,input().split()))
k=[]
p=[]
c=0
for i in l:
    i=str(i)
    k=len(i)
    if len(i)%2==0:
        c+=1
print(c)