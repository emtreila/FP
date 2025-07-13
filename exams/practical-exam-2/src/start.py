from src.repository import TextRepoPlayer
from src.services import Service
from src.ui import UI

repository = TextRepoPlayer()
service = Service(repository)
ui = UI(service)

ui.main()
