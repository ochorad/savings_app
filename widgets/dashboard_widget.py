from PyQt5.QtWidgets import QLabel, QGridLayout, QWidget, QVBoxLayout, QGroupBox


class DashboardWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.grid_layout = QGridLayout()
        # top left
        self.earnings_top_left_widget = QWidget()
        self.earnings_top_left_layout = QVBoxLayout()
        self.earnings_top_left_widget.setLayout(self.earnings_top_left_layout)
        self.grid_layout.addWidget(self.earnings_top_left_widget, 0, 0)
        self.earnings_group_box = QGroupBox("Earnings")
        self.earnings_top_left_layout.addWidget(self.earnings_group_box)
        # top right
        self.expenses_top_right_widget = QWidget()
        self.expenses_top_right_layout = QVBoxLayout()
        self.expenses_top_right_widget.setLayout(self.expenses_top_right_layout)
        self.grid_layout.addWidget(self.expenses_top_right_widget, 0, 1)
        self.expenses_group_box = QGroupBox("Expenses")
        self.expenses_top_right_layout.addWidget(self.expenses_group_box)
        # bottom left
        self.upcoming_bottom_left_widget = QWidget()
        self.upcoming_bottom_left_layout = QVBoxLayout()
        self.upcoming_bottom_left_widget.setLayout(self.upcoming_bottom_left_layout)
        self.grid_layout.addWidget(self.upcoming_bottom_left_widget, 1, 0)
        self.upcoming_group_box = QGroupBox("Upcoming Earnings and Expenses")
        self.upcoming_bottom_left_layout.addWidget(self.upcoming_group_box)
        # bottom right
        self.goals_bottom_right_widget = QWidget()
        self.goals_bottom_right_layout = QVBoxLayout()
        self.goals_bottom_right_widget.setLayout(self.goals_bottom_right_layout)
        self.grid_layout.addWidget(self.goals_bottom_right_widget, 1, 1)
        self.goals_group_box = QGroupBox("Goals Status")
        self.goals_bottom_right_layout.addWidget(self.goals_group_box)
        
        
        self.setLayout(self.grid_layout)
        
