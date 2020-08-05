def loose_change(cents):
    cents=int(cents)
    dict={'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    if(cents<=0):
        return dict
    else:
        while(cents!=0):
            if(cents>=25):
                dict["Quarters"]+=1
                cents-=25
            elif(cents>=10):
                dict["Dimes"]+=1
                cents-=10
            elif(cents>=5):
                dict["Nickels"]+=1
                cents-=5
            else:
                dict["Pennies"]+=1
                cents-=1
    print(dict)
    return dict