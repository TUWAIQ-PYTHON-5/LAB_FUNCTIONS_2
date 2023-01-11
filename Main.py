
# def find_primes(num1 : int ,num2 : int) -> int:
#     if num2 > num1:
        
#         for i in range (num1 , num2 +1):
#             if i % 2 !=0 and i / i == 1 :
#                 print(i)

            
#             else:
#                 continue
#     else:
#         print("Second number must be greater than First number")


# find_primes(int(input("enter first number")) , int(input("enter second number")))



def findprime(num1:int  , num2:int):
    

        for i in range(num1 , num2 +1):
            
                if(i==1):
                    continue
                elif(i == 2 or i ==3):
                    print(i)
                elif (i % 2 != 0 and i % 3 !=0 and i % 5 !=0):
                    print(i)
                   
        print("The End of Loop")



findprime( int(input("please enter the first number")) , int(input("please enter the second number")) )        
            
            

   


    

