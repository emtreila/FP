from assignment_checker.repository import TextMemoRepo
from assignment_checker.service import Service
from assignment_checker.ui import UI

repository = TextMemoRepo()
service = Service(repository)
ui = UI(service)

ui.main()