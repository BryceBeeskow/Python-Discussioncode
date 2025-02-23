# Bryce Beeskow
# Discussion 2
# CSC115
# I certify, that this computer program submitted by me is all of my own work. Signed: Bryce Beeskow


grocery_list = ['Bread', 'Milk', 'Dog Food', 'Burgers', 'Cheese']
grocery_price = [2.99, 3.49, 64.99, 8.99, 3.19]

grocery_list.remove('cheese')


for i in range(len(grocery_list)):
    print(f'{grocery_list[i]} is ${grocery_price[i]:.2f}')