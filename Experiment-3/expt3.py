Aim:
The aim of this experiment is to implement and demonstrate fundamental Python programming constructs, including control flow (loops), mathematical logic (factorials), and comprehensive string manipulation techniques.

Algorithm:
Step1: Start
Step2: Looping Operations:
         While Loop: Initialize a counter; while the counter is less than or equal to a limit, print the value and increment.
         For Loop: Iterate through a predefined list (e.g., fruits) and print each element.
Step3: Mathematical Logic (Factorial):
         Initialize factorial = 1.
         Loop from 1 to the target number n.
         Multiply factorial by the current loop index in each step.
Step4: String Reversal & Analysis:
         Reverse: Use slicing [::-1] to flip the string.
         Count: Use the built-in len() function to get the total characters.
         Palindrome: Check if the original string is identical to its reversed version.
Step5: Case Transformation:
         Apply upper() for all caps and lower() for all small letters.
         Apply capitalize() for the first letter and swapcase() to invert all existing cases.
Step6: Search & Filtering:
        Substring: Use find() to locate the starting index of a specific word or character.
        Vowels: Iterate through the string and increment a counter if a character exists in the set {a, e, i, o, u}.
Step7: Output: Display all calculated and transformed results to the console.
Step8: End
                                               
Source code:
# --- Loops ---
# While Loop: Counting to 5
print("While Loop:")
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1
print("\n")

# For Loop: Iterating through a list
print("For Loop:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
print("-" * 20)

# --- Mathematical Logic ---
# Factorial of a number
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is: {factorial}")
print("-" * 20)

# --- String Manipulations ---
text = "Python Programming"

# Reverse String
reversed_text = text[::-1]
print(f"Reverse: {reversed_text}")

# Count String (Length)
print(f"Length of string: {len(text)}")

# Palindrome Check
word = "radar"
is_palindrome = word == word[::-1]
print(f"Is '{word}' a palindrome?: {is_palindrome}")

# Case Conversions
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Capitalize: {'hello world'.capitalize()}") # First letter only
print(f"Swapcase: {text.swapcase()}") # Flips upper to lower and vice versa

# Find Substring
position = text.find("gram")
print(f"Index of 'gram': {position}")

# Count Vowels
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text if char in vowels)
print(f"Number of vowels in '{text}': {vowel_count}")

Output:
While Loop:
1 2 3 4 5 

For Loop:
I like apple
I like banana
I like cherry

Factorial of 5 is: 120

Reverse: gnimmargorP nohtyP
Length of string: 18
Is 'radar' a palindrome?: True
Uppercase: PYTHON PROGRAMMING
Lowercase: python programming
Capitalize: Hello world
Swapcase: pYTHON pROGRAMMING
Index of 'gram': 10
Number of vowels in 'Python Programming': 4
