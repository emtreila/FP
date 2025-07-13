class Student:
    def __init__(self, name, group):
        self._student_id = None
        self._name = name
        self._group = group

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, new_id):
        self._student_id = new_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, new_group):
        self._group = new_group

    def __str__(self):
        return f"Student id: {self._student_id}, Name: {self._name}, Group:{self._group}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self._student_id == other.student_id and \
            self._group == other.group and \
            self._name == other.name
