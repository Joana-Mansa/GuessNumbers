import random
value= random.randint(0,20)
print(value)
choice= int(input("Guess the value: "))
if value==choice:
    print ("Ëxactement!")
elif value>choice:
    print("You're close to it")
elif value<choice:
    print("You're too far")
    

