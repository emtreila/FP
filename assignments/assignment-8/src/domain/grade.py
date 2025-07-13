class Grade:
    def __init__(self, assignment_id, student_id, grade_value):
        self._assignment_id = assignment_id
        self._student_id = student_id
        self._grade_value = grade_value

    @property
    def assignment_id(self):
        return self._assignment_id

    @assignment_id.setter
    def assignment_id(self, new_id):
        self._assignment_id = new_id

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, new_student_id):
        self._student_id = new_student_id

    @property
    def grade_value(self):
        return self._grade_value

    @grade_value.setter
    def grade_value(self, new_grade_value):
        self._grade_value = new_grade_value

    def __str__(self):
        return f"Assignment id:{self._assignment_id}, Student id: {self._student_id}, Grade value:{self._grade_value}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self._student_id == other.student_id and self._assignment_id == other.assignment_id and self.grade_value == other.grade_value
