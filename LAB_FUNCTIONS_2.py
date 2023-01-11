# Create a function : find_primes that takes in 2 parameters of type int , 
# and print the prime numbers between the first parameter and the second parameter . 


def find_primes( num1 : int , num2 : int):
    ''' here first we have a counter if the counter grater than 1 then it is not a prime number 
    , then we have a nested loop the first one take the the number we will check every time if 
    it is a prime number or not by divied it by number2 by using the seconde loop the .
    the idea here if it is a prime number it will divide once which means the counter will equal to 1 and the number will print '''
    for number1 in range(num1 , num2):
        count = 0
        for number2 in range(2 , num2):
            if number1 % number2 == 0 :
                count = count +1

        if count ==1 :
            print(number1)
            

find_primes(25,50)





        

   