Aim:
To implement a functional phonebook application using a Python Dictionary to demonstrate key-value mapping, efficient data retrieval, and the implementation of a menu-driven interface using control flow (while, if-elif-else).

Algorithm:
Step1: Start
Step2: Initialize: Create a dictionary phonebook with predefined contacts.
Step3: Menu Display: Enter an infinite while loop to show options for viewing, adding, searching, deleting, and exiting.
Step4: View (Read): Use a for loop with the .items() method to iterate through and display all key-value pairs.
Step5: Add/Update (Write): Take user input for a name and number. Use the syntax phonebook[name] = number to either create a new entry or update an existing one.
Step6: Search (Query):
        Take user input for a name.
        Use the in operator to check if the key exists in the dictionary.
        If found, print the value associated with that key.         
Step7: Delete (Remove):
        Check if the name exists.
        If true, use the .pop() method to remove the entry from the dictionary.
Step8: Exit: Use the break statement to terminate the loop when the user chooses the exit option.
Step9: End.

Source code:
# 1. Initialize the Phonebook (Dictionary)
# Keys are Names (Strings), Values are Phone Numbers (Strings/Ints)
phonebook = {
    "Vansitha": "9876543210",
    "Amit": "9123456789",
    "Sneha": "8887776665"
}
# 2. Main Menu Loop
while True:
    print("\n--- PHONEBOOK MENU ---")
    print("1. View All Contacts")
    print("2. Add/Update Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        # Operation: Iteration
        print("\n--- All Contacts ---")
        if not phonebook:
            print("Phonebook is empty.")
        for name, number in phonebook.items():
            print(f"Name: {name:<10} | Number: {number}")
    elif choice == '2':
        # Operation: Adding/Updating
        name = input("Enter Name: ")
        number = input("Enter Number: ")
        phonebook[name] = number
        print(f"Contact {name} saved successfully.")
    elif choice == '3':
        # Operation: Searching (Membership Test)
        name = input("Enter Name to search: ")
        if name in phonebook:
            print(f"Found: {name}'s number is {phonebook[name]}")
        else:
            print("Contact not found.")
    elif choice == '4':
        # Operation: Removal
        name = input("Enter Name to delete: ")
        if name in phonebook:
            # Using .pop() or del
            phonebook.pop(name)
            print(f"Contact {name} deleted.")
        else:
            print("Name not found in phonebook.")
    elif choice == '5':
        print("Exiting Phonebook. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

Output:
--- PHONEBOOK MENU ---
1. View All Contacts
2. Add/Update Contact
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 1

--- All Contacts ---
Name: Vansitha   | Number: 9876543210
Name: Amit       | Number: 9123456789
Name: Sneha      | Number: 8887776665   
