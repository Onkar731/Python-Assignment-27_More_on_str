"""
Write a python script to check whether it is a pallindrome or not
"""

# taking input from the user
string = input("Enter a string : ")

# checking whether a string is pallindrome or not
if string == string[::-1] :
    print("Pallindrome string -", string)
else :
    print("Non pallindrome string -", string)