from pprint import pprint

from exam.service import Service
from exam.student import Student


class UI(Service):
    def __init__(self, service: Service = Service):
        super().__init__()
        self._service = service

    def main(self):
        while True:
            print("\n1. Add a new student.")
            print("2. Display students.")
            print("3. Give bonus points for students.")
            print("4. Display students with a given name.")
            print("5. Exit")

            option = input("Choose your option: ")

            try:
                option = int(option)
            except:
                print("Invalid option!")
                continue
            if not option:
                print("Invalid option!")
                continue
            elif not (1 <= option <= 5):
                print("Invalid option!")
                continue

            if option == 5:
                exit()

            elif option == 1:
                while True:
                    name = input("Enter the name: ")
                    try:
                        self._service.handle_name(name)
                    except Exception as e:
                        print(e)
                        continue
                    break

                while True:
                    attendance = input("Enter the attendance: ")

                    try:
                        attendance = int(attendance)
                    except:
                        print("The attendance should be a number!")
                        continue

                    try:
                        self._service.handle_attendance(attendance)
                    except Exception as e:
                        print(e)
                        continue
                    break

                while True:
                    grade = input("Enter the grade:")

                    try:
                        grade = int(grade)
                    except:
                        print("The grade should be an integer!")
                        continue

                    try:
                        self._service.handle_grade(grade)
                    except Exception as e:
                        print(e)
                        continue

                    break

                new_student = Student(name, attendance, grade)
                self._service.add_student(new_student)

            elif option == 2:

                students = self._service.get_all_students().values()
                sorted_students = sorted(students, key=lambda student: (-student.grade, student.name))

                print("\nSTUDENTS")
                pprint(sorted_students)

            elif option == 3:

                p = int(input("Number of attendance: "))
                b = int(input("Bonus: "))

                self._service.give_bonus(p, b)

            elif option == 4:
                name = input("Enter the name: ")
                students = self._service.get_all_students().values()
                sorted_students = sorted(students, key=lambda student: student.name)

                for student in sorted_students:
                    if name in student.name:
                        print(student)
