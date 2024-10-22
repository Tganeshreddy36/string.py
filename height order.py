...
 There are 50 students in the class. The teacher wants to arrange them in the height order. So help the teacher to find the smallest person and tallest to arrange.(count the number of lowercase letters and uppercase letters in a string.)
Problem Description:
The program takes a string and counts the number of lowercase letters and uppercase letters in the string.
Problem Solution:
1. Take a string from the user and store it in a variable.
2. Initialize the two count variables to 0.
3. Use a for loop to traverse through the characters in the string and increment the first count variable each time a lowercase character is encountered and increment the second count variable each time a uppercase character is encountered.
4. Print the total count of both the variables.
5. Exit.
Input & Output Format:
Input consists of one string.
Output consists of two integers.
First output consists of count of the uppercase.
Second output consists of count of the lowercase.
...
...
input_string = input("Enter a string: ")
lowercase_count = 0
uppercase_count = 0
for char in input_string:
    if char.islower():  # Check if the character is lowercase
        lowercase_count += 1
    elif char.isupper():  # Check if the character is uppercase
        uppercase_count += 1
print(uppercase_count)  # First output: count of uppercase letters
print(lowercase_count)   # Second output: count of lowercase letters
...
