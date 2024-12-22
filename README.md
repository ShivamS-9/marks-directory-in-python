# Marks Directory - Faculty Management System

## Overview
This Python program is designed to maintain a **Marks Directory** for faculty, allowing the management of student records, including personal details, course information, and exam results. It supports adding, loading from CSV files, displaying, updating, removing, and searching for student entries.

### Features:
1. **Add New Entry**: Add student records with details like First Name, Last Name, Roll Number, Course Name, Semester, Exam Type, Total Marks, and Scored Marks.
2. **Load Data from CSV**: Load student entries from a CSV file to populate the directory.
3. **Display Directory**: Display the entire marks directory in a table-like format using PrettyTable.
4. **Remove Entries**: Remove a student's entry based on specific criteria (Roll Number, Course, Semester, or Exam Type).
5. **Update Entries**: Update a student's record with new values.
6. **Search Entries**: Search for student records based on various attributes such as First Name, Last Name, Roll Number, Course Name, or Semester.

## Requirements:
- **Python 3.x**
- **prettytable**: Install this library using `pip install prettytable`.

## How to Use:

### 1. **Run the Program**:
   - To run the program, execute the Python script in your terminal.
   - The program will continuously ask for user input until the user chooses to exit.

### 2. **Options Menu**:
   The program offers the following choices for interacting with the Marks Directory:


### 3. **Adding New Entry**:
- Select `1` to add a new student's entry.
- You will be prompted to enter details like First Name, Last Name, Roll Number, Course Name, Semester, Exam Type, Total Marks, and Scored Marks.

### 4. **Load Data from CSV**:
- Select `2` to load student records from a CSV file.
- The CSV file must be in the same folder as the program.
- The file should contain columns: "First Name", "Last Name", "Roll Number", "Course Name", "Semester", "Exam Type", "Total Marks", and "Scored Marks".

### 5. **Display the Marks Directory**:
- Select `3` to display all the entries in a formatted table. 
- If there are no records, a message "No data" will be displayed.

### 6. **Remove an Entry**:
- Select `4` to remove an entry by Roll Number.
- You can also remove entries based on additional criteria like Course, Semester, or Exam Type.

### 7. **Update an Entry**:
- Select `5` to update a student's record.
- You will be asked to provide the Roll Number and the field you wish to update (e.g., Total Marks, Scored Marks).

### 8. **Search for an Entry**:
- Select `6` to search for a student based on specific attributes like First Name, Last Name, Roll Number, Course Name, or Semester.
- Enter the attribute value you wish to search for.

### 9. **Exit the Program**:
- Select `0` to exit the program.


**CSV File Format**:
Ensure the CSV file follows this structure:

```csv
First Name, Last Name, Roll Number, Course Name, Semester, Exam Type, Total Marks, Scored Marks
Sai, Anirudh, 20112153, Software Engineering, Monsoon2021, Assignment 1, 50, 35
Sachin, Tendulkar, 2015896, Intro to Database Systems, Spring2023, Class Test, 10, 9


