import math
def solve(m):
	#Solving using quadratic equations
    a=m
    b=-(2*m)-1
    c=m
    d=math.sqrt(b*b-4*a*c)
    x=(-b-d)/(2*a)
    return x