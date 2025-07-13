import unittest

from src.domain.assigment import Assignment
from src.domain.grade import Grade
from src.domain.student import Student
from src.repository.repository import MemoRepoStudent, MemoRepoAssignment
from src.services.services import Services


class TestDomain(unittest.TestCase):

    def test_student(self):
        student = Student("Maria Popescu", 911)
        self.assertEqual(student.student_id, None, "There should be no id")

        # test setter + getter id
        student.id = 13
        self.assertEqual(student.id, 13, "The ids arent the same")

        # test setter + getter name
        self.assertEqual(student.name, "Maria Popescu", "The names arent the same")
        student.day = "Amalia Bahrim"
        self.assertEqual(student.day, "Amalia Bahrim", "The names arent the same")

        # test setter + getter group
        self.assertEqual(student.group, 911, "The groups arent the same")
        student.group = 916
        self.assertEqual(student.group, 916, "The groups arent the same")

    def test_assignment(self):
        assignment = Assignment("Calculati a+b", 1)
        self.assertEqual(assignment.assignment_id, None, "There should be no id")

        # test setter + getter id
        assignment.id = 13
        self.assertEqual(assignment.id, 13, "The ids arent the same")

        # test setter + getter description
        self.assertEqual(assignment.description, "Calculati a+b", "The descriptions arent the same")
        assignment.description = "Calculati (a+b)^2"
        self.assertEqual(assignment.description, "Calculati (a+b)^2", "The descriptions arent the same")

        # test setter + getter deadline
        self.assertEqual(assignment.deadline, 1, "The deadlines arent the same")
        assignment.deadline = 2
        self.assertEqual(assignment.deadline, 2, "The deadlines arent the same")

    def test_grade(self):
        grade = Grade(14, 13, 8)

        # test setter + getter assignment id
        self.assertEqual(grade.assignment_id, 14, "The assignment ids arent the same")
        grade.assignment_id = 5
        self.assertEqual(grade.assignment_id, 5, "The assignment ids arent the same")

        # test setter + getter student id
        self.assertEqual(grade.student_id, 13, "The student ids arent the same")
        grade.student_id = 45
        self.assertEqual(grade.student_id, 45, "The student ids arent the same")

        # test setter + getter grade value
        self.assertEqual(grade.grade_value, 8, "The grades arent the same")
        grade.grade_value = 6
        self.assertEqual(grade.grade_value, 6, "The grades arent the same")


class TestRepo(unittest.TestCase):
    def test_student_repo(self):
        student_repo = MemoRepoStudent()

        self.assertEqual(len(student_repo.list_student()), 20, "The length should be 20!")

        # adding a new student
        student = Student("melania", "211")
        student_repo.add_student(student)

        self.assertEqual(len(student_repo.list_student()), 21, "The length should be 21!")
        self.assertEqual(student_repo.list_student().get(20), student, "The students should be equal!")

        # removing the last student
        student_repo.remove_student(20)
        self.assertEqual(len(student_repo.list_student()), 20, "The length should be 20!")

        # updating the first student
        new_student = Student("melania", 911)
        new_student.student_id = 0
        student_repo.update_student(new_student)

        student_list = student_repo.list_student()
        self.assertEqual(student_list.get(0), new_student, "The students should be equal!")

    def test_assignment_repo(self):
        assignment_repo = MemoRepoAssignment()

        self.assertEqual(len(assignment_repo.list_assignment()), 20, "The length should be 20!")

        # adding a new assignment
        assignment = Assignment("melania", 2)
        assignment_repo.add_assignment(assignment)

        self.assertEqual(len(assignment_repo.list_assignment()), 21, "The length should be 21!")
        self.assertEqual(assignment_repo.list_assignment().get(20), assignment, "The assignments should be equal!")

        # removing the last assignment
        assignment_repo.remove_assignment(20)
        self.assertEqual(len(assignment_repo.list_assignment()), 20, "The length should be 20!")

        # updating the first assignment
        new_assignment = Assignment("melania2", 1)
        new_assignment.assignment_id = 0
        assignment_repo.update_assignment(new_assignment)

        assignment_list = assignment_repo.list_assignment()
        self.assertEqual(assignment_list.get(0), new_assignment, "The assignments should be equal!")


class TestService(unittest.TestCase):
    def test_first_functionality(self):
        service = Services()

        # add a new student
        student_added = Student("melania", 911)
        student_added.student_id = 20

        service.add_student("melania", 911)
        self.assertEqual(len(service.list_student()), 21, "The length should be 21!")
        self.assertEqual(service.list_student().get(20), student_added, "The students should be equal!")

        # update a student
        new_student = Student("melania2", 912)
        new_student.student_id = 20

        service.update_student(new_student)
        self.assertEqual(service.list_student().get(20), new_student, "The students should be equal!")

        # removing a student
        service.remove_student(20)
        self.assertEqual(len(service.list_student()), 20, "The length should be 20!")

        # add a new assignment
        assignment_added = Assignment("melania", 2)
        assignment_added.assignment_id = 20

        service.add_assignment("melania", 2)
        self.assertEqual(len(service.list_assignment()), 21, "The length should be 21!")
        self.assertEqual(service.list_assignment().get(20), assignment_added, "The assignments should be equal!")

        # updating an assignment
        new_assignment = Assignment("melania2", 4)
        new_assignment.assignment_id = 20

        service.update_assignment(new_assignment)
        self.assertEqual(service.list_assignment().get(20), new_assignment, "The assignments should be equal!")

        # removing an assignment
        service.remove_assignment(20)
        self.assertEqual(len(service.list_assignment()), 20, "The length should be 20!")

    def test_undo_redo(self):
        service = Services()

        # add a new student, a new assignment and a new grade
        service.add_student("melania", 911)
        service.add_assignment("melania", 2)
        service.assign(21, 21)
        service.grade_assignment(21, 21, 10)

        # undo the last operation
        service.undo()

        # check if the grade was ungraded (-1 as grade value)
        self.assertEqual(service.list_grade()[-1].grade_value, -1, "The grade should be -1!")

        # redo the last operation
        service.redo()

        # check if the grade was graded (10 as grade value)
        self.assertEqual(service.list_grade()[-1].grade_value, 10, "The grade should be 10!")

        # remove the student
        service.remove_student(21)

        # assert that the grades are removed
        self.assertEqual(len(service.list_grade()), 20, "The length should be 20!")

        # undo the last operation
        service.undo()

        # assert that the grades are restored
        self.assertEqual(len(service.list_grade()), 21, "The length should be 21!")

        # redo the last operation
        service.redo()

        # assert that the grades are removed
        self.assertEqual(len(service.list_grade()), 20, "The length should be 20!")


if __name__ == "__main__":
    unittest.main()