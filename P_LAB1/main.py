import datetime

from Staff import Student, Professor
from Course import Course, CourseProgress

if __name__ == "__main__":
    """Testing of all methods from this lab work.
    F:
        Unenroll method: class Student.
        Remove student method: class Course.
    """
    test_student = Student("Test Student", "Addres, 1", "+380XXXXXXXX",
                           "testmail@lnu.edu.com", 1, 2.2, ["Subject", "id"])
    test_course = Course("Test Course", 2020 - 12 - 20, 2021 - 12 - 21,
                         "sum.", ["lecture_1"], [], 80, [])
    test_professor = Professor(
        "Test Professor", "Addres, 2", "+380XXXXXXXXX", "testmail2@lnu.edu.ua", 500)
    assignment_0 = {datetime.datetime(2020, 12, 20): {"title": "subject",
                                                    "is_done": True, "description": "sum.", "mark": 0}}
    test_course_progress = CourseProgress({}, 1, assignment_0, {})

    # Test of Student's methods
    print(test_student.taken_courses(self=test_student))
    test_student.enroll(test_course)
    print(test_student.taken_courses(self=test_student))
    test_student.unenroll(test_course)
    print(test_student.taken_courses(self=test_student))

    # Test of Professor's method
    print(f"\n{assignment_0}")
    test_professor.check_assignment(assignment_0, test_course_progress)
    print(f"{assignment_0}")

    # Test of CourseProgress.get_progress and final mark methods
    print(f"\n{test_course_progress.get_progress_to_date(datetime.datetime(2022, 12, 20))}")
    print(f"{test_course_progress.get_final_mark()}")

    # Test of CourseProgress.notes methods
    test_course_progress.fill_notes("Note test.")
    print(f"\n{test_course_progress.notes}")
    test_course_progress.remove_note(datetime.date(2022, 12, 20))
    print(f"{test_course_progress.notes}")

    # Test of Curse methods
    print(f"\n{test_course.students_list}")
    test_course.remove_student(test_student)
    print(f"{test_course.students_list}")
