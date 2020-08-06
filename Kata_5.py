import math
def squared_sum(n):
    fact=[]
    for x in range(2,int(math.sqrt(n))+1):
        if(n%x==0):
            fact.append(int(x*x))
            fact.append(int((n/x))*int((n/x)))
    fact.append(1)
    fact.append(n*n)
    if(n==42):
        print(fact)
    return sum(list(set(fact)))

def list_squared(m, n):
    pairs=[]
    for x in range(m,n+1):
        pair=[]
        summ=squared_sum(x)
        root=math.sqrt(summ)
        if(root-math.floor(root)==0):
            pair.append(x)
            pair.append(int(summ))
            pairs.append(pair)
    print(pairs)
    return pairs