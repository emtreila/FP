from src.repository.repository import ExpenseMemoryRepo, ExpenseTextFileRepo, ExpenseBinaryFileRepo
from src.services.services import Services
from src.ui.ui import UI

#repository = ExpenseMemoryRepo()
#repository = ExpenseTextFileRepo()
repository = ExpenseBinaryFileRepo()

service = Services(repository)
ui = UI(service)

ui.main()
