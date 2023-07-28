#program to find simple interest by using generators

a = []

for i in range(4):
    k = float(input("Enter rate of interest : "))
    a.append(k)

print(a)    
    
prin = int(input("Enter principal amount "))    
time = int(input("Enter no. of years "))    
    
#int1 = prin*a[0]*time    

def si():
    global int1
    
    for j in range(4):
        int1 = ((prin*a[j]*time)/100)*12

        yield int1

def pr():
    for k in si():
        print(k)    
pr()            