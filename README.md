# CODTECH-TASK2

Name:- P.Lokeswar

Company:-CODTECH IT SOLUTIONS

ID:-CT04DS7476

Domain:- Python Programming

Duration:-August to September 2024

Mentor:-Neela Santhosh Kumar

### Overview of the Python Program:

This program is designed to manage and track student grades by allowing the user to input grades for various subjects or assignments. It calculates the average grade, converts numeric grades to letter grades and GPA, and displays individual and overall grade summaries.

### Key Components:

1. **Helper Functions:**
   - `get_letter_grade(grade)`: Converts a numeric grade into a letter grade based on standard grading scale:
     - 90+ = A
     - 80–89 = B
     - 70–79 = C
     - 60–69 = D
     - Below 60 = F
   - `get_gpa(grade)`: Converts a numeric grade into GPA based on the 4.0 scale:
     - 90+ = 4.0
     - 80–89 = 3.0
     - 70–79 = 2.0
     - 60–69 = 1.0
     - Below 60 = 0.0
   - `calculate_average(grades)`: Calculates the average of all grades provided.

2. **Main Function (`manage_student_grades`)**:
   - **Input Loop**: The program prompts the user to input subjects and corresponding grades. The loop continues until the user types `'done'`.
     - Each grade input is validated to ensure it's a valid number between 0 and 100.
   - **Grade Storage**: Grades for each subject are stored in a dictionary (`subjects`), where the subject name is the key and the grade is the value.
   
3. **Grade Calculation and Display**:
   - **Grade Summary**: Once all grades are entered, the program calculates the average grade across subjects.
   - **Individual Subject Grades**: For each subject, the program displays the numeric grade, corresponding letter grade, and GPA.
   - **Overall Summary**: The program calculates and displays the average numeric grade, overall letter grade, and overall GPA.

4. **Program Execution**:
   - The program is run by calling `manage_student_grades()`. It handles user input, calculations, and displays the results.
  
     

![Screenshot 2024-09-09 193514](https://github.com/user-attachments/assets/7773a592-48c6-4bbf-83f0-0d76b8a0f12b)
