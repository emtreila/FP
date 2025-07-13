import pickle
import random
import string

from src.domain.assigment import Assignment
from src.domain.grade import Grade
from src.domain.student import Student

class RepositoryError(Exception):
    # this means that class RepositoryError is inherited from Python's default Exception class
    def __init__(self, message: str = ""):
        self.__message = message

    @property
    def message(self):
        return self.__message


class MemoRepoStudent:
    def __init__(self):
        self._students_data: dict[int, Student] = {}
        self._last_id = 0

        if type(self) == MemoRepoStudent:
            self.generate_entries()

    def generate_entries(self):
        for _ in range(20):
            name = "".join(random.choices(string.ascii_letters, k=10))
            group = random.randint(100, 999)

            student = Student(name, group)
            student.student_id = self._last_id

            self._students_data[self._last_id] = student
            self._last_id += 1

    def add_student(self, student: Student):
        """
        Adds a new student
        :param student: the student to be added
        """
        student.student_id = self._last_id
        self._students_data[self._last_id] = student
        self._last_id += 1

    def remove_student(self, id_):
        """
        Removes the student with the given id
        :param id_: the id for the student to be removed
        """
        self._students_data.pop(id_)

    def update_student(self, student: Student):
        """
        Updates the student data with the changed student
        :param student: the student with which we update
        """
        self._students_data[student.student_id] = student

    def list_student(self):
        """
        :return: all the students
        """
        return self._students_data


class MemoRepoAssignment:
    def __init__(self):
        self._assignments_data: dict[int, Assignment] = {}
        self._last_id = 0

        if type(self) == MemoRepoAssignment:
            self.generate_entries()

    def generate_entries(self):
        for _ in range(20):
            description = "".join(random.choices(string.ascii_letters, k=10))
            deadline = random.randint(1, 6)

            assignment = Assignment(description, deadline)
            assignment.assignment_id = self._last_id

            self._assignments_data[self._last_id] = assignment
            self._last_id += 1


    def add_assignment(self, assignment: Assignment):
        """
        Adds a new assignment
        :param assignment: the assignment to be added
        """
        assignment.assignment_id = self._last_id
        self._assignments_data[self._last_id] = assignment
        self._last_id += 1

    def remove_assignment(self, id_):
        """
        Removes the assignment with the given id
        :param id_: the id for the assignment to be removed
        """
        self._assignments_data.pop(id_)

    def update_assignment(self, assignment: Assignment):
        """
        Updates the assignments data with the changed assignment
        :param assignment: the assignment with which we update
        """
        self._assignments_data[assignment.assignment_id] = assignment

    def list_assignment(self):
        """
        :return: all the assignments
        """
        return self._assignments_data


class MemoRepoGrades:
    def __init__(self):
        self._grades_data: list[Grade] = []

        if type(self) == MemoRepoGrades:
            self.generate_entries()

    def generate_entries(self):
        """
        Generates 20 entries
        Only the grade value is random, the assignment id increases,
        the student id decreases
        """
        for i in range(20):
            assignment_id = i
            student_id = 20 - i - 1

            grade_value = random.randint(1, 10)

            # ungraded assignment with a probability of 0.5
            p = random.random()

            if p > 0.5:
                grade_value = -1

            self._grades_data.append(Grade(assignment_id, student_id, grade_value))


    def add_grade(self, grade: Grade):
        """
        Adds a new grade
        :param grade: the grade to be added
        """
        self._grades_data.append(grade)

    def remove_grade(self, grade):
        """
        Removes the grade.
        :param grade: the grade to be removed
        """
        index = -1
        for i in range(len(self._grades_data)):
            if self._grades_data[i] == grade:
                index = i

        self._grades_data.pop(index)

    def update_grade(self, grade: Grade):
        """
        Updates the grades data with the changed grade
        :param grade: the grade with which we update
        """
        for i in self._grades_data:
            if i.assignment_id == grade.assignment_id and i.student_id == grade.student_id:
                i.grade_value = grade.grade_value
                return

    def list_grade(self):
        """
        :return: all the grades
        """
        return self._grades_data


class TextRepoStudent(MemoRepoStudent):
    def __init__(self, filename: str = "FileStudents.txt"):
        super().__init__()
        self._file_name = filename
        self.__read_from_file()

    def __read_from_file(self):
        """
        Reads from file all the students
        """
        try:
            with open(self._file_name, "r") as f:
                for line in f.readlines():
                    attributes = line.strip().split(",")
                    if len(attributes) != 3:
                        continue

                    student_id = int(attributes[0])
                    name = attributes[1]
                    group = int(attributes[2])

                    student = Student(name, group)
                    student.student_id = student_id

                    self._last_id = student_id + 1
                    self._students_data[student_id] = student
        except FileNotFoundError:
            # file will be created on first write
            self.generate_entries()
            self.__write_to_file()

    def __add_to_file(self, student):
        """
        Adds a student to file
        :param student: new student
        """

        with open(self._file_name, "a") as f:
            f.write(f"{student.student_id},{student.name},{student.group}\n")

    def __write_to_file(self):
        """
        Writes all students to file
        """

        with open(self._file_name, "w") as f:
            student_list = sorted(self._students_data.values(), key=lambda x: x.student_id)

            for student in student_list:
                f.write(f"{student.student_id},{student.name},{student.group}\n")

    def add_student(self, student):
        super().add_student(student)
        self.__add_to_file(student)

    def remove_student(self, id_):
        super().remove_student(id_)
        self.__write_to_file()

    def update_student(self, student: Student):
        super().update_student(student)
        self.__write_to_file()


