
def find_prime(number):
    if number > 1:
        prime = False
        for check in range(2,number):
            if number % check == 0:
                prime = True
                break
            else:
                prime = False
                break
        if prime == True:
            return
        else:
            print(number)
    else:
        return
    


startPoint = int(input("Enter a starting point: "))
endPoint = int(input("Enter a ending point: ")) + 1

for check in range(startPoint,endPoint):
    find_prime(check)

