from exam.repository import TextMemoRepo
from exam.service import Service
from exam.ui import UI

repository = TextMemoRepo()
service = Service(repository)
ui = UI(service)

ui.main()
