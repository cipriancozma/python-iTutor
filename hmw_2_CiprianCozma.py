number = input("Enter a number: ")

sum = 0
countEven = 0
countOdd = 0
sumEven = 0
sumOdd = 0

for i in number:
    sum += int(i)
    palindrom = str(number) == str(number)[::-1]

    if int(i) % 2 == 0:
        print("Even!")
        countEven += 1
        sumEven += int(i)

    else:
        countOdd +=1
        sumOdd += int(i)

print("The sum is: ", sum)
print("Even numbers: ", countEven)
print("Odd numbers: ", countOdd)
print("Sum of even numbers: ", sumEven)
print("Sum of odd numbers: ", sumOdd)
print("Palindrom number: ", str(palindrom))



# Second part
maxNumber = []
sumaOdd = 0
while True:
    number = int(input("Enter a number: "))
    maxNumber.append(number)
    if number % 2 == 0:
        pass
    else:
        sumaOdd += number
    if number == 0:
        break
    if number > 0:
        continue


print("Max number: ", max(maxNumber))
print("Sum odd numbers: ", sumaOdd)

# Sa se afiseze numarul maxim de numere citite consecutiv crescator
# Si aici la fel sunt impotmolit, ce ar trebui sa afisez daca am 1 2 3 0 4 5 6 ca input?
