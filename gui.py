import sys
import sieve
from PySide.QtCore import *
from PySide.QtGui import *

class window(QMainWindow):
    def __init__(self, parent = None):
        super(window, self).__init__(parent)
        self.setWindowTitle("Prime Calculator")

        # Initialize all of our widgets.
        self.search_box = QGroupBox("Find Primes in a Range")
        
        self.search_button = QPushButton("Begin Search")
        self.search_button.clicked.connect(self.get_primes)
        
        self.lower_bound = QSpinBox()
        self.lower_bound.setRange(1, 4999999)
        self.lower_bound.valueChanged.connect(self.check_spinbox_values)
        
        self.upper_bound = QSpinBox()
        self.upper_bound.setRange(2, 5000000)
        self.upper_bound.valueChanged.connect(self.check_spinbox_values)
        
        self.search_label = QLabel(self)
        self.search_label.setText("Search from:")
        
        self.to_label = QLabel(self)
        self.to_label.setText(" to ")
        
        self.tabs = QTabWidget()
        
        self.search_range_page_layout = QGridLayout()
        
        self.text_area = QPlainTextEdit(self)
        
        self.copy_button = QPushButton("Copy Primes to Clipboard")
        self.copy_button.clicked.connect(self.copy_text_area)
        
        # Create the sub-layout for organizing the search controls
        self.search_box_layout = QGridLayout()
        self.search_box_layout.addWidget(self.search_label, 1, 1)
        self.search_box_layout.addWidget(self.lower_bound, 1, 2)
        self.search_box_layout.addWidget(self.to_label, 1, 3)
        self.search_box_layout.addWidget(self.upper_bound, 1, 4)
        self.search_box_layout.addWidget(self.search_button, 2, 3, 1, 2)
        self.search_box_layout.addWidget(self.text_area, 3, 1, 1, 4)
        self.search_box_layout.addWidget(self.copy_button, 4, 1, 1, 4)
        
        # Finalize the search control area
        self.search_box.setLayout(self.search_box_layout)
        # Add text area before searching?
        # How about the copy button?
        
        self.tabs.addTab(self.search_box, "Search")
        
        self.setCentralWidget(self.tabs)
        
        self.search_button.clicked.connect(self.get_primes)
        
    def check_spinbox_values(self):
        if self.lower_bound.value() >= self.upper_bound.value():
            self.lower_bound.setValue(self.upper_bound.value() - 1)

            self.alert = QMessageBox()
            self.alert.setIcon(QMessageBox.Critical)
            self.alert.setText("The lower bound must be less than the upper bound.")
            self.alert.show()

    def get_primes(self):
        progress_window = QProgressDialog("Searching for prime numbers...", "Abort", self.lower_bound.value(), self.upper_bound.value())
        
        primes = sieve.find_primes_in_range(self.lower_bound.value(), self.upper_bound.value(), progress_window)
        self.text_area.setPlainText(self.output_primes(primes))
    
    def output_primes(self, primes):
        text = ""
        
        for i in xrange(len(primes)):
            text = text + str(primes[i]) + " "
        
        return text        

    def copy_text_area(self):
        self.text_area.selectAll()
        self.text_area.copy()
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = window()
    window.show()
    
    sys.exit(app.exec_())