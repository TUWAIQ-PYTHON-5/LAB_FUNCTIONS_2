
start = 25
last_number = 50

for number in range(start, last_number + 1):
    
    if number > 1:
        for i in range(2, number):
            
            if (number % i) == 0:
                
                break
        else:
            print(number)