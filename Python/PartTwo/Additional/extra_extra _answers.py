"""
EXTRA EXTRA:
Part 1:
Create Classroom Data
Create a nested dictionary called classrooms that contains information about two classrooms:
•	Classroom 1:
o	Class Name: "Math101"
o	Students: List of dictionaries, where each dictionary represents a student with the keys: "name", "age", and "grade"
	Student 1: Name - "Alice", Age - 18, Grade - 95
	Student 2: Name - "Bob", Age - 17, Grade – 85

Classroom 2:
•	Class Name: "History101"
•	Students: List of dictionaries, similar to Classroom 1
o	Student 1: Name - "Eve", Age - 18, Grade - 78
o	Student 2: Name - "Charlie", Age - 17, Grade – 92
"""
classrooms = {
    "Math101": {
        "students": [
            {"name": "Alice", "age": 18, "grade": 95},
            {"name": "Bob", "age": 17, "grade": 85},
        ]
    },
    "History101": {
        "students": [
            {"name": "Eve", "age": 18, "grade": 78},
            {"name": "Charlie", "age": 17, "grade": 92},
        ]
    },
}
"""
Part 2: 
Add Student
Add a new student to "Math101":
Student 3: Name - "David", Age - 16, Grade – 88
"""
new_student = {"name": "David", "age": 16, "grade": 88}
classrooms["Math101"]["students"].append(new_student)

"""
Task 3: Update Grade
Update the grade of "Alice" in "Math101" to 98.
"""
classrooms["Math101"]["students"][0]["grade"] = 98

"""
Part 4: Access and Print Information
Print out the age of "Eve" in "History101" using nested dictionary access.
"""
eve_age = classrooms["History101"]["students"][0]["age"]
print("Age of Eve in History101:", eve_age)


"""
Part 5: Calculate Average Grade
Calculate and print the average grade for "History101" using only the given data, without loops or libraries.
"""
history_grades = classrooms["History101"]["students"]
average_grade = (history_grades[0]["grade"] + history_grades[1]["grade"]) / 2
print("Average Grade for History101:", average_grade)