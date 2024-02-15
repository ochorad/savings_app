from PyQt5.QtWidgets import QApplication
from main_window import CustomMainWindow

import sys

def main():
    app = QApplication(sys.argv)
    win = CustomMainWindow()    
    win.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()