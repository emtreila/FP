class Student:
    def __init__(self, name, attendance, grade):
        self._student_id = None
        self._name = name
        self._attendance = attendance
        self._grade = grade

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, new):
        self._student_id = new

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new):
        self._name = new

    @property
    def attendance(self):
        return self._attendance

    @attendance.setter
    def attendance(self, new):
        self._attendance = new

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new):
        self._grade = new

    def __str__(self):
        return f"Student id: {self._student_id}, Name: {self._name}, Attendance:{self._attendance}, Grade:{self.grade}"

    def __repr__(self):
        return self.__str__()
