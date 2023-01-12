first = int(input("the first number:"))
second = int(input("the second number"))
print("prime numbers ",first,second)


def prnumbers (first,second):
    for v in range(first,second):
        if v > 1:
            for i in range(2,v):
                if (v % i) == 0:
                    break
            else:
             print(v, end="")
             print("")



prnumbers(25,50)