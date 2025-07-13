from exam.repository import TextMemoRepo


class Service(TextMemoRepo):
    def __init__(self, student_repo: TextMemoRepo = TextMemoRepo):
        super().__init__()
        self._student_repo = student_repo

    def handle_name(self, name: str):
        """
        Check if the name is correct input
        """
        words = name.strip().split(" ")
        if len(words) < 2:
            raise ValueError("The name should have at least 2 words!")

        for word in words:
            if len(word) < 3:
                raise ValueError("The words should have at least 3 letters!")

    def handle_attendance(self, attendance: int):
        """
        Check if the attendance is correct input
        """
        if attendance < 0:
            raise ValueError("The attendance should be a positive number!")

    def handle_grade(self, grade: int):
        """
        Check if the grade is correct input
        """
        if grade < 0 or grade > 10:
            raise ValueError("The grade should be between 0 and 10!")

    def get_all_students(self):
        """
        :return: all the students
        """
        return self._student_repo.get_all_students()

    def add_student(self, new_student):
        """
        Adds a new student
        :param new_student: the new student to be added
        """
        self._student_repo.add_student(new_student)

    def give_bonus(self, p: int, b: int):
        """
        Gives the bonus b to the grade for the students with at least p attendances
        :param p: number of attendances
        :param b: bonus
        """
        students = self._student_repo.get_all_students().values()
        for student in students:

            if student.attendance >= p:
                if student.grade + b <= 10:
                    grade = student.grade + b
                else:
                    grade = 10

                self._student_repo.update_student_grade(student.student_id, grade)
