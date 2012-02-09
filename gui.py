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
        self.scan_box = QGroupBox("Find All Primes in a Range")
        self.verify_box = QGroupBox("Verify that a Number is Prime")
        self.find_box = QGroupBox("Find a Number of Primes")
        
        # scan_box widgets
        self.scan_button = QPushButton("Begin Search")
        self.scan_button.clicked.connect(self.scan_primes)
        self.scan_lower_bound = QSpinBox()
        self.scan_lower_bound.setRange(1, 1999999)
        self.scan_lower_bound.valueChanged.connect(self.check_scan_spinbox_values)        
        self.scan_upper_bound = QSpinBox()
        self.scan_upper_bound.setRange(2, 2000000)
        self.scan_upper_bound.valueChanged.connect(self.check_scan_spinbox_values)        
        self.scan_label = QLabel(self)
        self.scan_label.setText("Search from")        
        self.scan_label2 = QLabel(self)
        self.scan_label2.setText("to")        
        self.scan_text_area = QPlainTextEdit(self)        
        self.scan_copy_button = QPushButton("Copy Primes to Clipboard")
        self.scan_copy_button.clicked.connect(self.copy_scan_text_area)
        
        # verify_box widgets
        self.verify_label = QLabel(self)
        self.verify_label.setText("Verify that")
        self.verify_number = QSpinBox()
        self.verify_number.setRange(1, 2000000)
        self.verify_label2 = QLabel(self)
        self.verify_label2.setText("is prime.")
        self.verify_button = QPushButton("Verify")
        self.verify_button.clicked.connect(self.verify_prime)
        self.verify_result = QLabel(self)
        
        # find_box widgets
        self.find_button = QPushButton("Begin Search")
        self.find_button.clicked.connect(self.find_primes)        
        self.find_quantity = QSpinBox()
        self.find_quantity.setRange(1, 25000)
        self.find_quantity.valueChanged.connect(self.check_find_spinbox_values)   
        self.find_lower_bound = QSpinBox()
        self.find_lower_bound.setRange(1, 1500000) 
        self.find_label = QLabel(self)
        self.find_label.setText("Find")        
        self.find_label2 = QLabel(self)
        self.find_label2.setText("prime from")        
        self.find_text_area = QPlainTextEdit(self)        
        self.find_copy_button = QPushButton("Copy Primes to Clipboard")
        self.find_copy_button.clicked.connect(self.copy_scan_text_area)
        
        # scan_box layout
        self.scan_box_layout = QGridLayout()
        self.scan_box_layout.addWidget(self.scan_label, 0, 0)
        self.scan_box_layout.addWidget(self.scan_lower_bound, 0, 1)
        self.scan_box_layout.addWidget(self.scan_label2, 0, 2, 1, 1, 4)
        self.scan_box_layout.addWidget(self.scan_upper_bound, 0, 3)
        self.scan_box_layout.addWidget(self.scan_button, 1, 2, 1, 2)
        self.scan_box.setLayout(self.scan_box_layout)
        self.scan_box_layout.addWidget(self.scan_text_area, 2, 0, 1, 4)
        self.scan_box_layout.addWidget(self.scan_copy_button, 3, 0, 1, 4)
        
        # verify_box layout
        self.verify_box_layout = QGridLayout()
        self.verify_box_layout.addWidget(self.verify_label, 0, 0)
        self.verify_box_layout.addWidget(self.verify_number, 0, 1, 1, 1, 1)
        self.verify_box_layout.addWidget(self.verify_label2, 0, 2)
        self.verify_box_layout.addWidget(self.verify_button, 1, 2)
        self.verify_box_layout.addWidget(self.verify_result, 2, 0, 1, 3, 4)
        self.verify_box.setLayout(self.verify_box_layout)
        
        # find_box layout
        self.find_box_layout = QGridLayout()
        self.find_box_layout.addWidget(self.find_label, 0, 0)
        self.find_box_layout.addWidget(self.find_quantity, 0, 1)
        self.find_box_layout.addWidget(self.find_label2, 0, 2, 1, 1, 4)
        self.find_box_layout.addWidget(self.find_lower_bound, 0, 3)
        self.find_box_layout.addWidget(self.find_button, 1, 2, 1, 2)
        self.find_box.setLayout(self.find_box_layout)
        self.find_box_layout.addWidget(self.find_text_area, 2, 0, 1, 4)
        self.find_box_layout.addWidget(self.find_copy_button, 3, 0, 1, 4)
        
        # Make the tabs
        self.tabs.addTab(self.scan_box, "Scan Range")
        self.tabs.setTabToolTip(0, "Scan a specified range for prime numbers.")        
        self.tabs.addTab(self.find_box, "Find Primes")
        self.tabs.setTabToolTip(1, "Find a number of primes starting from a specified number.")
        self.tabs.addTab(self.verify_box, "Verify")
        self.tabs.setTabToolTip(2, "Verify that a number is prime.")

        self.setCentralWidget(self.tabs)
        
    def check_scan_spinbox_values(self):
        if self.scan_lower_bound.value() >= self.scan_upper_bound.value():
            self.scan_lower_bound.setValue(self.scan_upper_bound.value() - 1)

            self.alert = QMessageBox()
            self.alert.setIcon(QMessageBox.Critical)
            self.alert.setText("The lower bound must be less than the upper bound.")
            self.alert.show()
    
    def check_find_spinbox_values(self):
        if self.find_quantity.value() > 1:
            self.find_label2.setText("primes from")
        else:
            self.find_label2.setText("prime from")

    def scan_primes(self):
        self.progress_window = QProgressDialog("Searching the specified range...", "Abort", self.scan_lower_bound.value(), self.scan_upper_bound.value())
        self.progress_window.setWindowTitle("Searching...")
        
        primes = sieve.find_primes_in_range(self.scan_lower_bound.value(), self.scan_upper_bound.value(), self.progress_window)
        
        self.scan_text_area.setPlainText(self.output_primes(primes))
    
    def find_primes(self):
        if self.find_quantity.value() == 1:
            progress_string = "Finding the first prime starting from " + str(self.find_lower_bound.value() + "...")
        else:
            progress_string = "Finding the first " + str(self.find_quantity.value()) + " primes starting from " + str(self.find_lower_bound.value()) + "..."
        
        self.progress_window = QProgressDialog(progress_string, "Abort", 1, self.find_quantity.value())
        self.progress_window.setWindowTitle("Searching...")
        
        primes = sieve.find_x_primes(self.find_lower_bound.value(), self.find_quantity.value(), self.progress_window)
        
        self.find_text_area.setPlainText(self.output_primes(primes))
    
    def output_primes(self, primes):
        text = ""
        
        for i in xrange(len(primes)):
            text = text + str(primes[i]) + " "
        
        return text

    def copy_scan_text_area(self):
        self.scan_text_area.selectAll()
        self.scan_text_area.copy()
    
    def verify_prime(self):
        self.progress_window = QProgressDialog("Verifying prime number...", "Abort", 1, self.verify_number.value())
        self.progress_window.setWindowTitle("Verifying...")
        
        if sieve.is_prime(self.verify_number.value(), self.progress_window) == True:
            self.verify_result.setText("<p style='font-size: 80px; color: green'><center>PRIME</center></p>")
        else:
            self.verify_result.setText("<p style='font-size: 80px; color: red'><center>NOT<br>PRIME</center></p>")
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = window()
    window.show()
    
    sys.exit(app.exec_())