...
Write a  Python Program to calculate the number of words and characters present in a string.
Input & Output Format:
Input consists of a string.
Output consists of two integers.
First output refers to the count of the words.
Second output refers to the count of the characters in a given string,
...
...
input_string = input("Enter a string: ")
word_count = len(input_string.split())
character_count = len(input_string)
print(word_count)      
print(character_count)   
...
