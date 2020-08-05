def sum(num):
    s=0
    for x in range(1,num):
        if(num%x==0):
            s=s+x
    #print(s)
    return s

def buddy(start, limit):
    arr=[]
    a=0
    for x in range(start,limit+1):
        b1=sum(x)
        b2=sum(b1-1)
        if(b2-1==x and b1-1>x):
            arr.append(x)
            arr.append(b1-1)
            a=1
            break
    if(a==1):
        return arr
    else:
        return "Nothing"