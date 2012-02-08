import sys
import sieve
import Queue
import time
from PySide.QtCore import *
from PySide.QtGui import *
from threading import Thread


class Form(QDialog):
    def __init__(self, parent = None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Prime Calculator")
        
        self.lower_bound = QSpinBox()
        self.lower_bound.setRange(1, 4999999)
        
        self.upper_bound = QSpinBox()
        self.upper_bound.setRange(2, 5000000)
        
        self.lower_bound.valueChanged.connect(self.check_spinbox_values)
        self.upper_bound.valueChanged.connect(self.check_spinbox_values)
        
        self.button = QPushButton("Find Primes")
        
        self.layout = QGridLayout()
        self.layout.addItem(QSpacerItem(20, 200), 1, 1, 3)
        self.layout.addItem(QSpacerItem(30, 10), 1, 2)
        self.layout.addWidget(self.lower_bound, 1, 3)
        self.layout.addWidget(self.upper_bound, 1, 4)
        self.layout.addWidget(self.button, 1, 5)
        self.layout.addItem(QSpacerItem(30, 10), 1, 6)
        self.layout.addItem(QSpacerItem(20, 200), 1, 7, 3)
        
        #self.progress_bar = QProgressBar(self)
        #self.progress_bar.setRange(self.lower_bound.value(), self.upper_bound.value())
        #self.progress_bar.setTextVisible(False)
        
        #self.layout.addWidget(self.progress_bar, 2, 2, 1, 5)
        
        self.text_area = QPlainTextEdit(self)
        
        self.layout.addWidget(self.text_area, 2, 2, 1, 5)
        self.setLayout(self.layout)
        
        self.button.clicked.connect(self.get_primes)
        
    def check_spinbox_values(self):
        if self.lower_bound.value() >= self.upper_bound.value():
            self.lower_bound.setValue(self.upper_bound.value() - 1)

            self.alert = QMessageBox()
            self.alert.setIcon(QMessageBox.Critical)
            self.alert.setText("The lower bound must be less than the upper bound.")
            self.alert.show()

    def get_primes(self):
        self.text_area.clear()
        
        progress_window = QProgressDialog("Searching for prime numbers...", "Abort", self.lower_bound.value(), self.upper_bound.value())
        
        sieve.find_primes_in_range(self.lower_bound.value(), self.upper_bound.value(), progress_window)
        
        #t = Thread(target=sieve.find_primes_in_range, args=(self.lower_bound.value(), self.upper_bound.value(), self))
        #t.start()
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    form = Form()
    form.show()
    
    sys.exit(app.exec_())