"""
Write a python script to find maximum length word in a  given text
"""

# taking input from the user
string = input("Enter a string : ")

# defining a variable 
word_length = 1
max_length_word = str()

# finding maximum length word in a given text
for word in string.split(' ') :
    if len(word) > word_length :
        word_length = len(word)
        max_length_word = word
        
# printing maximum length word
print("Maximum length word is :", max_length_word)