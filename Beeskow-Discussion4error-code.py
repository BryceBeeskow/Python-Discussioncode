# Bryce Beeskow
# Discussion 4
# CSC115
# I certify, that this computer program submitted by me is all of my own work. Signed: Bryce Beeskow
import math

#ask user for 2 numbers then multiply number 1 with itself then divide that number with number2
#find the square root of number 1
print('Enter 2 numbers')

#contains code that might raise an exception

num1 = int(input())
num2 = int(input())
c = num1 * num1
z = c/num2
num1_sqrt = math.sqrt(num1)


print(f'{num1} * {num1} = {c}')
print(f'{c} / {num2} = {z} ')
print(f'The Square root of {num1} is {num1_sqrt}')
