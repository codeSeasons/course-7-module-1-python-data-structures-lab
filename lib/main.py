from student_data import students
from filters import filter_students_by_major
from data_processing import display_students
from data_generator import student_generator
'''
cs_students = filter_students_by_major(students, "computer science")
print(cs_students)
'''

display_students(students)

for student in student_generator(students, "Mathematics"):
    print(student)