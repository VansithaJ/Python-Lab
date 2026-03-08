Aim:
To implement an advanced data management script using immutable tuples, focusing on tuple unpacking, data categorization via conditional filtering, and structured tabular output for academic reporting.
                                                                                                                                                                                 
Algorithm:
Step1: Start
Step2: Initialize & Unpack: Create a student_profile tuple and immediately demonstrate Unpacking by assigning its values to individual variables (name, age, etc.).
Step3: Define Database: Create a nested tuple database containing records with four fields (Name, Age, Course, Score).
Step4: Process Performance:
        Initiate a for loop to traverse the database.
        Use an if/else statement to check the s_score.
        If the score is >= 50, assign "Pass"; otherwise, assign "Fail".                                                                                                                                                                                 
Step5: Analyze Collection:
        Use Slicing to extract a subset of the top 3 records.
        Use len() to verify the total count of student records.
Step6: Construct Export Sheet:
        Define a sheet tuple that pulls data both from variables and specific indices of the database (e.g., database[2][0]).
Step7: Formatted Rendering:
        Loop through the sheet and use F-string padding (:<15) to create a perfectly aligned table with borders.
Step8: End
                                                                                                                                                                                 
Source code:
# 1. Tuple Creation
student_profile = ("Vansitha", 19, "BCA", "A+")
name, age, course, grade = student_profile 
print(f"Profile Loaded: {name} | Course: {course} | Grade: {grade}")
# 2. Collection of Students (Tuple of Tuples)
database = (
    ("Amit", 20, "BCA", 85),
    ("Rahul", 21, "BBA", 42),
    ("Sneha", 19, "BCA", 92),
    ("Priya", 22, "BSc", 78),
    ("Karan", 20, "BBA", 35)
)
# 3. Data Processing with IF and FOR
print("\n--- Performance Report ---")
for student in database:
    s_name, s_age, s_course, s_score = student
    # Conditional logic to determine status
    if s_score >= 50:
        status = "Pass"
    else:
        status = "Fail"
    print(f"Student: {s_name:<8} | Score: {s_score} | Status: {status}")
# 4. Tuple Operations (Slicing & Searching)
top_performers = database[0:3] # Slicing top 3
print(f"\nTotal Records in Database: {len(database)}")
print(f"Is Sneha in Database?: {'Sneha' in [s[0] for s in database]}")
# 5. The "Excel" Sheet
sheet = (
    ("Student Name", "Course", "Final Result"),
    (name, course, "Cleared"),
    (database[2][0], database[2][2], "Distinction"), # Accessing nested elements
    (database[4][0], database[4][2], "Pending")
)
print("\nFinal Export Table:")
print("-" * 40)
for row in sheet:
    print(f"| {row[0]:<15} | {row[1]:<10} | {row[2]:<12} |")
print("-" * 40)
