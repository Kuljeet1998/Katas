def open_or_senior(data):
    category=[]
    for x in range(0,len(data)):
        if(data[x][0]>=55 and data[x][1]>7):
            category.append("Senior")
        else:
            category.append("Open")
    return category
