def ip_to_int32(ip):
    octet=ip.split(".")
    index=0
    for x in octet:
        octet[index]=format(int(x),'08b')
        index+=1
    str=""
    for x in octet:
        str=str+x
    return int(str,2)