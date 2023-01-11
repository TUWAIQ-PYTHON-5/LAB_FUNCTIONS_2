def find_prime (num1:int,num2:int):
    for number in range(num1,num2 +1):
        if number>num1 and number<num2 :
            for x in range(2,number):
                if (number % x)==0:
                    break
            else:
                print(number) 
find_prime(10,50)  
  
    
    