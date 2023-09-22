def ask_for_input():
    number_picked = input("Pick a number:")
    return number_picked

def echo_user_input(x):
    print(x)

def add_two_number(x,y):
    z = int(x) + int(y)
    print(z)

def multiply_three_numbers(x,y,z):
	return int(x) * int(y) * int(z)
    
def determine_largest(x,y):
     
     if (int(y)) > int(x):
        print("y")
     else:
        print("x")

a = ask_for_input()

echo_user_input(a)

add_two_number(ask_for_input(),ask_for_input())

product = multiply_three_numbers(ask_for_input(),ask_for_input(),ask_for_input())
echo_user_input(product)

a = ask_for_input()
b = ask_for_input()
determine_largest(a,b)
