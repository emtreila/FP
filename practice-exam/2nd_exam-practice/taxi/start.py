from repository import TextMemoRepoDriver, TextMemoRepoOrder
from service import Service
from ui import UI

driver_repo = TextMemoRepoDriver()
order_repo = TextMemoRepoOrder()
service = Service(driver_repo, order_repo)
ui = UI(service)

ui.main()