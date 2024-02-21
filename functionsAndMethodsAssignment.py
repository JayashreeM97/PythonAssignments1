'''#write a function given number is even or odd 
def typeOfNumber(num):
    if num %2==0:
        print("Given number is Even number")
    else:
        print("Givent number is Odd number")
num=int(input("Enter the number"))
result=typeOfNumber(num)

#write a func which contains some number as arg and print square of that numbers

def squareOfNumber(numbers):
    for num in numbers:
        square= num ** 2
        print(f"the square of {num} is {square}")
numbers=[2,4,5,6,7,8]
squareOfNumber(numbers)'''

#write a program using function for addition  ,sub, multiplication, division
# Function for addition
def add(x, y):
    return x+y
# Function for subtraction
def subtract(x, y):
    return x-y
# Function for multiplication
def multiply(x, y):
    return x*y

# Function for division
def divide(x, y):
    if y==0:
        return "error"
    else:
        return x/y
if __name__ == "__main__":
    num1=int(input("Enter the first number"))
    num2=int(input("Enter the second number"))

    print("Addition:", add (num1, num2))
    print("Subtraction:", subtract(num1, num2))
    print("Multiplication:", multiply(num1, num2))
    print("Division:", divide(num1, num2))

