Aim:
To write a Python program to verify different arithmetic and bitwise identities using operators such as addition (+), and subtraction (-), OR (|), AND (&), XOR (^) and prove them by comparing the Left Hand Side (LHS) and Right Hand Side (RHS).

Algorithm:
Step1: Start the program.
Step2: Take two integer inputs a and b from the user.
Step3: Calculate the Left Hand Side (LHS) of the identity.
Step4: Calculate the Right Hand Side (RHS) of the identity.
Step5: Compare LHS and RHS using the equality operator ==.
Step6: Print whether the identity is True (Proved) or False.
Step7: Repeat the above steps for different identities.
Step8: End the program.

Source code:
# Verification of Bitwise Identities
print("Bitwise OR Identity")

# 1st Identity
a = int(input("Enter the Value: "))
b = int(input("Enter the Value: "))
LHS = a | b
RHS = (a & b) + (a ^ b)
print("Proved:", LHS == RHS)

# 2nd Identity
a = int(input("Enter the Value: "))
b = int(input("Enter the Value: "))
LHS = a ^ (a & b)
RHS = (a | b) ^ a
print("Proved:", LHS == RHS)

# 3rd Identity
a = int(input("Enter the Value: "))
b = int(input("Enter the Value: "))
LHS = b ^ (a & b)
RHS = (a | b) ^ a
print("Proved:", LHS == RHS)

# 4th Identity
a = int(input("Enter the Value: "))
b = int(input("Enter the Value: "))
LHS = (a & b) ^ (a | b)
RHS = a ^ b
print("Proved:", LHS == RHS)

# Addition Identity
a = int(input("Enter the Value: "))
b = int(input("Enter the Value: "))
LHS = a + b
RHS = (a ^ b) + 2 * (a & b)
print("Proved:", LHS == RHS)

# Subtraction Identity
a = int(input("Enter Value1: "))
b = int(input("Enter Value2: "))
LHS = a - b
RHS = (a ^ (a & b)) - ((a | b) ^ a)
print("Proved:", LHS == RHS)

#2
a = int(input("Enter Value1: "))
b = int(input("Enter Value2: "))
LHS = a - b
RHS = ((a | b) ^ b) - ((a | b) ^ a)
print("Proved:", LHS == RHS)

#3
a = int(input("Enter Value1: "))
b = int(input("Enter Value2: "))
LHS = a - b
RHS = (a ^ (a & b)) - (b ^ (a & b))
print("Proved:", LHS == RHS)

#4
a = int(input("Enter Value1: "))
b = int(input("Enter Value2: "))
LHS = a - b
RHS = ((a | b) ^ b) - (b ^ (a & b))
print("Proved:", LHS == RHS)

# Verification of Arithmetic Identities
# Identity 1
a = int(input("Enter the value: "))
b = int(input("Enter the value: "))
LHS = (a + b) * (a + b)
RHS = (a * a) + (2 * a * b) + (b * b)
print("Proved:", LHS == RHS)

# Identity 2
a = int(input("Enter the value: "))
b = int(input("Enter the value: "))
LHS = (a - b) * (a - b)
RHS = (a * a) - (2 * a * b) + (b * b)
print("Proved:", LHS == RHS)

# Identity 3
a = int(input("Enter the value: "))
b = int(input("Enter the value: "))
LHS = (a + b) * (a - b)
RHS = (a * a) - (b * b)
print("Proved:", LHS == RHS)

# Identity 4
a = int(input("Enter the value: "))
b = int(input("Enter the value: "))
LHS = (a + b) * (a + b)
RHS = (a * a) + (2 * a * b) + (b * b)
print("Proved:", LHS == RHS)

# Identity 5
a = int(input("Enter the value: "))
b = int(input("Enter the value: "))
LHS = (a * a * a) + (b * b * b)
RHS = (a + b) * (a * a - a * b + b * b)
print("Proved:", LHS == RHS)

Output:
Enter the Value: 5
Enter the Value: 3
Proved: True

Enter the Value: 6
Enter the Value: 2
Proved: True

Enter the Value: 4
Enter the Value: 1
Proved: True

Enter the Value: 7
Enter the Value: 3
Proved: True

Enter the Value: 5
Enter the Value: 4
Proved: True

Enter Value1: 8
Enter Value2: 3
Proved: True

Enter Value1: 10
Enter Value2: 6
Proved: True

Enter Value1: 9
Enter Value2: 2
Proved: True

Enter Value1: 12
Enter Value2: 5
Proved: True

Enter the value: 3
Enter the value: 2
Proved: True

Enter the value: 5
Enter the value: 1
Proved: True

Enter the value: 6
Enter the value: 2
Proved: True

Enter the value: 4
Enter the value: 3
Proved: True

Enter the value: 2
Enter the value: 1
Proved: True
