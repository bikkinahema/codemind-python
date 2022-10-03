s=input()
c=0
for i in s:
    if i.isdigit()==True:
        c+=1
if c>1:
    print("Contains {} digit".format(c))
else:
    print("Doesn't contain digit")