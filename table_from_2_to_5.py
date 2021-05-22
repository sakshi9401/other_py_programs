from os import write


for i in range(2, 6):
    with open(f"table of{i}.txt","w") as f:
        for j in range(1, 11):
            f.write(f"{i} X {j} is {i*j}")
            if(j!= 10):
                f.write("\n")
               




















