
def distinct(year):
    nlist = []
    n = [int(x) for x in str(year)] 
    nlist = set(n)
    if(len(n) == len(nlist)):
        return year
    

year_n = int(input())
for year_n in range(9000):
    year_o = distinct(i)
    print(type(year_o),type(year_n))
    if(year_o > year_n):
        print(year_o)
