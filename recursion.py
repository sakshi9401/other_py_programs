def recur(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * recur(num - 1) 

num = int(input("enter no : "))
f = recur(num)
print(f"factorial of {num} is {f}")