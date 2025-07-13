from assignment_checker.assignment import Assignment


class TextMemoRepo:
    def __init__(self, file_name: str = "assignments.txt"):
        self._file_name = file_name
        self._assignment_data: dict[int, Assignment] = {}
        self._last_id = 0
        self.__read_file()

    def __read_file(self):
        with open(self._file_name, "r") as f:
            for line in f.readlines():
                attributes = line.strip().split(",")
                if len(attributes) != 3:
                    continue

                student_id = int(attributes[0])
                name = attributes[1]
                solution = attributes[2]

                assignment = Assignment(name, solution)
                assignment.student_id = student_id

                self._last_id = student_id + 1
                self._assignment_data[student_id] = assignment

    def write_to_file(self):
        with open(self._file_name, "w") as f:
            assignment_list = sorted(self._assignment_data.values(), key=lambda x: x.student_id)

            for assignment in assignment_list:
                f.write(f"{assignment.student_id},{assignment.name},{assignment.solution}\n")

    def add_to_file(self, assignment: Assignment):
        with open(self._file_name, "a") as f:
            f.write(f"{assignment.student_id},{assignment.name},{assignment.solution}\n")

    def get_all_assignments(self):
        """
        :return: returns all assignments
        """
        return self._assignment_data

    def add_assignment(self, name, solution):
        """
        Adds a new assignment to the repository
        :param name: name of the student
        :param solution: the solution of the assignment
        """
        new = Assignment(name, solution)
        new.student_id = self._last_id
        self._last_id += 1

        self._assignment_data[new.student_id] = new
        self.add_to_file(new)