class TextRepoAssignment(MemoRepoAssignment):
    def __init__(self, filename: str = "FileAssignments.txt"):
        super().__init__()
        self._file_name = filename
        self.__read_from_file()

    def __read_from_file(self):
        """
        Reads from file all the assignments
        """
        try:
            with open(self._file_name, "r") as f:
                for line in f.readlines():
                    attributes = line.strip().split(",")
                    if len(attributes) != 3:
                        continue

                    assignment_id = int(attributes[0])
                    description = attributes[1]
                    deadline = int(attributes[2])

                    assignment = Assignment(description, deadline)
                    assignment.assignment_id = assignment_id

                    self._last_id = assignment_id + 1
                    self._assignments_data[assignment_id] = assignment
        except FileNotFoundError:
            # file will be created on first write
            self.generate_entries()
            self.__write_to_file()

    def __add_to_file(self, assignment):
        """
        Adds an assignment to file
        :param assignment: new assignment
        """

        with open(self._file_name, "a") as f:
            f.write(f"{assignment.assignment_id},{assignment.description},{assignment.deadline}\n")

    def __write_to_file(self):
        """
        Writes all students to file
        """

        with open(self._file_name, "w") as f:
            assignment_list = sorted(self._assignments_data.values(), key=lambda x: x.assignment_id)

            for assignment in assignment_list:
                f.write(f"{assignment.assignment_id},{assignment.description},{assignment.deadline}\n")

    def add_assignment(self, assignment):
        super().add_assignment(assignment)
        self.__add_to_file(assignment)

    def remove_assignment(self, id_):
        super().remove_assignment(id_)
        self.__write_to_file()

    def update_assignment(self, assignment: Assignment):
        super().update_assignment(assignment)
        self.__write_to_file()


class TextRepoGrade(MemoRepoGrades):
    def __init__(self, filename: str = "FileGrades.txt"):
        super().__init__()
        self._file_name = filename
        self.__read_from_file()

    def __read_from_file(self):
        """
        Reads from file all the grades
        """
        try:
            with open(self._file_name, "r") as f:
                for line in f.readlines():
                    attributes = line.strip().split(",")
                    if len(attributes) != 3:
                        continue

                    assignment_id = int(attributes[0])
                    student_id = int(attributes[1])
                    grade_value = int(attributes[2])

                    grade = Grade(assignment_id, student_id, grade_value)
                    grade.id = id

                    self._last_id = assignment_id + 1
                    self._grades_data.append(grade)
        except FileNotFoundError:
            self.generate_entries()
            self.__write_to_file()

    def __add_to_file(self, grade):
        """
        Adds a grade to file
        :param grade: new grade
        """

        with open(self._file_name, "a") as f:
            f.write(f"{grade.assignment_id},{grade.student_id},{grade.grade_value}\n")

    def __write_to_file(self):
        """
        Writes all students to file
        """

        with open(self._file_name, "w") as f:
            for grade in self._grades_data:
                f.write(f"{grade.assignment_id},{grade.student_id},{grade.grade_value}\n")

    def add_grade(self, grade):
        super().add_grade(grade)
        self.__add_to_file(grade)

    def remove_grade(self, id_):
        super().remove_grade(id_)
        self.__write_to_file()


class BinaryRepoStudent(TextRepoStudent):
    def __init__(self, filename: str = "FileStudents.bin"):
        super().__init__(filename)

    def __read_from_file(self):
        try:
            with open(self._file_name, "rb") as f:
                self._students_data = pickle.load(f)
        except FileNotFoundError:
            self.generate_entries()
            self.__write_to_file()

    def __add_to_file(self, student):
        with open(self._file_name, "ab") as f:
            pickle.dump(student, f)

    def __write_to_file(self):
        with open(self._file_name, "wb") as f:
            pickle.dump(self._students_data, f)


class BinaryRepoAssignment(TextRepoAssignment):
    def __init__(self, filename: str = "FileAssignments.bin"):
        super().__init__(filename)

    def __read_from_file(self):
        try:
            with open(self._file_name, "rb") as f:
                self._assignments_data = pickle.load(f)
        except FileNotFoundError:
            self.generate_entries()
            self.__write_to_file()

    def __add_to_file(self, assignment):
        with open(self._file_name, "ab") as f:
            pickle.dump(assignment, f)

    def __write_to_file(self):
        with open(self._file_name, "wb") as f:
            pickle.dump(self._assignments_data, f)


class BinaryRepoGrade(TextRepoGrade):
    def __init__(self, filename: str = "FileGrades.bin"):
        super().__init__(filename)

    def __read_from_file(self):
        try:
            with open(self._file_name, "rb") as f:
                self._grades_data = pickle.load(f)
        except FileNotFoundError:
            self.generate_entries()
            self.__write_to_file()

    def __add_to_file(self, grade):
        with open(self._file_name, "ab") as f:
            pickle.dump(grade, f)

    def __write_to_file(self):
        with open(self._file_name, "wb") as f:
            pickle.dump(self._grades_data, f)
