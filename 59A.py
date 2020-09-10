s = input()
supper=0
slower=0
for i in range(len(s)):
    if(s[i].isupper()):
        supper += 1
    else:
        slower += 1
if(supper > slower):
    print(s.upper()) 
else:
    print(s.lower())
