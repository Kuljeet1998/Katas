def custom_christmas_tree(chars, n):
    arr=[]
    for x in chars:
        arr.append(x)
    print(arr)
    str=""
    index=0
    for x in range(0,n):
        for y in range(0,n-x-1):
            str=str+" "
        for y in range(0,x+1):
            str=str+arr[index]+" "
            arr.append(arr[index])
            index+=1
        str=str[:-1]
        str=str+"\n"
    trunk=int(n/3)
    for x in range(0,trunk):
        for y in range(0,n-1):
            str=str+" "
        str=str+"|"+"\n"
    print(str)
    return str[:-1]