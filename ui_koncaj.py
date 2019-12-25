########################### ui_koncaj.py ####################################
#
# razred zakljucnega okna aplikacije
#
# MainWindow - osnovno okolje okoli gradnikov/widgetov
# Widget - gradnik funkcionalnosti
# Layout - prostor, kjer prebivajo gradniki
#############################################################################

from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QPushButton, QLineEdit, QLabel, QFrame, QTableView, QComboBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QRect, QSize

class Ui_Koncaj():
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(QSize(525, 430))
        self.centralWidget = QWidget(MainWindow)
        self.naZacetekBtn = QPushButton("Na začetek", self.centralWidget)

        MainWindow.setCentralWidget(self.centralWidget)
