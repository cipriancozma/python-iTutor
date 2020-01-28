
# Ex 1
def functiaMea():
    sum = 0
    
    for i in range(0, 101):
        if (i % 2) == 0:
            sum = sum + i
            continue
        
        if i < 10:
            print(i)
        
        if i > 10 and i < 20:
            continue
    
    print(sum)

functiaMea()


# Ex 2
def functiaMea2():
    for i in range(0, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            continue
        elif i % 3 == 0:
            print("Fizz")
            continue
        elif i % 5 == 0:
            print("Buzz")
            continue
        
        print(i)

functiaMea2()