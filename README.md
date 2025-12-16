# Assignment-5
Tutedude
1. Demonstrate list slicing - 


    Step 1: Creating a list of numbers from 1 to 10
    numbers = list(range(1, 11))
    
    
    The range(1, 11) function generates numbers starting from 1 up to 10 (11 is excluded).
    
    The list() function converts these numbers into a list.
    
    As a result, the numbers list contains values from 1 to 10.
    
    Step 2: Extracting the first five elements
    first_five = numbers[:5]
    
    
    This uses list slicing.
    
    [:5] means elements from index 0 to index 4.
    
    The first five elements of the list are extracted and stored in first_five.
    
    Step 3: Reversing the extracted elements
    reversed_first_five = first_five[::-1]
    
    
    [::-1] reverses the order of the list.
    
    The extracted list is reversed and stored in reversed_first_five.
    
    Step 4: Printing the results
    print("Original list:", numbers)
    print("Extracted first five elements:", first_five)
    print("Reversed extracted elements:", reversed_first_five)
    
    
    These statements print:
    
    The original list
    
    The extracted first five elements
    
    The reversed version of the extracted elements




2. Create a Dict of Student marks --


    Step 1: Creating a dictionary
    student_marks = {"Alice": 85, "Rohan": 90, "Sonam": 78, "David": 92}
    
    
    A dictionary named student_marks is created.
    
    The keys are student names.
    
    The values are their corresponding marks.
    
    This allows marks to be accessed easily using a student’s name.
    
    Step 2: Taking input from the user
    name = input("Enter the student's name: ")
    
    
    The program asks the user to enter a student’s name.
    
    The entered name is stored in the variable name.
    
    Step 3: Checking if the student exists in the dictionary
    if name in student_marks:
    
    
    This line checks whether the entered name exists as a key in the dictionary.
    
    If the name is found, the condition becomes True.
    
    Step 4: Displaying the result
    print(f"{name}'s marks: {student_marks[name]}")
    
    
    If the student exists, their marks are fetched using the key.
    
    The marks are displayed using an f-string for proper formatting.
    
    Step 5: Handling the case when the student is not found
    else:
        print("Student not found.")
    
    
    If the entered name does not exist in the dictionary, this message is printed
