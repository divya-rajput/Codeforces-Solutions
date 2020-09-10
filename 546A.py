a, b, n = [int(x) for x in input().split(' ')] 
sum = int((n/2)*((2*a)+((n-1)*a)))
if(b >= sum):
    print('0')
else:
    print(sum - b)

