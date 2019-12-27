############################# MAIN.PY ######################################
#
# main program
# vpis podatkov iz SQLite baze v excel(.xlsx) datoteko
#
# MainWindow - osnovno okolje okoli gradnikov/widgetov
# Widget - gradnik funkcionalnosti
# Layout - prostor, kjer prebivajo gradniki
###########################################################################
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QComboBox, QLabel
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QFileDialog
from PyQt5.QtWidgets import QVBoxLayout, QFormLayout
from PyQt5.QtCore import QRect, QSize

import sys


class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setupUi(self)     
        self.show()
        self.vpisiMoznosti()

    def setupUi(self, MainWindow):
        # postavi glavni gradnik
        self.centralWidget = QWidget(MainWindow)
        MainWindow.setFixedSize(525, 430)
        # lokacija excel
        lokacijaExcelBtn = QPushButton("Lokacija excel", self.centralWidget)
        lokacijaExcelBtn.setGeometry(40, 19, 100, 24)
        lokacijaExcelLe = QLineEdit(self.centralWidget)
        lokacijaExcelLe.setGeometry(160, 20, 340, 22)

        izberiSegmentLb = QLabel(self.centralWidget)
        izberiSegmentLb.setGeometry(QRect(40, 290, 90, 20))
        izberiSegmentLb.setText("Izberi segment")
        self.izberiSegmentCb = QComboBox(self.centralWidget)
        self.izberiSegmentCb.setGeometry(QRect(240, 290, 260, 20))


        izberiModelLb = QLabel(self.centralWidget)
        izberiModelLb.setGeometry(QRect(40, 320, 90, 20))
        izberiModelLb.setText("Izberi model")
        self.izberiModelCb = QComboBox(self.centralWidget)
        self.izberiModelCb.setGeometry(QRect(240, 320, 260, 20))

        izberiVelikostLb = QLabel(self.centralWidget)
        izberiVelikostLb.setGeometry(QRect(40, 350, 90, 20))
        izberiVelikostLb.setText("Izberi velikost")
        self.izberiVelikostCb = QComboBox(self.centralWidget)
        self.izberiVelikostCb.setGeometry(QRect(240, 350, 260, 20))
        
        MainWindow.setCentralWidget(self.centralWidget)

    def vpisiMoznosti(self):
        segmenti = ["residential", "comercial"]
        self.izberiSegmentCb.addItems(segmenti)
        modeli = ["aaaa", "ccc", "abbsbsbbsb"]
        self.izberiModelCb.addItems(modeli)
        velikost = ["1111", "22222", "333333"]
        self.izberiVelikostCb.addItems(velikost)

    def izberiEnote(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    sys.exit(app.exec_())
