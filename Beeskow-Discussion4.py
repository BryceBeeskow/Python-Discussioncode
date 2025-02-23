# Bryce Beeskow
# Discussion 4
# CSC115
# I certify, that this computer program submitted by me is all of my own work. Signed: Bryce Beeskow
import math

#ask user for 2 numbers then multiply number 1 with itself then divide that number with number2
#find the square root of number 1
print('Enter 2 numbers')

#contains code that might raise an exception
try:
    num1 = int(input())
    num2 = int(input())
    c = num1 * num1
    z = c/num2
    num1_sqrt = math.sqrt(num1)

#executes when num2 is 0 because you cant divide by 0
except ZeroDivisionError:
    print('Invalid number entered. num2 cant equal 0 in order to divide.')   

#executes when num1 is a negative because math module doesnt work with negative numbers
except ValueError:
    print('Invalid number entered. num1 must be a positive number to find the square root. ')

#else when there are no exceptions raised
else:
    print(f'{num1} * {num1} = {c}')
    print(f'{c} / {num2} = {z} ')
    print(f'The Square root of {num1} is {num1_sqrt}')

#always executes no matter what
finally:
    print("Thanks for giving me two numbers")