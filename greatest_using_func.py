def great(num1,num2,num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        else :
            return num3
    else :
        return num2
x = int(input("enter first number : ")) 
y = int(input("enter second number : ")) 
z = int(input("enter third number : ")) 
m = great(x, y, z)
print(f"greatest number is {m}")