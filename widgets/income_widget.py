from widgets.dialogs.add_income_dialog import AddIncomeDialog
from PyQt5.QtWidgets import QLabel, QAbstractItemView, QVBoxLayout, QHBoxLayout, QWidget, QTableWidget, QPushButton, QTableWidgetItem, QGridLayout, QSpacerItem, QHeaderView
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class IncomeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.make_table_widget()
        
        h_layout = QHBoxLayout()
        self.setLayout(h_layout)
        v_box_layout_widget = QWidget()
        h_layout.addSpacerItem(QSpacerItem(25,10))
        h_layout.addWidget(v_box_layout_widget)
        h_layout.addSpacerItem(QSpacerItem(25,10))
        
        
        v_layout = QVBoxLayout()
        v_box_layout_widget.setLayout(v_layout)
        
        income_label = QLabel("Income")
        income_label.setFont(QFont("Arial", 25, 2, False))

        v_layout.addWidget(income_label, 0, Qt.AlignmentFlag.AlignCenter)
        v_layout.addWidget(self.table_widget)
        
        push_buttons_widget = QWidget()
        bottom_grid_layout = QGridLayout()
        push_buttons_widget.setLayout(bottom_grid_layout)
        v_layout.addWidget(push_buttons_widget)
        
        add_push_button = QPushButton("Add")
        add_push_button.clicked.connect(self.open_add_income_dialog)
        add_push_button.setFont(QFont("Arial", 16, 2, False))
        remove_push_button = QPushButton("Remove")
        remove_push_button.clicked.connect(self.remove_button_clicked)
        cancel_push_button = QPushButton("Cancel Recurring") #Need to do after calendar is implemented
        
        bottom_grid_layout.addWidget(add_push_button, 0, 0, 0, 1)
        bottom_grid_layout.addWidget(remove_push_button, 0, 1)
        bottom_grid_layout.addWidget(cancel_push_button, 1, 1)
    
    
    def make_table_widget(self):
        self.table_widget = QTableWidget(0,3)
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        
        dollar_amount_column_header = QTableWidgetItem("$ Amount")
        date_column_header = QTableWidgetItem("Date")
        type_column_header = QTableWidgetItem("Income Type")
        self.table_widget.setHorizontalHeaderItem(0, dollar_amount_column_header)
        self.table_widget.setHorizontalHeaderItem(1, date_column_header)
        self.table_widget.setHorizontalHeaderItem(2, type_column_header)
        
        header = self.table_widget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        
        self.table_widget.setSortingEnabled(True)
        self.table_widget.verticalHeader().hide()
    
    def open_add_income_dialog(self):
        income_dialog_box = AddIncomeDialog(self)

        if income_dialog_box.exec_() == 1: # 1=accepted
            print("Accepted")
            data = income_dialog_box.get_data()
            self.update_data_list(data)
        
    def remove_button_clicked(self): 
        self.table_widget.removeRow(self.table_widget.currentRow())
                
    def update_data_list(self, data):
        self.table_widget.setSortingEnabled(False)        
        self.table_widget.setRowCount(self.table_widget.rowCount() + 1)
        print(self.table_widget.rowCount())
        
        amount_item = QTableWidgetItem()
        amount_item.setData(Qt.ItemDataRole.DisplayRole, data['$ Amount'])
        self.table_widget.setItem(self.table_widget.rowCount() - 1, 0, amount_item)
        
        date_item = QTableWidgetItem()
        date_item.setData(Qt.ItemDataRole.DisplayRole, data['Date'])
        self.table_widget.setItem(self.table_widget.rowCount() - 1, 1, date_item)
        
        self.table_widget.setItem(self.table_widget.rowCount() - 1, 2, QTableWidgetItem(str(data['Income Type']), 0))
        self.table_widget.setSortingEnabled(True)

