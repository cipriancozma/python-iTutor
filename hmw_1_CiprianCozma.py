import random
generated = random.randint(0, 100)
number = 0

while(number != generated):
    number = int(input("Enter number:"))
    if number < generated:
	    print("Caut un numar mai mare")
    else:
	    print("Caut un numar mai mic")

print("Corect!")