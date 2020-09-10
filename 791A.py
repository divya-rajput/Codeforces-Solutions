a, b = [int(x) for x in input().split(' ')]
for i in range(10): 
    if (a > b):
        print(i)
        break
    else:
        a = 3 * a
        b = 2 * b
