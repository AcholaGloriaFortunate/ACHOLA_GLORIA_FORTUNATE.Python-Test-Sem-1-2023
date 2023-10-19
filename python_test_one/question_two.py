def average_of_two_numbers(x, y):
    return (x + y)/2

number1 = 30
number2 = 40
output = average_of_two_numbers(number1, number2)
print(f"the average of {number1} and {number2} is {output}")

number1 = float(input("enter the first number:"))
number2 = float(input("enter the second number:"))
number3 = float(input("enter the third number:"))

min_number = min(number1, number2, number3)
print(f"The minimum number is:{min_number}")