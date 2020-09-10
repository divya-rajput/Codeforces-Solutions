n = int(input())
s = input()
cA=0 
cD=0
for i in range(n):
    if(s[i]=='A'):
        cA+=1
    else:
        cD+=1
if(cA > cD):
    print("Anton")
elif(cD > cA):
    print("Danik")
else:
    print("Friendship")
