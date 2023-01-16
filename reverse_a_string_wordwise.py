"""
Write a python script to reverse a string word wise
(for example - "mysirg education services" is a given string and resulting string
 should be "services education mysirg")
"""

# taking input from the user
string = input("Enter a string of multiple words : ")

# reversing a string word wise
reversed_string = str()

for e in (string.split(' '))[::-1] :
    reversed_string = reversed_string + e + ' '

# printing reversed word wise string
print("Reversed string :", reversed_string)