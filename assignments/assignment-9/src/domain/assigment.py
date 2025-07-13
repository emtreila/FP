class Assignment:
    def __init__(self, description, deadline):
        self._assignment_id = None
        self._description = description
        self._deadline = deadline

    @property
    def assignment_id(self):
        return self._assignment_id

    @assignment_id.setter
    def assignment_id(self, new_id):
        self._assignment_id = new_id

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        self._description = new_description

    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, new_deadline):
        self._deadline = new_deadline

    def __str__(self):
        return f"Assignment id:{self._assignment_id}, Description: {self._description}, Deadline:{self._deadline}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self._assignment_id == other.assignment_id and \
            self._description == other.description and \
            self._deadline == other.deadline
