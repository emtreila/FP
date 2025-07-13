from jproperties import Properties

from src.repository.repository import MemoRepoStudent, MemoRepoAssignment, MemoRepoGrades, TextRepoStudent, \
    TextRepoAssignment, TextRepoGrade, BinaryRepoStudent, BinaryRepoAssignment, BinaryRepoGrade
from src.services.services import Services
from src.ui.ui import UI

p = Properties()

with open("settings.properties", "rb") as f:
    p.load(f, "utf-8")

repository_type = p.get("repository").data.strip()

repo_student = None
repo_assignment = None
repo_grade = None

if repository_type == "inmemory":
    repo_student = MemoRepoStudent()
    repo_assignment = MemoRepoAssignment()
    repo_grade = MemoRepoGrades()

elif repository_type == "text":
    students_file = p.get("students").data.strip()
    assignments_file = p.get("assignments").data.strip()
    grades_file = p.get("grades").data.strip()

    repo_student = TextRepoStudent(students_file)
    repo_assignment = TextRepoAssignment(assignments_file)
    repo_grade = TextRepoGrade(grades_file)

elif repository_type == "binary":
    students_file = p.get("students").data.strip()
    assignments_file = p.get("assignments").data.strip()
    grades_file = p.get("grades").data.strip()

    repo_student = BinaryRepoStudent(students_file)
    repo_assignment = BinaryRepoAssignment(assignments_file)
    repo_grade = BinaryRepoGrade(grades_file)

service = Services(repo_student, repo_assignment, repo_grade)
ui = UI(service)

ui.main()
