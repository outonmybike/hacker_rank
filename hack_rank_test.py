def fizzBuzz(n):
    for x in range(n+1):
        if x == 0:
            continue
        elif (x % 3 == 0 and x % 5 == 0):
            print('FizzBuzz')
        elif ( x % 3 == 0):
            print('Fizz')
        elif (x % 5 ==0):
            print('Buzz')
        else:
            print(x)
fizzBuzz(15)