# import random
# generated = random.randint(0, 100)

# numbers = int(input("Enter number:"))

# i = 0
# while(i < 100):
#     if numbers < generated:
# 	    print("Caut un numar mai mare")
#     elif numbers > generated:
# 	    print("Caut un numar mai mic")
#     else:
#     	print("Corect!")
# 	    break
#     i+=1



# import random
# generated = random.randint(0, 100)
#
# i = 0
# while(i < 100):
#     numbers = int(input("Enter number:"))
#     if numbers < generated:
# 	    print("Caut un numar mai mare")
# 	    continue
#     elif numbers > generated:
# 	    print("Caut un numar mai mic")
# 	    continue
#     else:
#     	print("Corect!")
#     break
# i+=1



import random
generated = random.randint(0, 100)

i = 0
while(i < 100):
    numbers = int(input("Enter number:"))
    if numbers < generated:
	    print("Caut un numar mai mare")
    elif numbers > generated:
	    print("Caut un numar mai mic")
    else:
    	print("Corect!")
    break
