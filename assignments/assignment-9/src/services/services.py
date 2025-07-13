import copy

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
        self.undo_operations = []
        self.redo_operations = []

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
        self.undo_operations.append({
            "event_type": "add_student",
            "student": copy.deepcopy(student)
        })

    def remove_student(self, id_):
        """
        Removes a student with the given id
        :param id_:  the id for the student to be removed
        """
        student = self._student_repo.get_by_id(id_)
        if student is not None:
            self._student_repo.remove_student(id_)
            temp = self._grade_repo.list_grade().copy()
            grades = []
            for grade in temp:
                if grade.student_id == id_:
                    grades.append(copy.deepcopy(grade))
                    self._grade_repo.remove_grade(grade)
            self.undo_operations.append({
                "event_type": "remove_student",
                "student": copy.deepcopy(student),
                "grades": grades
            })
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

        old_student = self._student_repo.list_student().get(id_)
        if old_student is not None:
            self.undo_operations.append({
                "event_type": "update_student",
                "student": copy.deepcopy(old_student)
            })
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

        assignment = Assignment(description, deadline)
        self._assignment_repo.add_assignment(assignment)
        self.undo_operations.append({
            "event_type": "add_assignment",

            "assignment": copy.deepcopy(assignment)
        })

    def remove_assignment(self, id_):
        """
        Removes an assignment with the given id
        :param id_:  the id for the assignment to be removed
        """
        assignment = self._assignment_repo.list_assignment().get(id_)
        if assignment is not None:
            self._assignment_repo.remove_assignment(id_)
            temp = self._grade_repo.list_grade().copy()
            grades = []
            for grade in temp:
                if grade.assignment_id == id_:
                    grades.append(copy.deepcopy(grade))
                    self._grade_repo.remove_grade(grade)

            self.undo_operations.append({
                "event_type": "remove_assignment",
                "assignment": copy.deepcopy(assignment),
                "grades": grades
            })

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

        old_assignment = self._assignment_repo.list_assignment().get(id_)
        if old_assignment is not None:
            self.undo_operations.append({
                "event_type": "update_assignment",
                "assignment": copy.deepcopy(old_assignment)
            })
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
            grade = Grade(assignment_id, student_id, -1)
            self._grade_repo.add_grade(grade)
            self.undo_operations.append({
                "event_type": "assign",
                "grade": copy.deepcopy(grade)
            })

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
            self.undo_operations.append({
                "event_type": "grade_assignment",
                "grade": copy.deepcopy(grade)
            })
            grade.grade_value = grade_value
            self._grade_repo.update_grade(grade)

    def stud_given_assignment_grade(self, assignment):
        """
        Creates a list with all students who received a given assignment,
        ordered descending by grade.
        :param assignment: the given assignment
        :return: the generated list
        """
        list_students_grades = []
        for grade in self._grade_repo.list_grade():
            if grade.assignment_id == assignment:
                list_students_grades.append([grade.student_id, grade.grade_value])
        if not list_students_grades:
            raise ServiceError("No student with the assignment given!")

        list_students = self._student_repo.list_student()
        for index in range(len(list_students_grades)):
            student_id = list_students_grades[index][0]
            list_students_grades[index][0] = list_students.get(student_id)

        return sorted(list_students_grades, key=lambda x: x[1], reverse=True)

    def late_assignment(self, current_week):
        """
        Creates a list with all students who are late in handing in at least one assignment.
        These are all the students who have an ungraded assignment for which
        the deadline has passed.
        :param current_week: the current week in the school year
        :return: the generated list
        """
        late_assignments = []
        for assignment in self._assignment_repo.list_assignment().values():
            if assignment.deadline < current_week:
                late_assignments.append(assignment.assignment_id)

        ungraded_grades = []
        for grade in self._grade_repo.list_grade():
            if grade.assignment_id in late_assignments and grade.grade_value == -1:
                ungraded_grades.append(grade.student_id)

        if not ungraded_grades:
            raise ServiceError("No ungraded assignments!")

        return [student for student in self._student_repo.list_student().values() if
                student.student_id in ungraded_grades]

    def school_situation(self):
        """
        Creates a list with the students with the best school situation,
        sorted in descending order of the average grade received for all graded assignments.
        :return: the generated list
        """
        list_students = []
        for student in self._grade_repo.list_grade():
            sum_of_grades = 0
            number_of_grades = 0
            for assignment in self._grade_repo.list_grade():
                if student.assignment_id == assignment.assignment_id:
                    if assignment.grade_value != -1:
                        sum_of_grades = sum_of_grades + assignment.grade_value
                        number_of_grades += 1
            if number_of_grades != 0:
                average = sum_of_grades / number_of_grades
            else:
                average = 0
            list_students.append([student, average])

        return sorted(list_students, key=lambda x: x[1], reverse=True)

    # event_type is what happened
    def undo(self):
        if not self.undo_operations:
            raise ServiceError("No more undo operations!")
        operation = self.undo_operations.pop()
        event_type = operation["event_type"]
        if event_type == "add_student":
            self.__handle_undo_add_student(operation["student"])
        elif event_type == "remove_student":
            self.__handle_undo_remove_student(operation["student"], operation["grades"])
        elif event_type == "update_student":
            self.__handle_undo_update_student(operation["student"])
        elif event_type == "add_assignment":
            self.__handle_undo_add_assignment(operation["assignment"])
        elif event_type == "remove_assignment":
            self.__handle_undo_remove_assignment(operation["assignment"], operation["grades"])
        elif event_type == "update_assignment":
            self.__handle_undo_update_assignment(operation["assignment"])
        elif event_type == "assign":
            self.__handle_undo_assign(operation["grade"])
        elif event_type == "grade_assignment":
            self.__handle_undo_grade_assignment(operation["grade"])

    def redo(self):
        if not self.redo_operations:
            raise ServiceError("No more redos!")
        operation = self.redo_operations.pop()
        event_type = operation["event_type"]

        if event_type == "add_student":
            self.__handle_redo_add_student(operation["student"], operation["grades"])
        elif event_type == "remove_student":
            self.__handle_redo_remove_student(operation["student"])
        elif event_type == "update_student":
            self.__handle_redo_update_student(operation["student"])
        elif event_type == "add_assignment":
            self.__handle_redo_add_assignment(operation["assignment"], operation["grades"])
        elif event_type == "remove_assignment":
            self.__handle_redo_remove_assignment(operation["assignment"])
        elif event_type == "update_assignment":
            self.__handle_redo_update_assignment(operation["assignment"])
        elif event_type == "assign":
            self.__handle_redo_assign(operation["grade"])
        elif event_type == "grade_assignment":
            self.__handle_redo_grade_assignment(operation["grade"])

    def __handle_undo_add_student(self, student: Student):
        self._student_repo.remove_student(student.student_id)
        self.redo_operations.append({
            "event_type": "remove_student",
            "student": copy.deepcopy(student)
        })

    def __handle_undo_remove_student(self, student:Student, grades):
        self._student_repo.add_student(student)
        for grade in grades:
            self._grade_repo.add_grade(grade)
        self.redo_operations.append({
            "event_type": "add_student",
            "student": copy.deepcopy(student),
            "grades": copy.deepcopy(grades)
        })

    def __handle_undo_update_student(self, student: Student):
        self._student_repo.update_student(student)
        self.redo_operations.append({
            "event_type": "update_student",
            "student": copy.deepcopy(student)
        })

    def __handle_undo_add_assignment(self, assignment: Assignment):
        self._assignment_repo.remove_assignment(assignment.assignment_id)
        self.redo_operations.append({
            "event_type": "remove_assignment",
            "assignment": copy.deepcopy(assignment)
        })

    def __handle_undo_remove_assignment(self, assignment: Assignment, grades):
        self._assignment_repo.add_assignment(assignment)
        for grade in grades:
            self._grade_repo.add_grade(grade)
        self.redo_operations.append({
            "event_type": "add_assignment",
            "assignment": copy.deepcopy(assignment),
            "grades": copy.deepcopy(grades)
        })

    def __handle_undo_update_assignment(self, assignment: Assignment):
        self._assignment_repo.update_assignment(assignment)
        self.redo_operations.append({
            "event_type": "update_assignment",
            "assignment": copy.deepcopy(assignment)
        })

    def __handle_undo_assign(self, grade: Grade):
        for grade_ in self._grade_repo.list_grade():
            if grade_.assignment_id == grade.assignment_id and grade_.student_id == grade.student_id:
                self.redo_operations.append({
                    "event_type": "grade_assignment",
                    "grade": copy.deepcopy(grade_)
                })
                self._grade_repo.remove_grade(grade)
                break

    def __handle_undo_grade_assignment(self, grade: Grade):
        for grade_ in self._grade_repo.list_grade():
            if grade_.assignment_id == grade.assignment_id and grade_.student_id == grade.student_id:
                self.redo_operations.append({
                    "event_type": "grade_assignment",
                    "grade": copy.deepcopy(grade_)
                })
                self._grade_repo.update_grade(grade)
                break

    def __handle_redo_add_student(self, student: Student, grades):
        self._student_repo.add_student(student)
        for grade in grades:
            self._grade_repo.remove_grade(grade)
        self.undo_operations.append({
            "event_type": "add_student",
            "student": copy.deepcopy(student),
            "grades": copy.deepcopy(grades)
        })

    def __handle_redo_remove_student(self, student: Student):
        self._student_repo.remove_student(student.student_id)
        self.undo_operations.append({
            "event_type": "remove_student",
            "student": copy.deepcopy(student)
        })

    def __handle_redo_update_student(self, student: Student):
        self._student_repo.update_student(student)
        self.undo_operations.append({
            "event_type": "update_student",
            "student": copy.deepcopy(student)
        })

    def __handle_redo_add_assignment(self, assignment: Assignment, grades):
        self._assignment_repo.add_assignment(assignment)
        for grade in grades:
            self._grade_repo.remove_grade(grade)
        self.undo_operations.append({
            "event_type": "add_assignment",
            "assignment": copy.deepcopy(assignment),
            "grades": copy.deepcopy(grades)
        })

    def __handle_redo_remove_assignment(self, assignment: Assignment):
        self._assignment_repo.remove_assignment(assignment.assignment_id)
        self.undo_operations.append({
            "event_type": "remove_assignment",
            "assignment": copy.deepcopy(assignment)
        })

    def __handle_redo_update_assignment(self, assignment: Assignment):
        self._assignment_repo.update_assignment(assignment)
        self.undo_operations.append({
            "event_type": "update_assignment",
            "assignment": copy.deepcopy(assignment)
        })

    def __handle_redo_assign(self, grade: Grade):
        for grade_ in self._grade_repo.list_grade():
            if grade_.assignment_id == grade.assignment_id and grade_.student_id == grade.student_id:
                self.undo_operations.append({
                    "event_type": "grade_assignment",
                    "grade": copy.deepcopy(grade_)
                })
                self._grade_repo.add_grade(grade)
                break

    def __handle_redo_grade_assignment(self, grade: Grade):
        for grade_ in self._grade_repo.list_grade():
            if grade_.assignment_id == grade.assignment_id and grade_.student_id == grade.student_id:
                self.undo_operations.append({
                    "event_type": "grade_assignment",
                    "grade": copy.deepcopy(grade_)
                })
                self._grade_repo.update_grade(grade)
                break
