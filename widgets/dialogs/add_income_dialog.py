from PyQt5.QtWidgets import QFormLayout, QLabel, QGridLayout, QWidget, QHBoxLayout, QDialog, QLineEdit, QPushButton

class AddIncomeDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.setWindowTitle("Add Income")
        
        grid_layout = QGridLayout(self)
        self.setLayout(grid_layout)
        form_widget = QWidget()
        grid_layout.addWidget(form_widget, 0, 0, 1, 0)
        
        form_layout = QFormLayout(form_widget)
        form_widget.setLayout(form_layout)

        amount_label = QLabel("$ Amount")
        date_label = QLabel("Date")
        type_label = QLabel("Type")
        
        self.amount_line_text_edit = QLineEdit(form_widget)
        self.amount_line_text_edit.setPlaceholderText("Enter Income Amount")
        self.date_line_text_edit = QLineEdit(form_widget)
        self.date_line_text_edit.setPlaceholderText("Enter Income Date")
        self.type_line_text_edit = QLineEdit(form_widget)
        self.type_line_text_edit.setPlaceholderText("Enter Income Type")
        
        form_layout.addRow(amount_label, self.amount_line_text_edit)
        form_layout.addRow(date_label, self.date_line_text_edit)
        form_layout.addRow(type_label, self.type_line_text_edit)        
        
        accept_button = QPushButton("Accept")
        accept_button.clicked.connect(self.accept)
        grid_layout.addWidget(accept_button, 1, 0)
        
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        grid_layout.addWidget(cancel_button, 1, 1)
        
        
    def get_data(self):
        return {
            '$ Amount': self.amount_line_text_edit.text(),
            'Date': self.date_line_text_edit.text(),
            'Income Type': self.type_line_text_edit.text()
        }