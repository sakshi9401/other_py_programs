num = int(input("enter a number : "))
i = 1
fact = 1
for i in range(i,num+1):#range stops at n-1 i.e.,
                         #if we have to print 10 no. 
                         # then range should be upto 11
    fact = fact * i
print("factorial of " + str(num) + " is " + str(fact))

