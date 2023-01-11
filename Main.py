def findprime(max:int ):
    print(1)
    for i in range(2 ,max+1):
      prime = True
      for j in range(2 , i):
        num = i%j
        if num == 0:
          prime = False
          break
      if prime:
        print(i)  


findprime(50)        
    
 
