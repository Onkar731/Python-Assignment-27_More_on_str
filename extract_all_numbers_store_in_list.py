"""
Write a python script to extract numbers from a given text and store all the 
numbers in a list
"""

# taking input from the user
string = input("Enter a string : ")

# creating a list empty list for extracted digits
digits = list()

# extracting numbers from a given text
for ch in string :
    if ch.isdigit() :
        digits.append(int(ch))
        
# printing list of extracted numbers from the string
if len(digits) != 0 :
    print("Extracted numbers are :", digits)
else :
    print("String has 0 digits in it")