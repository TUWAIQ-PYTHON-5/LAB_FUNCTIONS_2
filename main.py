def find_prime_numbers(start:int, end:int)-> int:
    '''This function is to search for prime numbers from the starting and end you put it'''

    for num in range(start, end+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
find_prime_numbers(start, end)