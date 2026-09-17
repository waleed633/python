# Program make a simple calulator

# this function adds two numbers 
def add(x, y):
    return x + y
# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

num1 = int(input("Enter Number 1: "))
num2 = int(input("enter number 2: "))

print("sum :", add(num1, num2))
print("diffrence :", subtract(num1, num2))
print("product :", multiply(num1, num2))
print("Qoutient :", divide(num1,num2))