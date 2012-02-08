import sys
import sieve
from PySide.QtCore import *
from PySide.QtGui import *

class window(QMainWindow):
    def __init__(self, parent = None):
        super(window, self).__init__(parent)
        self.setWindowTitle("Prime Calculator")
        
        self.tabs = QTabWidget()

        # Organizational boxes for tabs
        self.search_box = QGroupBox("Find Primes in a Range")
        self.verify_box = QGroupBox("Verify a Prime")
        
        # search_box widgets
        self.search_button = QPushButton("Begin Search")
        self.search_button.clicked.connect(self.get_primes)        
        self.search_lower_bound = QSpinBox()
        self.search_lower_bound.setRange(1, 4999999)
        self.search_lower_bound.valueChanged.connect(self.check_spinbox_values)        
        self.search_upper_bound = QSpinBox()
        self.search_upper_bound.setRange(2, 5000000)
        self.search_upper_bound.valueChanged.connect(self.check_spinbox_values)        
        self.search_label = QLabel(self)
        self.search_label.setText("Search from: ")        
        self.search_label2 = QLabel(self)
        self.search_label2.setText("to")        
        self.search_text_area = QPlainTextEdit(self)        
        self.search_copy_button = QPushButton("Copy Primes to Clipboard")
        self.search_copy_button.clicked.connect(self.copy_search_text_area)
        
        # verify_box widgets
        self.verify_label = QLabel(self)
        self.verify_label.setText("Verify that")
        self.verify_number = QSpinBox()
        self.verify_number.setRange(1, 5000000)
        self.verify_label2 = QLabel(self)
        self.verify_label2.setText("is prime.")
        self.verify_button = QPushButton("Verify")
        self.verify_button.clicked.connect(self.verify_prime)
        self.verify_result = QLabel(self)
        
        # search_box layout
        self.search_box_layout = QGridLayout()
        self.search_box_layout.addWidget(self.search_label, 0, 0)
        self.search_box_layout.addWidget(self.search_lower_bound, 0, 1)
        self.search_box_layout.addWidget(self.search_label2, 0, 2, 1, 1, 4)
        self.search_box_layout.addWidget(self.search_upper_bound, 0, 3)
        self.search_box_layout.addWidget(self.search_button, 1, 2, 1, 2)
        self.search_box.setLayout(self.search_box_layout)
        self.search_box_layout.addWidget(self.search_text_area, 2, 0, 1, 4)
        self.search_box_layout.addWidget(self.search_copy_button, 3, 0, 1, 4)
        
        # verify_box layout
        self.verify_box_layout = QGridLayout()
        self.verify_box_layout.addWidget(self.verify_label, 0, 0)
        self.verify_box_layout.addWidget(self.verify_number, 0, 1, 1, 1, 1)
        self.verify_box_layout.addWidget(self.verify_label2, 0, 2)
        self.verify_box_layout.addWidget(self.verify_button, 1, 2)
        self.verify_box_layout.addWidget(self.verify_result, 2, 0, 1, 3, 4)
        self.verify_box.setLayout(self.verify_box_layout)
        
        # Make the tabs
        self.tabs.addTab(self.search_box, "Search")
        self.tabs.setTabToolTip(0, "Search for all prime numbers in a given range.")
        self.tabs.addTab(self.verify_box, "Verify")
        self.tabs.setTabToolTip(1, "Verify that a number is prime.")

        self.setCentralWidget(self.tabs)
        
        self.search_button.clicked.connect(self.get_primes)
        
    def check_spinbox_values(self):
        if self.search_lower_bound.value() >= self.search_upper_bound.value():
            self.search_lower_bound.setValue(self.search_upper_bound.value() - 1)

            self.alert = QMessageBox()
            self.alert.setIcon(QMessageBox.Critical)
            self.alert.setText("The lower bound must be less than the upper bound.")
            self.alert.show()

    def get_primes(self):
        progress_window = QProgressDialog("Searching for prime numbers...", "Abort", self.search_lower_bound.value(), self.search_upper_bound.value())

        primes = sieve.find_primes_in_range(self.search_lower_bound.value(), self.search_upper_bound.value(), progress_window)
        self.search_text_area.setPlainText(self.output_primes(primes))
    
    def output_primes(self, primes):
        text = ""
        
        for i in xrange(len(primes)):
            text = text + str(primes[i]) + " "
        
        return text 

    def copy_search_text_area(self):
        self.search_text_area.selectAll()
        self.search_text_area.copy()
    
    def verify_prime(self):
        progress_window = QProgressDialog("Verifying prime number...", "Abort", 1, self.verify_number.value())
        
        if sieve.is_prime(self.verify_number.value(), progress_window) == True:
            self.verify_result.setText("<p style='font-size: 80px; color: green'><center>PRIME</center></p>")
        else:
            self.verify_result.setText("<p style='font-size: 80px; color: red'><center>NOT<br>PRIME</center></p>")
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = window()
    window.show()
    
    sys.exit(app.exec_())