from src.domain.assigment import Assignment
from src.domain.grade import Grade
from src.domain.student import Student
from src.repository.repository import MemoRepoGrades, MemoRepoStudent, MemoRepoAssignment


class ServiceError(Exception):
    # this means that class ServiceError is inherited from Python's default Exception class
    def __init__(self, message: str = ""):
        self.__message = message

    @property
    def message(self):
        return self.__message


class Services:
    def __init__(self, student_repo: MemoRepoStudent = MemoRepoStudent(),
                 assignment_repo: MemoRepoAssignment = MemoRepoAssignment(),
                 grade_repo: MemoRepoGrades = MemoRepoGrades()):
        self._student_repo = student_repo
        self._assignment_repo = assignment_repo
        self._grade_repo = grade_repo

    def add_student(self, name, group):
        """
        Adds a new student
        :param name: new name
        :param group: new group
        """
        if not name or not group:
            raise ServiceError("Invalid parameters!")
        if not (100 <= group <= 999):
            raise ServiceError("Invalid group number!")
        student = Student(name, group)
        self._student_repo.add_student(student)

    def remove_student(self, id_):
        """
        Removes a student with the given id
        :param id_:  the id for the student to be removed
        """

        if self._student_repo.list_student().get(id_) is not None:
            self._student_repo.remove_student(id_)
            temp = self._grade_repo.list_grade().copy()
            for i in temp:
                if i.student_id == id_:
                    self._grade_repo.remove_grade(i)
            return
        raise ServiceError("No student with the given id!")

    def update_student(self, student):
        """
        Modifies the student
        :param student: new student
        """
        id_ = student.student_id
        name = student.name
        group = student.group

        if not name:
            raise ServiceError("Invalid parameters!")
        if not (100 <= group <= 999):
            raise ServiceError("Invalid group number!")

        if self._student_repo.list_student().get(id_) is not None:
            self._student_repo.update_student(student)

    def list_student(self):
        """
        :return: all the students
        """
        return self._student_repo.list_student()

    def list_groups(self):
        """
        :return: all groups
        """
        students = self._student_repo.list_student()
        groups = set()

        for student in students.values():
            groups.add(student.group)

        return groups

    def add_assignment(self, description, deadline):
        """
        Adds a new assignment
        :param description: new description
        :param deadline: new deadline
        """

        if not description or not deadline:
            raise ServiceError("Invalid parameters!")
        self._assignment_repo.add_assignment(Assignment(description, deadline))

    def remove_assignment(self, id_):
        """
        Removes an assignment with the given id
        :param id_:  the id for the assignment to be removed
        """

        if self._assignment_repo.list_assignment().get(id_) is not None:
            self._assignment_repo.remove_assignment(id_)
            return
        raise ServiceError("No assignment with the given id!")

    def update_assignment(self, assignment):
        """
        Modifies the assignment
        :param assignment: new assignment
        """
        id_ = assignment.assignment_id
        description = assignment.description
        deadline = assignment.deadline

        if not description:
            raise ServiceError("Invalid parameters!")
        if not (1 <= deadline <= 6):
            raise ServiceError("Invalid deadline!")

        if self._assignment_repo.list_assignment().get(id_) is not None:
            self._assignment_repo.update_assignment(assignment)

    def list_assignment(self):
        """
        :return: all the assignments
        """
        return self._assignment_repo.list_assignment()

    def assign(self, assignment_id, student_id):
        """
        Assigns an assignment to a student
        :param assignment_id: id of the assignment
        :param student_id: id of the student
        """

        if self._assignment_repo.list_assignment().get(assignment_id) is None:
            raise ServiceError("No such id!")
        if self._student_repo.list_student().get(student_id) is None:
            raise ServiceError("No such id!")

        exists = False
        for grade in self._grade_repo.list_grade():
            if grade.assignment_id == assignment_id and grade.student_id == student_id:
                exists = True
                break

        if not exists:
            self._grade_repo.add_grade(Grade(assignment_id, student_id, -1))

    def list_grade(self):
        """
        Returns the list of all grades
        :return: the list of all grades
        """
        return self._grade_repo.list_grade()

    def list_ungraded_assignments(self):
        """
        :return: all the ungraded grades
        """

        ungraded = []
        for grade in self._grade_repo.list_grade():
            if grade.grade_value == -1:
                ungraded.append(grade)
        return ungraded

    def grade_assignment(self, assignment_id: int, student_id: int, grade_value: int):
        """
        Grades the specified assignment
        :param assignment_id: the id of the assignment to grade
        :param student_id: the id of the student
        :param grade_value: the new grade value
        """
        if self._assignment_repo.list_assignment().get(assignment_id) is None:
            raise ServiceError("No such id!")
        if self._student_repo.list_student().get(student_id) is None:
            raise ServiceError("No such id!")
        if not (1 <= grade_value <= 10):
            raise ServiceError("Invalid grade!")

        grade = None

        for grade_ in self._grade_repo.list_grade():
            if grade_.assignment_id == assignment_id and grade_.student_id == student_id:
                grade = grade_
                break

        if grade is not None:
            grade.grade_value = grade_value
            self._grade_repo.update_grade(grade)
