n=int(input())
l=list(map(int,input().split()))
t=0
for i in range(0,n):
   t+=l[i]
average=t/n
print("{:.2f}".format(average))