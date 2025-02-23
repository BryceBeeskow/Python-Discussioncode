import math
# Bryce Beeskow
# 10/30/2024
# CSC115
# Discussion 1

#Introduce what this code is about
print('Please enter 4 numbers to get the average and factorial ')

# Asking user to enter 4 numbers and assigning them with a variable
number1 = int(input('Please enter number 1: '))
number2 = int(input('Please enter number 2: '))
number3 = int(input('Please enter number 3: '))
number4 = int(input('Please enter number 4: '))


# Finding the average of the 4 numbers
ave = (number1 + number2 + number3 + number4) / 4

# Finding the factorial of the 4 numbers
num1_factorial = math.factorial(number1)
num2_factorial = math.factorial(number2)
num3_factorial = math.factorial(number3)
num4_factorial = math.factorial(number4)

# Print the Average and Factorial
print('The average of your numbers is:', ave,'\n')
print(number1,'! is', num1_factorial)
print(number2,'! is', num2_factorial)
print(number3,'! is', num3_factorial)
print(number4,'! is', num4_factorial)