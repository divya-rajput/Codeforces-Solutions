s = input()
slen = len(s)
count=0

for i in range(slen):
    if(s[i]=='7' or s[i]=='4'):
        count+=1   
if(count==4 or count==7):
    print("YES")
else:
    print("NO")