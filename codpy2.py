class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}  # Dictionary to store subjects and corresponding grades

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def calculate_average(self):
        total_grades = sum(self.grades.values())
        num_subjects = len(self.grades)
        return total_grades / num_subjects if num_subjects > 0 else 0

    def determine_letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def calculate_gpa(self, average):
        if average >= 90:
            return 4.0
        elif average >= 80:
            return 3.0
        elif average >= 70:
            return 2.0
        elif average >= 60:
            return 1.0
        else:
            return 0.0

    def display_summary(self):
        average = self.calculate_average()
        letter_grade = self.determine_letter_grade(average)
        gpa = self.calculate_gpa(average)

        print(f"\nStudent Name: {self.name}")
        print("Grades:")
        for subject, grade in self.grades.items():
            print(f"  {subject}: {grade}")
        print(f"Average Grade: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA: {gpa:.2f}")


def main():
    name = input("Enter the student's name: ")
    student = Student(name)

    while True:
        subject = input("\nEnter the subject ( type (done) if it reaches the no of subjects ): ")
        if subject.lower() == 'done':
            break

        try:
            grade = float(input(f"Enter the grade for {subject}: "))
            if grade < 0 or grade > 100:
                raise ValueError("Grade must be between 0 and 100.")
            student.add_grade(subject, grade)
        except ValueError as e:
            print(e)

    student.display_summary()


if __name__ == "__main__":
    main()
