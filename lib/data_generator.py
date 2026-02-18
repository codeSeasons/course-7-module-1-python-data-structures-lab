# This module contains functions to lazily generate student data.

def student_generator(student_list, major):
    """
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator.
    """

    major_clean = major.strip().lower()

    return (
        student
        for student in student_list
        if student[2].strip().lower() == major_clean
    )