#  Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example)

# You can only use one print function with string format
# You can only use one loop in your code
# You are not allowed to store numbers or strings in a variable
# You are not allowed to import any module

# num1 = int(input("Type in a number: "))
# num2 = input("Type in another number: ")

# num1 = hex(num1)
# num2 = float(num2)
# print(num1, num2)

for i in range (0, 99):
    print("{}" ,"{0:.0f}".format( i, i+i, i+i+i))