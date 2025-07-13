from src.repository import Repo
from src.services import Service
from src.ui import UI

repository = Repo()
service = Service(repository)
ui = UI(service)

ui.main()