from PyQt5.QtWidgets import QFormLayout, QLabel, QGridLayout, QWidget, QDateEdit, QDialog, QLineEdit, QPushButton, QDoubleSpinBox
from PyQt5.QtCore import QDate

class AddExpenseDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.setWindowTitle("Add Expense")
        
        grid_layout = QGridLayout(self)
        self.setLayout(grid_layout)
        form_widget = QWidget()
        grid_layout.addWidget(form_widget, 0, 0, 1, 0)
        
        form_layout = QFormLayout(form_widget)
        form_widget.setLayout(form_layout)

        amount_label = QLabel("Expense Amount")
        date_label = QLabel("Expense Date")
        type_label = QLabel("Expense Type")
        
        self.amount_double_spin_box = QDoubleSpinBox(form_widget)
        self.amount_double_spin_box.setPrefix("$ ")
        self.amount_double_spin_box.setRange(0.00, 999999.99)
        self.amount_double_spin_box.setDecimals(2)
        self.amount_double_spin_box.valueChanged.connect(lambda: self.double_spin_box_changed())
        
        self.date_edit = QDateEdit(form_widget)
        current_day = QDate(QDate.currentDate())
        self.date_edit.setDate(current_day)
        self.date_edit.setDateRange(QDate(2000, 1, 1), current_day)
        
        self.type_line_text_edit = QLineEdit(form_widget)
        self.type_line_text_edit.setPlaceholderText("Enter Expense Type")
        self.type_line_text_edit.textChanged.connect(lambda: self.type_line_edit_changed())
        
        form_layout.addRow(amount_label, self.amount_double_spin_box)
        form_layout.addRow(date_label, self.date_edit)
        form_layout.addRow(type_label, self.type_line_text_edit)        
        
        self.accept_button = QPushButton("Accept")
        self.accept_button.clicked.connect(self.accept)
        grid_layout.addWidget(self.accept_button, 1, 0)
        
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        grid_layout.addWidget(cancel_button, 1, 1)
        
        self.check_if_valid()
        
    def check_if_valid(self):
        if self.amount_double_spin_box.value() == 0.00 or self.type_line_text_edit.text() == "":
            self.accept_button.setDisabled(True)
        else:
            self.accept_button.setDisabled(False)
            
    def type_line_edit_changed(self):
        self.check_if_valid()
        
    def double_spin_box_changed(self):
        self.check_if_valid()
        
    def get_data(self):
        return {
            '$ Amount': self.amount_double_spin_box.value(),
            'Date': self.date_edit.date(),
            'Expense Type': self.type_line_text_edit.text()
        }