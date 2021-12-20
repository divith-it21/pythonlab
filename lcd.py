def computeLCD(x, y): 
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            return i
            
a=int(input("Enter a num 1:"))
b=int(input("Enter a num 2:"))
c=computeLCD(a,b)
print("LCD=",c)
