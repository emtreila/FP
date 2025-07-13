from exam.student import Student


class TextMemoRepo:
    def __init__(self, file_name: str = "students.txt"):
        self._file_name = file_name
        self._student_data: dict[int, Student] = {}
        self._last_id = 0
        self.__read_from_file()

    def __read_from_file(self):
        """
        Reads from file all the students
        """

        with open(self._file_name, "r") as f:
            for line in f.readlines():
                attributes = line.strip().split(",")
                if len(attributes) != 4:
                    continue

                student_id = int(attributes[0])
                name = str(attributes[1])
                attendance = int(attributes[2])
                grade = int(attributes[3])

                student = Student(name, attendance, grade)
                student.student_id = student_id

                self._last_id = student_id + 1
                self._student_data[student_id] = student

    def __write_to_file(self):
        """
        Writes all students to file
        """

        with open(self._file_name, "w") as f:
            student_list = sorted(self._student_data.values(), key=lambda x: x.student_id)

            for student in student_list:
                f.write(f"{student.student_id}, {student.name}, {student.attendance}, {student.grade}\n")

    def __add_to_file(self, student):
        """
        Adds a student to file
        :param student: new student
        """

        with open(self._file_name, "a") as f:
            f.write(f"{student.student_id}, {student.name}, {student.attendance}, {student.grade}\n")

    def get_student_by_id(self, id_):
        """
        :param id_: the id for the student
        :return: the student with the given id
        """
        return self._student_data[id_]

    def get_all_students(self):
        """
        :return: returns all students
        """
        return self._student_data

    def add_student(self, new_student):
        """
        Adds a new student
        :param new_student: the student added
        """
        new_student.student_id = self._last_id
        self._last_id += 1
        self._student_data[new_student.student_id] = new_student

        self.__add_to_file(new_student)

    def update_student_grade(self, student_id, new):
        """
        Updates the information about student
        :param student_id: the id of the student
        :param new: the new grade
        """
        student = self._student_data[student_id]
        student.grade = new

        self.__write_to_file()
