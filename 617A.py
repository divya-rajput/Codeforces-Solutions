n = int(input())
output = 0
for i in range(n):
    if(n >= 5):
        output += 1 
        n = n-5
    elif(n >= 4):
        output += 1 
        n = n-4
    elif(n >= 3):
        output += 1 
        n = n-3
    elif(n >= 2):
        output += 1 
        n = n-2
    elif(n >= 1):
        output += 1 
        n = n-1
print(output)