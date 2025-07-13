from taxi_company.repository import TextMemoRepo
from taxi_company.service import Service
from taxi_company.ui import UI

repository = TextMemoRepo()
service = Service(repository)
ui = UI(service)

ui.main()