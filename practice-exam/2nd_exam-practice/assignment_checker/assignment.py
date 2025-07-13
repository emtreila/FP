class Assignment:
    def __init__(self, name, solution, student_id: int = None):
        self._name = name
        self._solution = solution
        self._student_id = student_id
        self.__words_in_solution = set(solution.split())

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
    def solution(self):
        return self._solution

    @solution.setter
    def solution(self, new):
        self._solution = new
        self.__words_in_solution = set(new.split())

    @property
    def words_in_solution(self):
        return self.__words_in_solution

    def __str__(self):
        return f"Id: {self._student_id}, Name: {self._name}, Solution: {self._solution}"

    def __repr__(self):
        return self.__str__()