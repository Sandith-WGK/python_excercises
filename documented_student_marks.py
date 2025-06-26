"""
Student Marks Analysis System

This program reads student marks from a CSV file and performs the following analysis:
1. Calculates total marks for each student across all subjects
2. Finds the overall top student
3. Finds the top student in each subject

File format expected:
Name,Subject,Marks
Alice,Math,85
Bob,Science,90
...

Author: [Kulitha]
Date: [26/06/2025]
"""

def get_top_student(subject: str, dataset: dict) -> tuple:
    """
    Find the student with the highest marks in a given subject.
    
    Args:
        subject (str): The subject name (used for context, not in calculation)
        dataset (dict): Dictionary with student names as keys and marks as values
                       Example: {'Alice': 85, 'Bob': 90, 'Charlie': 78}
    
    Returns:
        tuple: (highest_marks, student_name)
               Example: (90, 'Bob')
    
    Note: If dataset is empty, returns (0, None)
    """
    max_mark = 0
    m_name = None

    # Iterate through all students and their marks in this subject
    for name, mark in dataset.items():
        if mark > max_mark:
            max_mark = mark
            m_name = name

    return max_mark, m_name        


def get_marks(record: tuple) -> int:
    """
    Extract marks from a (name, marks) tuple for sorting purposes.
    
    Args:
        record (tuple): A tuple containing (student_name, total_marks)
                       Example: ('Alice', 255)
    
    Returns:
        int: The marks value (second element of the tuple)
             Example: 255
    
    This function is used as a key function for sorting student records by marks.
    """
    return record[1]


# ===== MAIN PROGRAM =====

# Step 1: Read the file
lines = None

try:
    with open('info.txt', 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("Error: 'info.txt' file not found!")
    exit()
except Exception as e:
    print(f"Error reading file: {e}")
    exit()

# Step 2: Validate file content
if not lines:
    print("Something went wrong, file is empty")
    exit()

# Skip the header line (assumed to be "Name,Subject,Marks")
marks_lines = lines[1:]

if not marks_lines:
    print("No data found in file (only header present)")
    exit()

# Step 3: Initialize data structures
# subject_marks: nested dict to store marks by subject and student
# Structure: {'Math': {'Alice': 85, 'Bob': 90}, 'Science': {'Alice': 78}}
subject_marks = {}

# student_marks: dict to store total marks for each student across all subjects
# Structure: {'Alice': 255, 'Bob': 175, 'Charlie': 88}
student_marks = {}

# Step 4: Process each line of student data
print("Processing student marks data...")

for line_num, line in enumerate(marks_lines, start=2):  # start=2 because we skipped header
    try:
        # Parse the CSV line
        entries = line.split(',')
        
        # Validate line format
        if len(entries) != 3:
            print(f"Warning: Skipping malformed line {line_num}: {line.strip()}")
            continue
            
        name = entries[0].strip()
        subject = entries[1].strip()
        marks = int(entries[2].strip())
        
        # Validate data
        if not name or not subject:
            print(f"Warning: Skipping line {line_num} with empty name/subject")
            continue
            
        if marks < 0:
            print(f"Warning: Negative marks ({marks}) for {name} in {subject}")
        
        # Step 4a: Calculate total marks for each student
        # Get student's previous total marks (0 if student is new)
        prev_marks = student_marks.get(name, 0)
        # Add current subject marks to student's total
        student_marks[name] = prev_marks + marks

        # Step 4b: Organize marks by subject
        # Create subject entry if it doesn't exist
        if subject not in subject_marks:
            subject_marks[subject] = {}
        
        # Store this student's marks for this subject
        subject_marks[subject][name] = marks
        
    except ValueError:
        print(f"Warning: Invalid marks value on line {line_num}: {line.strip()}")
        continue
    except Exception as e:
        print(f"Error processing line {line_num}: {e}")
        continue

# Step 5: Find overall top student
print("\n" + "="*50)
print("OVERALL TOP STUDENT ANALYSIS")
print("="*50)

# Convert student_marks dict to list of tuples for sorting
# Format: [(name, total_marks), (name, total_marks), ...]
marks_list = [(name, marks) for name, marks in student_marks.items()]

# Sort by total marks in descending order (highest first)
marks_list.sort(key=get_marks, reverse=True)

# Get the top student (first element after sorting)
if marks_list:
    top_student = marks_list[0]
    print(f"Top student is {top_student[0]} with {top_student[1]} marks.")
    
    # Show top 3 students if available
    print("\nTop students ranking:")
    for i, (name, total_marks) in enumerate(marks_list[:3], 1):
        print(f"  {i}. {name}: {total_marks} marks")
else:
    print("No student data found!")

# Step 6: Find top student in each subject
print("\n" + "="*50)
print("SUBJECT-WISE TOP STUDENTS")
print("="*50)

for subject, dataset in subject_marks.items():
    # Find the top student in this subject
    max_marks, top_name = get_top_student(subject, dataset)
    
    # Display the result
    msg = f"{subject} max mark is {max_marks} and got by {top_name}."
    print(msg)

# Step 7: Additional statistics (bonus information)
print("\n" + "="*50)
print("SUMMARY STATISTICS")
print("="*50)

total_students = len(student_marks)
total_subjects = len(subject_marks)
total_records = sum(len(subject_data) for subject_data in subject_marks.values())

print(f"Total students: {total_students}")
print(f"Total subjects: {total_subjects}")
print(f"Total records processed: {total_records}")

if student_marks:
    avg_total_marks = sum(student_marks.values()) / len(student_marks)
    print(f"Average total marks per student: {avg_total_marks:.2f}")

print("\nProcessing completed successfully!")
