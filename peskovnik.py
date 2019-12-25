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
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QFileDialog
from PyQt5.QtWidgets import QVBoxLayout, QFormLayout

import sys


class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setupUi(self)        
        self.show()

    def setupUi(self, MainWindow):
        # postavi glavni gradnik
        self.centralWidget = QWidget(MainWindow)
        MainWindow.setFixedSize(525, 200)
        # lokacija excel
        lokacijaExcelBtn = QPushButton("Lokacija excel", self.centralWidget)
        lokacijaExcelBtn.setGeometry(40, 19, 100, 24)
        lokacijaExcelLe = QLineEdit(self.centralWidget)
        lokacijaExcelLe.setGeometry(160, 20, 340, 22)


        self.Btn = QPushButton("Odpri dialog", self.centralWidget)
        self.Btn.clicked.connect(self.dialog)
        
        MainWindow.setCentralWidget(self.centralWidget)

    def dialog(self):
        fname = QFileDialog.getExistingDirectory(self, "Select Directory")
        folderPath = fname
        print(folderPath)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    sys.exit(app.exec_())
