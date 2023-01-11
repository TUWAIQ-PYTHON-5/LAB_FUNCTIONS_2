
#Create a function to print prime numbers

def find_primes(x , y) -> None:
    """Find prime numbers"""
    for numbers in range(x , y):
        isPrime  =  True
        for i in range( 2 , numbers): 
            if (numbers % i == 0):
                isPrime = False
                break
        if isPrime:
            print(numbers) 


inputFirstNumber = int(input("the lower number "))
inputSecandNumber = int(input("the biggest number "))

results = find_primes(inputFirstNumber,inputSecandNumber)                   
print(results)
