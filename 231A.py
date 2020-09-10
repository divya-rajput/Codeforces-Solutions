
n = int(input())
output=0
for word in range(n):
    s = list(map(int, input().strip().split()))
    count=0
    for i in range(len(s)):
        if (s[i] == 1):
            count+=1
    if(count==2 or count==3):
        output+=1
print(output)    
        
