import random 

x = input("pick a number between 1 and 100: ")
#Utilize the buit-in input function to adk the user a question.
#Set the value of x to the user typed value

y = random.randint(1,100)
# Utilize the random function to generate a random number between 1-100
# Save this value to the variable y

print("you picked " + x + " and the number " + str(y) + " was generated")
# Print the two values using a regular string 

print(f"You picked {x} and the number generated was {y}".format(x,y))
# Print the two values using an fstring this time

if int(x) < y:
    print("Too Low!")
if int(x) > y:
    print("Too High!")
if int(x) == y:
    print("Correct")