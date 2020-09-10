
n, k = map(int,input().split())
count=0
s = list(map(int, input().strip().split()))
for i in range(n):
    if(s[i] >= s[k-1] and s[i] != 0): 
        count+=1
print(count)




