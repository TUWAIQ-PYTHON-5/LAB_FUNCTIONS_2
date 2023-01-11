def func2 (num1,num2):
    for num in range(num1,num2 +1):
        if num>num1 and num<num2 :
            for i in range(2,num):
                if (num % i)==0:
                    break
            else:
                print(num)
func2(25,50) 