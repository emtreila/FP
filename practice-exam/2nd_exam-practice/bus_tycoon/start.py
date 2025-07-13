from bus_tycoon.repository import TextFileRepoBus, TextFileRepoRoute
from bus_tycoon.ui import UI
from bus_tycoon.services import Service

repo_bus = TextFileRepoBus()
repo_bus_route = TextFileRepoRoute()
service = Service(repo_bus, repo_bus_route)
ui = UI(service)

ui.main()