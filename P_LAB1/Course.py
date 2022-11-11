from __future__ import annotations

from typing import Dict, List, TYPE_CHECKING

from datetime import datetime, date

if TYPE_CHECKING:

    from Staff import Student, Professor


class CourseProgress:
    """Progress of the course.
    Args:
        received_marks (dict): marks received student.
        visited_lectures (int): Count of lectures student have visited.
        completed_assignments (dict): completed assignments.
        notes (dict): student notes.
    Methods:
        get_progress_to_date(date: datetime)
           Returns marks.

        get_final_mark()
            Returns total mark.

        fill_notes(note: str)
            Adding notes.

        remove_note(date: datetime)
            Removing notes.
    """

    def __init__(self, received_marks: dict, visited_lectures: int,
                 completed_assignments: dict, notes: dict):
        self.received_marks = received_marks
        self.visited_lectures = visited_lectures
        self.completed_assignments = completed_assignments
        self.notes = notes

    def get_progress_to_date(self, date: datetime) -> str:
        """Returning marks of the student
        Args:
            date (datetime): date due to which we want to take marks.
        Returns:
            Dictionary "marks" with structure: "task": "mark".
        """
        marks = []
        for k, x in self.completed_assignments.items():
            if k < date:
                marks.append(x["mark"])
        return marks

    def get_final_mark(self) -> float:
        """Returning final mark

        Returns:
            Arithmetic result of student for this course.

        """
        values = self.received_marks.values()
        amounts_of_marks = self.received_marks
        return sum(values) / len(amounts_of_marks)

    def fill_notes(self, note: str) -> None:
        """Adding note
        Args:
            note (str): note to add.
        Returns:
            Noth.
        """
        today_date = date.today()
        self.notes[today_date] = note

    def remove_note(self, date: date) -> None:
        """Deleting notes by the date.
        Args:
            date (date): date of the note to delete.
        Returns:
            Noth.
        """
        del self.notes[date]


class Course:
    """Represents course.
    Args:
        title (str): Course title,
        start_date (datetime): course start date.
        end_date (datetime): course end date.
        description (str): course descriptions.
        lectures (list[str]): lectures list.
        assignments (list[str]): assignments list.
        limit (int): limit of students.
        students_list (list[int]): list of students.
    Methods:
        add_student(student: Student)
            Calling from Student enroll method.
        remove_student(student: Student)
            Calling unenroll method from Student.
    """
    def __init__(self, title: str, start_date: datetime, end_date: datetime,
                 description: str, lectures: list[str], assignments: list[str],
                 limit: int, students_list: list[int]):
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.lectures = lectures
        self.assignments = assignments
        self.limit = limit
        self.students_list = students_list

    def add_student(self, student: Student) -> None:
        """Adding student to the Course
        Args:
             student (Student): class Student.
        Returns:
            Noth.
        """
        try:
            student.enroll(course=self)
        except ValueError:
            print(
                f"Student id: {student.student_id} has already enrolled to {self.title}.")

    def remove_student(self, student: Student) -> None:
        """Removing student from the Course
        Args:
            student (Student): class Student.
        Returns:
            Noth.
        """
        try:
            student.unenroll(course=self)
        except ValueError:
            print(
                f"Student id: {student.student_id} has already unenrolled to {self.title}.")