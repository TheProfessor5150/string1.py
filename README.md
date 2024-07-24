Fill in the Code:

You will complete the functions provided in the string1.py file.
Each function has a description of what it should do. Your task is to write the code inside each function to achieve the described behavior.
The main() function is already set up to call these functions with various inputs and print 'OK' when a function is correct.
Function Descriptions:

A. donuts:
Given an int count of a number of donuts, return a string of the form 'Number of donuts: ', where <count> is the number passed in. However, if the count is 10 or more, then use the word 'many' instead of the actual count.
Example: donuts(5) should return 'Number of donuts: 5' and donuts(23) should return 'Number of donuts: many'.
B. both_ends:
Given a string s, return a string made of the first 2 and the last 2 chars of the original string.
Example: both_ends('spring') should return 'spng'. If the string length is less than 2, return the empty string instead.
C. fix_start:
Given a string s, return a string where all occurrences of its first char have been changed to '*', except do not change the first char itself.
Example: fix_start('babble') should return 'ba**le'.
D. mix_up:
Given strings a and b, return a single string with a and b separated by a space <a> <b>, except swap the first 2 chars of each string.
Example: mix_up('mix', 'pod') should return 'pox mid' and mix_up('dog', 'dinner') should return 'dig donner'.
Testing Your Code:

The main() function includes test cases that will help you verify if your implementations are correct.
The test() function compares the output of your function with the expected result and prints 'OK' if they match, otherwise it prints 'X'.
Submission
Complete as many functions as you can.
Ensure your code runs without errors.
Submit your completed string1.py file by pushing your repo to GitHub and it will auto grade.
Happy coding!
