import sys
import random
import sieve
import Queue
from PySide.QtCore import *
from PySide.QtGui import *
from threading import Thread


class Form(QDialog):
    def __init__(self, parent = None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Prime Calculator")
        
        self.lower_bound = QSpinBox()
        self.lower_bound.setRange(1, 1000000)
        
        self.upper_bound = QSpinBox()
        self.upper_bound.setRange(2, 1000000)
        
        self.lower_bound.valueChanged.connect(self.check_spinbox_values)
        self.upper_bound.valueChanged.connect(self.check_spinbox_values)
        
        self.button = QPushButton("Find Primes")
        
        self.layout = QGridLayout()
        self.layout.addWidget(self.lower_bound, 1, 1)
        self.layout.addWidget(self.upper_bound, 1, 2)
        self.layout.addWidget(self.button, 1, 3)
        self.setLayout(self.layout)
        
        self.button.clicked.connect(self.get_primes)
        
    def check_spinbox_values(self):
        if self.lower_bound.value() >= self.upper_bound.value():
            self.lower_bound.setValue(self.upper_bound.value() - 1)

            self.alert = QMessageBox()
            self.alert.setIcon(QMessageBox.Critical)
            self.alert.setText("The lower bound must be less than the upper bound.")
            self.alert.show()

    def get_single_prime(self):
        random_number = random.randint(3, 5000)
        
        if sieve.find_single(random_number) == True:
            print random_number, "is prime!"
        else:
            print random_number, "is not prime."

    def get_primes(self):
        thread_storage = Queue.Queue()
        
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        # self.progress_bar.setRange(self.lower_bound.value(), self.upper_bound.value())
        
        self.layout.addWidget(self.progress_bar, 2, 1, 1, 3)
        self.setLayout(self.layout)
        
        t = Thread(target=sieve.search_range, args=(self.lower_bound.value(), self.upper_bound.value(), self.progress_bar, thread_storage))
        t.start()
        
        #my_primes = thread_storage.get_nowait()
        
        #for item in my_primes:
            #print item
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    form = Form()
    form.show()
    
    sys.exit(app.exec_())