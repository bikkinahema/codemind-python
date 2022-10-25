s=input()
c=0
for i in s:
    if i.isalpha():
        continue
    if i.isdigit():
        continue
    if i==' ':
        continue
    c+=1
print(c)