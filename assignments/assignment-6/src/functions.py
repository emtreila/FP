#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#
import operator


def create_solution(p1, p2, p3) -> list:
    """
    Create the list of scores for a participant
    :param p1: score for 1st problem
    :param p2: score for 2nd problem
    :param p3: score for 3rd problem
    :return: list of scores for a participant
    """
    return [p1, p2, p3]


def get_sol1(scores: list):
    return scores[0]


def get_sol2(scores: list):
    return scores[1]


def get_sol3(scores: list):
    return scores[2]


def set_sol1(scores: list, p):
    scores[0] = p


def set_sol2(scores: list, p):
    scores[1] = p


def set_sol3(scores: list, p):
    scores[2] = p


# Converts to string
def to_string(scores: list) -> str:
    return f"{get_sol1(scores)},{get_sol2(scores)},{get_sol3(scores)}"


def add(p1, p2, p3, scores: list) -> None:
    """
    Add the result of a new participant to the list of scores
    :param p1: score for 1st problem
    :param p2: score for 2nd problem
    :param p3: score for 3rd problem
    :param scores: the list of scores for all participants
    """
    scores.append(create_solution(p1, p2, p3))


def insert1(p1, p2, p3, scores: list, position) -> None:
    """
    Inserts the score of a new participant at a given position in the list of all scores
    :param p1: score for 1st problem
    :param p2: score for 2nd problem
    :param p3: score for 3rd problem
    :param scores: the list of scores for all participants
    :param position: the position where the new score is inserted
    """
    scores.insert(position, create_solution(p1, p2, p3))


def remove1(scores, position) -> None:
    """
    Removes the score of a participant at a given position
    :param scores: the list of scores for all participants
    :param position: the position where the score becomes 0

    """
    set_sol1(scores[position], 0)
    set_sol2(scores[position], 0)
    set_sol3(scores[position], 0)


def remove2(scores: list, start, end) -> None:
    """
    Removes the score of the participants from the position start to position end
    :param scores: the list of scores for all participants
    :param start: starting position
    :param end: the last position
    """
    for i in range(start, end + 1):
        set_sol1(scores[i], 0)
        set_sol2(scores[i], 0)
        set_sol3(scores[i], 0)


def remove3(scores: list, sign, x) -> None:
    """
    Set the scores having an average score </=/> than x to 0
    :param scores: the list of scores for all participants
    :param sign: either the score is smaller/equal/bigger
    :param x: the score with which we compare the average score of participants
    """
    op = operator.eq
    if sign == "<":
        op = operator.lt
    elif sign == ">":
        op = operator.gt
    for i in range(len(scores)):
        average = sum(scores[i]) // 3
        if op(average, x):
            set_sol1(scores[i], 0)
            set_sol2(scores[i], 0)
            set_sol3(scores[i], 0)


def replace(scores, participant, problem, new):
    """
    Replaces the old score obtained by the participant with a new score
    :param scores: the list of scores for all participants
    :param participant: the participant whose score is changed
    :param problem: the problem that's changed
    :param new: the new score
    """
    if problem == 0:
        set_sol1(scores[participant], new)
    elif problem == 1:
        set_sol2(scores[participant], new)
    elif problem == 2:
        set_sol3(scores[participant], new)


def list1(scores: list) -> list:
    """
    :param scores:  the list of scores for all participants
    :return:  the list of scores for all participants
    """
    return scores


def list2(scores: list) -> list:
    """
        :param scores:  the list of scores for all participants
        :return:  the list of scores for all participants sorted in decreasing order by the average score
    """
    return sorted(scores, key=lambda x: sum(x) // 3, reverse=True)


def list3(scores: list, sign, score) -> list:
    """
    Display participants with an average score >/=/< than the value score
    :param scores: the list of scores for all participants
    :param sign: </=/>
    :param score: the value with which the average score is compared
    :return:  the list if scores of all participants which have an average score >/</= to the value score
    """
    op = operator.eq
    if sign == ">":
        op = operator.gt
    elif sign == "<":
        op = operator.lt
    new_list = []
    for i in range(len(scores)):
        if op(sum(scores[i]) // 3, score):
            new_list.append(scores[i])
    return new_list


def top1(scores: list, number) -> list:
    """
    Display the number of participants having the highest average score, in descending order of average score
    :param scores: the list of scores for all participants
    :return: the list with the number of participants with the highest average score
    """
    new_list = sorted(scores, key=lambda x: sum(x) // 3, reverse=True)
    top_list = []
    for i in range(number):
        top_list.append(new_list[i])
    return top_list


def top2(scores: list, number, p) -> list:
    """
    Display participants (number participants) who obtained the highest score for a problem P, sorted descending by that score
    :param scores: the list of scores for all participants
    :param number: number of participants in the top
    :param p: the problem by which the participants are sorted
    :return: the list with the number of participants with the highest average score
    """
    new_list = sorted(scores, key=lambda x: x[p], reverse=True)
    top_list = []
    for i in range(number):
        top_list.append(new_list[i])
    return top_list


def undo(undo_scores: list) -> list:
    """
    Undos the last operation that modified the list
    :param undo_scores: The previous operations
    :return: The last list before modifications
    """
    return undo_scores.pop()


def test():
    test_add()
    test_insert1()
    test_remove1()
    test_remove2()
    test_remove3()
    test_replace()


def test_add():
    scores = [[1, 2, 3], [3, 4, 6], [6, 7, 6], [9, 1, 6], [10, 10, 8]]
    len1 = len(scores)
    add(2, 5, 7, scores)
    try:
        assert len(scores) == len1 + 1 and scores[-1] == [2, 5, 7]
        print("Test add successfully done!")
    except:
        print("Test add failed.")


def test_insert1():
    scores = [[1, 2, 3], [3, 4, 6], [6, 7, 6], [9, 1, 6], [10, 10, 8]]
    len1 = len(scores)
    insert1(2, 5, 7, scores, 3)
    try:
        assert len(scores) == len1 + 1 and scores[3] == [2, 5, 7]
        print("Test insert1 successfully done!")
    except:
        print("Test insert1 failed.")


def test_remove1():
    scores = [[1, 2, 3], [3, 4, 6], [6, 7, 6], [9, 1, 6], [10, 10, 8]]
    remove1(scores, 3)
    try:
        assert scores[3] == [0, 0, 0]
        print("Test remove1 successfully done!")
    except:
        print("Test remove1 failed.")


def test_remove2():
    scores = [[1, 2, 3], [3, 4, 6], [6, 7, 6], [9, 1, 6], [10, 10, 8]]
    remove2(scores, 1, 3)
    try:
        assert scores[1] == [0, 0, 0] and scores[2] == [0, 0, 0] and scores[3] == [0, 0, 0]
        print("Test remove2 successfully done!")
    except:
        print("Test remove2 failed.")


def test_remove3():
    scores = [[1, 2, 3], [3, 4, 6], [6, 7, 6], [9, 3, 6], [10, 10, 8]]
    remove3(scores, "=", 6)
    try:
        assert scores[2] == [0, 0, 0] and scores[3] == [0, 0, 0]
        print("Test remove3 successfully done!")
    except:
        print("Test remove3 failed.")


def test_replace():
    scores = [[1, 2, 3], [3, 4, 6], [6, 7, 6], [9, 3, 6], [10, 10, 8]]
    replace(scores, 2, 0, 1)
    try:
        assert scores[2] == [1, 7, 6]
        print("Test replace successfully done!")
    except:
        print("Test replace failed.")
