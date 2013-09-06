l2 = []
for i in range(3, 1000000):
    l = map(int,list(str(i)))
    SUM = 0
    for x in l:
        if x:
          factorial = reduce(lambda x,y: x*y,range(1,x+1))
          SUM += factorial
    if i==SUM:
        print i, SUM
        l2+=[i]
print sum(l2)
