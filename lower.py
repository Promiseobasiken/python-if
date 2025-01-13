#  Write a function that checks for lowercase character.

# Prototype: def islower(c):
# Returns True if c is lowercase
# Returns False otherwise
# You are not allowed to import any module
# You are not allowed to use str.upper() and str.isupper()
# Tips: ord()
# You don’t need to understand _import_
alpha = input("type in a lowercase c: \n")

for c in alpha:
    if c.islower():
        print(alpha)
    else:
        print('use lowercase c only')
        exit()