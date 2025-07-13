from taxi_simulator.repository import MemoRepo
from taxi_simulator.services import Service
from taxi_simulator.ui import UI

repository = MemoRepo()
service = Service(repository)
ui = UI(service)

ui.main()