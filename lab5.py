
num1 = int(input (" Enter the first number :   "))  
num2 = int(input (" Enter the second number :   ")) 

def prime_number(num1,num2) :

 for number in range (num1,num2):  
    if number > 1:  
        for x in range (2,number):  
            if (number % x) == 0:  
                break
        else: 
         print (number) 
         
prime_number(num1,num2)
            

