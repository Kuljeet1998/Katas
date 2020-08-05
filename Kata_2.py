def scale(strng, k, n):
    arr=strng.split()
    arr2=[]
    for x in arr:
        str=""
        for y in range(0,len(x)):
            str=str+x[y]*k
        str=str+"\n"
        arr2.append(str*n)
    #print(arr2)
    str=""
    for x in arr2:
        str=str+x
    return str[:-1]