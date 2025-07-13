from petite_slam.repository import TextRepoPlayer
from petite_slam.services import Service
from petite_slam.ui import UI

repository = TextRepoPlayer()
service = Service(repository)
ui = UI(service)

ui.main()