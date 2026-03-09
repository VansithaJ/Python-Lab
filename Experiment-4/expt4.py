Aim:
To implement a Python program that manages and manipulates list data sourced from a 5G connectivity blog, demonstrating core list operations including slicing, modification (append, extend, replace), removal, searching, concatenation, and traversal using both for and while loops.

Algorithm:
Step1: Start
Step2: Initialize Data Structures:
        Create a list named Content containing 11 network capability strings (e.g., "5G", "10-100 times", "Reliability").
        Create a list named Info containing 9 industry application strings (e.g., "robotic surgery", "smart factories").
Step3: Verify Input: Print both lists to ensure data integrity.
Step4: Perform Slicing:
        Extract the first five elements of Content using Content[0:5].
        Extract the first three elements of Info using Info[0:3].
Step5: Modify Lists (Addition/Update):
        Use .append() to add "Manufacturing" to the end of the Content list.
        Update the element at index 7 of Info by assigning it the string "and".
        Use .extend() to add a new list ["delivering upto 20 Gbps"] to the Info list.
Step6: Remove Data:
        Check if "Consistent Connections" exists in Content using the in operator.
        If present, remove it using the .remove() method.
Step7: Search and Access:
        Access the element at index 10 of Content directly.
        Find and store the index of the keyword "5G" using the .index() method.
Step8: Combine Data:
        Create a new list combined_data by concatenating Content and Info using the + operator.
Step9: Iterate and Display:
        Determine the length of the Info list using len() and store it in variable k.
        For Loop: Traverse the Info list and print each element directly.
        While Loop: Initialize a counter i = 0. While i < k, print the element at Info[i] and increment i by 1.
Step10: End.

Source code:
# List 1: Network Capabilities (12 elements)
Content = [
    "5G", "Upto 10 Gbps", "ultra-low latency", "10-100 times", 
    "faster than 4G", "low as 1ms", "massive network capacity", 
    "increased capacity & density", "stable", "Consistent Connections", 
    "Reliability"
]
# List 2: Industry Applications (13 elements)
Info = [
    "advanced infrastructure", "utility meters", "remote", 
    "real-time diagnostics", "robotic surgery", "high-definition", 
    "lag-free VR/AR", "automation", "smart factories"
]

# 1. Verification of data entry
print("Initial Network Capabilities (Content list):")
print(Content)
print("\nInitial Industry Applications (Info list):")
print(Info)
print("-" * 30)

# 2. Slicing Operations
print(f"Top 5 Capabilities (Slice [0:5]): {Content[0:5]}")
print(f"Key Use Cases (Slice [0:3]): {Info[0:3]}")
print("-" * 30)

# 3. Modification (Appending)
Content.append("Manufacturing")
print("After appending a new application sector:")
print(Content)
print("-" * 30)

# 4. Modification (Value Replacement/Update)
print(f"Item at Index 7 before update: {Info[7]}")
Info[7] = "and"
print("After replacing element at index 7 with 'and':")
print(Info)
print("-" * 30)

# 5. Removal Operations
if "Consistent Connections" in Content:
    Content.remove("Consistent Connections")
    print("After removing 'Consistent Connections':")
    print(Content)
    print("-" * 30)

# 6. Modification (Extending a list)
new_specs = ["delivering upto 20 Gbps"]
Info.extend(new_specs)
print("After extending list with peak speed specifications:")
print(Info)
print("-" * 30)

# 7. Accessing & Searching
print(f"Accessing element at index 10: {Content[10]}")
L = Content.index("5G")
print(f"The index of '5G' keyword: {L}")
print("-" * 30)

# 8. Concatenation
combined_data = Content + Info
print("Combined Data (Concatenated Content and Info lists):")
print(combined_data)
print("-" * 30)

# 9. Measuring Length & Iteration
k = len(Info)
print(f"Total elements in Industry Applications list (Info): {k}")

# --- Loop Demonstrations ---
# A) For Loop (Iterating over elements)
print("\nIterating with 'for' loop (Displaying all Applications):")
for application_word in Info:
    print(application_word)

# B) While Loop (Iterating over indices)
print("\nIterating with 'while' loop (Index-based traversal):")
i = 0
while i < k:
    print(Info[i])
    i = i + 1 
print("\nOperations verified and complete.")

Output:
Initial Network Capabilities (Content list):
['5G', 'Upto 10 Gbps', 'ultra-low latency', '10-100 times', 'faster than 4G', 'low as 1ms', 'massive network capacity', 'increased capacity & density', 'stable', 'Consistent Connections', 'Reliability']

Initial Industry Applications (Info list):
['advanced infrastructure', 'utility meters', 'remote', 'real-time diagnostics', 'robotic surgery', 'high-definition', 'lag-free VR/AR', 'automation', 'smart factories']

Top 5 Capabilities (Slice [0:5]): ['5G', 'Upto 10 Gbps', 'ultra-low latency', '10-100 times', 'faster than 4G']
Key Use Cases (Slice [0:3]): ['advanced infrastructure', 'utility meters', 'remote']

After appending a new application sector:
['5G', 'Upto 10 Gbps', 'ultra-low latency', '10-100 times', 'faster than 4G', 'low as 1ms', 'massive network capacity', 'increased capacity & density', 'stable', 'Consistent Connections', 'Reliability', 'Manufacturing']

Item at Index 7 before update: automation
After replacing element at index 7 with 'and':
['advanced infrastructure', 'utility meters', 'remote', 'real-time diagnostics', 'robotic surgery', 'high-definition', 'lag-free VR/AR', 'and', 'smart factories']

After removing 'Consistent Connections':
['5G', 'Upto 10 Gbps', 'ultra-low latency', '10-100 times', 'faster than 4G', 'low as 1ms', 'massive network capacity', 'increased capacity & density', 'stable', 'Reliability', 'Manufacturing']

After extending list with peak speed specifications:
['advanced infrastructure', 'utility meters', 'remote', 'real-time diagnostics', 'robotic surgery', 'high-definition', 'lag-free VR/AR', 'and', 'smart factories', 'delivering upto 20 Gbps']

Accessing element at index 10: Manufacturing
The index of '5G' keyword: 0

Combined Data (Concatenated Content and Info lists):
['5G', 'Upto 10 Gbps', 'ultra-low latency', '10-100 times', 'faster than 4G', 'low as 1ms', 'massive network capacity', 'increased capacity & density', 'stable', 'Reliability', 'Manufacturing', 'advanced infrastructure', 'utility meters', 'remote', 'real-time diagnostics', 'robotic surgery', 'high-definition', 'lag-free VR/AR', 'and', 'smart factories', 'delivering upto 20 Gbps']

Total elements in Industry Applications list (Info): 10

Iterating with 'for' loop (Displaying all Applications):
advanced infrastructure
utility meters
remote
real-time diagnostics
robotic surgery
high-definition
lag-free VR/AR
and
smart factories
delivering upto 20 Gbps

Iterating with 'while' loop (Index-based traversal):
advanced infrastructure
utility meters
remote
real-time diagnostics
robotic surgery
high-definition
lag-free VR/AR
and
smart factories
delivering upto 20 Gbps

Operations verified and complete.
