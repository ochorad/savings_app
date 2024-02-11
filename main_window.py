#import python
import sys
#import widgets
from dashboard_widget import DashboardWidget
from income_widget import IncomeWidget
from expenses_widget import ExpensesWidget
from goals_widget import GoalsWidget
from calendar_widget import CalendarWidget
#import qt stuff
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QStackedWidget, QPushButton, QToolBar, QAction
from PyQt5.QtGui import QFont

class CustomMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_widgets()
        self.create_toolbar()
        
        self.setWindowTitle("Main Window: Savings app")
        self.setGeometry(100,50,1080,800)
        self.setFixedSize(1080,800)

        # stacked widget stuff
        self.central_stacked_widgets = QStackedWidget(self)
        self.setCentralWidget(self.central_stacked_widgets)
        
        
        self.central_stacked_widgets.addWidget(self.dashboard_widget)
        self.central_stacked_widgets.addWidget(self.income_widget)
        self.central_stacked_widgets.addWidget(self.expenses_widget)
        self.central_stacked_widgets.addWidget(self.goals_widget)
        self.central_stacked_widgets.addWidget(self.calendar_widget)
        self.central_stacked_widgets.setCurrentWidget(self.dashboard_widget)

    def create_toolbar(self):
        toolbar = QToolBar()
        toolbar.setFloatable(False)
        toolbar.setMovable(False)
        # add actions 
        dashboard_action = QAction("Dashboard", self)
        income_action = QAction("Income", self)
        expenses_action = QAction("Expenses", self)
        goals_action = QAction("Goals", self)
        calendar_action = QAction("Calendar", self)
        
        # connect actions to slots (show_xxxxxx)
        dashboard_action.triggered.connect(self.show_dashboard)
        income_action.triggered.connect(self.show_income)
        expenses_action.triggered.connect(self.show_expenses)
        goals_action.triggered.connect(self.show_goals)
        calendar_action.triggered.connect(self.show_calendar)
        
        # adding actions to the toolbar
        toolbar.addAction(dashboard_action)
        toolbar.addAction(income_action)
        toolbar.addAction(expenses_action)
        toolbar.addAction(goals_action)
        toolbar.addAction(calendar_action)
        
        toolbar_font = QFont("Arial", 16, 2, False)
        toolbar_font.setBold(True)
        toolbar.setFont(toolbar_font)
        
        self.addToolBar(toolbar)

    def show_dashboard(self):
        self.central_stacked_widgets.setCurrentWidget(self.dashboard_widget)

    def show_income(self):
        self.central_stacked_widgets.setCurrentWidget(self.income_widget)

    def show_expenses(self):
        self.central_stacked_widgets.setCurrentWidget(self.expenses_widget)

    def show_goals(self):
        self.central_stacked_widgets.setCurrentWidget(self.goals_widget)

    def show_calendar(self):
        self.central_stacked_widgets.setCurrentWidget(self.calendar_widget)

    def init_widgets(self):
        self.dashboard_widget = DashboardWidget()
        self.income_widget = IncomeWidget()
        self.expenses_widget = ExpensesWidget()
        self.goals_widget = GoalsWidget()
        self.calendar_widget = CalendarWidget()
        