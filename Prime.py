'''# LAB_FUNCTIONS_2

## Create a function : find_primes that takes in 2 parameters of type int , and print the prime numbers between the first parameter and the second parameter . 

#### hint
a prime number i a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11)    
Also , you can think of it as A Prime Number is a number that cannot be made by multiplying other whole numbers


#### for example, primes between 25 and 50 are:
29   
31   
37   
41   
43   
47   
'''


def find_primes(lowestNum :int ,highestNum :int):
    highestNum +=1
    for loop1 in range(lowestNum, highestNum):
        for loop2 in range(2,loop1):
            if (loop1%loop2) == 0: 
             break 
        else:
            print(loop1) 
  
usrNumber1: int = int(input("Enter a low Number "))
usrNumber2: int = int(input("Enter a high Number "))
find_primes(usrNumber1,usrNumber2)