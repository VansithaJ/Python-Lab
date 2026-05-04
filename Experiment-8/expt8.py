Aim:
To implement the use of Regular Expressions (re module) in Python for pattern matching, searching, finding, substitution, splitting, and validation.

Algorithm:
Step1: Start
Step2: Import the re module.
Step3: Define a text string containing a phone number and email.
Step4: Use re.match() to check if the string starts with a given pattern.
Step5: Use re.search() to find a phone number in the string.
Step6: Use re.findall() to extract all digits from the string.
Step7: Use re.finditer() to find digits along with their positions.
Step8: Use re.sub() to replace digits with *.
Step9: Use re.split() to split the string based on spaces.
Step10: Take date input from the user.
Step11: Define a pattern for date format (dd/mm/yyyy).
Step12: Use re.fullmatch() to validate the date format.
Step13: Display whether the date is valid or invalid.

Source code:
import re
text = "My phone number is 9876543210 and email is test123@gmail.com"
match_result = re.match(r"my", text)
if match_result:
    print("Match found at beginning:", match_result.group())

search_result = re.search(r"\d{10}", text)
if search_result:
    print("Phone number found:", search_result.group())

findall_result = re.findall(r"\d", text)
print("All digits:", findall_result)
print("Digits using finditer:")
for match in re.finditer(r"\d", text):
    print(match.group(), "at position", match.start())
sub_result = re.sub(r"\d", "*", text)
print("After substitution:", sub_result)

split_result = re.split(r"\s", text)
print("Split by space:", split_result)

date = input("Enter date (dd/mm/yyyy): ")
pattern = r"^\d{2}/\d{2}/\d{4}$"

if re.fullmatch(pattern, date):
    print("Valid date format")
else:
    print("Invalid date format")
  
Output:
Phone number found: 9876543210
All digits: ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0', '1', '2', '3']
Digits using finditer:
9 at position 19
8 at position 20
7 at position 21
6 at position 22
5 at position 23
4 at position 24
3 at position 25
2 at position 26
1 at position 27
0 at position 28
1 at position 47
2 at position 48
3 at position 49
After substitution: My phone number is ********** and email is test***@gmail.com
Split by space: ['My', 'phone', 'number', 'is', '9876543210', 'and', 'email', 'is', 'test123@gmail.com']
Enter date (dd/mm/yyyy): 21/04/2026
Valid date format
