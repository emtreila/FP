from pprint import pprint

from src.domain.assigment import Assignment
from src.domain.student import Student
from src.services.services import Services


class UI:
    def __init__(self, services: Services):
        self._services = services

    def __handle_student(self):
        print("\n1) Add student")
        print("2) Remove student")
        print("3) Update student information")
        print("4) List all students\n")

        command_student = input("Choose an option: ")
        if not command_student:
            print("No command given!")
            return

        try:
            command_student = int(command_student)
        except:
            print("Invalid command!")
            return
        if not (1 <= command_student <= 4):
            print("Invalid command!")
            return

        if command_student == 1:
            name = input("Name: ")
            group = input("Group: ")
            try:
                group = int(group)
            except:
                print("Invalid group!")
                return
            if not (100 <= group <= 999):
                print("Invalid group!")
                return
            try:
                self._services.add_student(name, group)
            except Exception as error:
                print(error)
        elif command_student == 2:
            print("\nStudent IDs:\n")
            pprint(self._services.list_student().keys())

            id_ = input("Id of the student to be removed: ")
            try:
                id_ = int(id_)
            except:
                print("Invalid id!")
                return
            try:
                self._services.remove_student(id_)
            except Exception as error:
                print(error)
        elif command_student == 3:
            print("\nStudents:\n")
            pprint(self._services.list_student())

            student_id = input("Type id of the student: ")

            try:
                student_id = int(student_id)
            except:
                print("Invalid id!")
                return

            new_name = input("Name: ")
            new_group = input("Group: ")

            try:
                new_group = int(new_group)
            except:
                print("Invalid group!")
                return

            new_student = Student(new_name, new_group)
            new_student.student_id = student_id
            self._services.update_student(new_student)
        if command_student == 4:
            print("Students:\n")
            pprint(self._services.list_student())

    def __handle_assignments(self):
        print("\n1) Add assignment")
        print("2) Remove assignment")
        print("3) Update assignment information")
        print("4) List all assignments\n")

        command_assignment = input("Choose an option: ")
        if not command_assignment:
            print("No command given!")
            return
        try:
            command_assignment = int(command_assignment)
        except:
            print("Invalid command!")
            return
        if not (1 <= command_assignment <= 4):
            print("Invalid command!")
            return

        if command_assignment == 1:
            description = input("Description: ")
            deadline = input("Deadline (in weeks): ")
            try:
                deadline = int(deadline)
            except:
                print("Invalid deadline!")
                return
            if not (1 <= deadline <= 6):
                print("The deadline can be maximum of 6 weeks!")
                return
            try:
                self._services.add_assignment(description, deadline)
            except Exception as e:
                print(e)
        elif command_assignment == 2:
            print("\nAssignment IDs:\n")
            pprint(self._services.list_assignment().keys())

            id_ = input("Id of the assignment to be removed: ")
            try:
                id_ = int(id_)
            except:
                print("Invalid id!")
                return
            try:
                self._services.remove_assignment(id_)
            except Exception as e:
                print(e)
        elif command_assignment == 3:
            print("\nAssignments:\n")
            pprint(self._services.list_assignment())

            assignment_id = input("Type id of the assignment: ")

            try:
                assignment_id = int(assignment_id)
            except:
                print("Invalid id!")
                return

            new_description = input("Description: ")
            new_deadline = input("Deadline: ")

            try:
                new_deadline = int(new_deadline)
            except:
                print("Invalid deadline!")
                return

            new_assignment = Assignment(new_description, new_deadline)
            new_assignment.assignment_id = assignment_id
            self._services.update_assignment(new_assignment)
        elif command_assignment == 4:
            print("Assignments:\n")
            pprint(self._services.list_assignment())

    def __handle_grades(self):
        print("\n1) Give assignments to a student")
        print("2) Give assignments to a group of students")
        print("3) Grade student for a given assignment")
        print("4) List grades\n")

        command_grade = input("Choose an option: ")

        if not command_grade:
            print("No command given!")
            return
        try:
            command_grade = int(command_grade)
        except:
            print("Invalid command!")
            return
        if not (1 <= command_grade <= 4):
            print("Invalid command!")
            return

        if command_grade == 1:
            print("\nStudents:\n")
            pprint(self._services.list_student())
            student_id = input("Give the id for the student you want to assign to: ")
            try:
                student_id = int(student_id)
            except:
                print("Invalid id!")
                return

            print("Assignments:\n")
            pprint(self._services.list_assignment())
            assignment_id = input("Give the id for the assignment you want to give: ")

            try:
                assignment_id = int(assignment_id)
            except:
                print("Invalid id!")
                return

            try:
                self._services.assign(assignment_id, student_id)
            except Exception as e:
                print(e)
        elif command_grade == 2:
            groups = self._services.list_groups()
            print("Groups:\n")
            pprint(groups)
            group = input("Give the group you want to assign to: ")
            try:
                group = int(group)
            except:
                print("Invalid id!")
                return

            print("Assignments:\n")
            pprint(self._services.list_assignment())
            assignment_id = input("Give the id for the assignment you want to give: ")
            try:
                assignment_id = int(assignment_id)
            except:
                print("Invalid id!")
                return

            exists = False
            for student in self._services.list_student().values():
                if student.group == group:
                    try:
                        self._services.assign(assignment_id, student.student_id)
                        exists = True
                    except Exception as e:
                        print(e)
                        return

            if not exists:
                print("No such group!")
        elif command_grade == 3:
            ungraded = self._services.list_ungraded_assignments()
            if not ungraded:
                print("No ungraded assignments!")
                return

            print("Ungraded grades:\n")
            pprint(ungraded)

            assignment_id = input("Give the id for the assignment you want to grade: ")
            try:
                assignment_id = int(assignment_id)
            except:
                print("Invalid id!")
                return

            student_id = input("Give the id for the student you want to grade: ")
            try:
                student_id = int(student_id)
            except:
                print("Invalid id!")
                return

            grade_value = input("Give the grade for the assignment: ")
            try:
                grade_value = int(grade_value)
            except:
                print("Invalid grade!")
                return

            try:
                self._services.grade_assignment(assignment_id, student_id, grade_value)
            except Exception as e:
                print(e)
        elif command_grade == 4:
            print("\nGrades:\n")
            pprint(self._services.list_grade())

    def main(self):
        while True:
            print("\nMENU")
            print("1) Manage students")
            print("2) Manage assignments")
            print("3) Manage grading + assignments given to students")
            print("4) Exit\n")
            command = input("Please select your choice: ")

            if not command:
                print("No command given!")
                continue

            try:
                command = int(command)
            except:
                print("Invalid command!")
                continue
            if not (1 <= command <= 4):
                print("Invalid command!")
                continue

            if command == 4:
                print("You've exited the program!")
                exit()

            if command == 1:
                self.__handle_student()

            if command == 2:
                self.__handle_assignments()

            if command == 3:
                self.__handle_grades()
