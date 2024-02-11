from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from main_window import *

import sys

def main():
    app = QApplication(sys.argv)
    win=CustomMainWindow()    
    win.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()