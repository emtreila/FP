from assignment_checker.repository import TextMemoRepo


class Service:
    def __init__(self, assignment_repo: TextMemoRepo = TextMemoRepo):
        super().__init__()
        self._assignment_repo = assignment_repo

    def add_assignment(self, name: str, solution: str):
        """
        Adds a new assignment to the repository
        :param name: name of the student
        :param solution: the solution of the assignment
        """
        self._assignment_repo.add_assignment(name, solution)

    def get_all_assignments(self):
        """
        :return: returns all assignments
        """
        return self._assignment_repo.get_all_assignments()

    def dishonesty_check(self):
        """
        Checks for dishonesty
        :return: returns a list of students who have cheated
        """
        assignments = list(self._assignment_repo.get_all_assignments().values())
        result = {
            x.name: [] for x in assignments
        }

        for i in range(0, len(assignments) - 1):
            words_i = assignments[i].words_in_solution

            for j in range(i + 1, len(assignments) - 1):
                words_j = assignments[j].words_in_solution

                words = words_i.intersection(words_j)
                common_i = (len(words) / len(words_i))
                common_j = (len(words) / len(words_j))

                if common_j > 0.2:
                    result[assignments[i].name].append((assignments[j].name, common_j))
                if common_i > 0.2:
                    result[assignments[j].name].append((assignments[i].name, common_i))

        return result
