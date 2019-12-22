############################# MAIN.PY ######################################
#
# main program
# vpis podatkov iz SQLite baze v excel(.xlsx) datoteko
#
# MainWindow - osnovno okolje okoli gradnikov/widgetov
# Widget - gradnik funkcionalnosti
# Layout - prostor, kjer prebivajo gradniki
###########################################################################

from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QPushButton, QLineEdit, QLabel, QFrame, QTableView, QComboBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QRect

# from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Ui_Zacetek():
    def setupUi(self, MainWindow):
        pass

class Ui_Izberi():
    def setupUi(self, MainWindow):
        # nastavitev fonta, ikone, velikosti okna, naslova
        MainWindow.setWindowTitle("Projektantski popis")
        MainWindow.resize(525, 430)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        app_icon = QIcon('logo/logo2_256.ico')
        MainWindow.setWindowIcon(app_icon)

        # postavi glavni gradnik
        self.centralWidget = QWidget(MainWindow, objectName="centralwidget")

        # lokacija excel
        self.lokacijaExcelLb = QLabel(
            self.centralWidget, objectName="lokacijaExcelLb")
        self.lokacijaExcelLb.setGeometry(QRect(40, 20, 90, 20))
        self.lokacijaExcelLb.setText("Lokacija Excel")
        self.lokacijaExcelLe = QLineEdit(
            self.centralWidget, objectName="lokacijaExcelLe")
        self.lokacijaExcelLe.setGeometry(QRect(160, 20, 340, 22))
        # zakljuci zapis
        self.zakljuciZapisBtn = QPushButton(
            self.centralWidget, objectName="zakljuciZapisBtn")
        self.zakljuciZapisBtn.setGeometry(QRect(380, 50, 120, 28))
        self.zakljuciZapisBtn.setText("Zaključi zapis")
        # dodane postavke
        self.dodanePostavkeLb = QLabel(
            self.centralWidget, objectName="dodanePostavkeLb")
        self.dodanePostavkeLb.setGeometry(QRect(40, 100, 100, 20))
        self.dodanePostavkeLb.setText("Dodane postavke")
        self.dodanePostavkeTb = QTableView(
            self.centralWidget, objectName="dodanePostavkeTb")
        self.dodanePostavkeTb.setGeometry(QRect(160, 100, 340, 90))
        # skupaj
        self.skupajLb = QLabel(self.centralWidget, objectName="skupajLb")
        self.skupajLb.setGeometry(QRect(310, 200, 40, 20))
        self.skupajLe = QLineEdit(
            self.centralWidget, objectName="skupajLe")
        self.skupajLe.setGeometry(QRect(380, 200, 120, 22))
        self.skupajLb.setText("Skupaj")

        # horizontala
        self.delitev = QFrame(self.centralWidget, objectName="delitev")
        self.delitev.setGeometry(QRect(7, 230, 513, 20))
        self.delitev.setFrameShape(QFrame.HLine)
        self.delitev.setFrameShadow(QFrame.Sunken)
        # dodaj postavke
        self.dodajPostavkoLb = QLabel(
            self.centralWidget, objectName="dodajPostavkoLb")
        self.dodajPostavkoLb.setGeometry(QRect(40, 260, 160, 20))
        self.dodajPostavkoLb.setText("Dodajanje postavke")
        # izberi segment, model, velikost
        self.izberiSegmentLb = QLabel(self.centralWidget)
        self.izberiSegmentLb.setGeometry(QRect(40, 290, 90, 20))
        self.izberiSegmentLb.setText("Izberi model")
        self.izberiSegmentCb = QComboBox(self.centralWidget)
        self.izberiSegmentCb.setGeometry(QRect(240, 290, 260, 20))

        self.izberiModelLb = QLabel(self.centralWidget)
        self.izberiModelLb.setGeometry(QRect(40, 320, 90, 20))
        self.izberiModelLb.setText("Izberi model")
        self.izberiModelCb = QComboBox(self.centralWidget)
        self.izberiModelCb.setGeometry(QRect(240, 320, 260, 20))

        self.izberiVelikostLb = QLabel(self.centralWidget)
        self.izberiVelikostLb.setGeometry(QRect(40, 350, 90, 20))
        self.izberiVelikostLb.setText("Izberi velikost")
        self.izberiVelikostCb = QComboBox(self.centralWidget)
        self.izberiVelikostCb.setGeometry(QRect(240, 350, 260, 20))
        
        # gumb dodaj
        self.dodajPostavkoBtn = QPushButton(
            self.centralWidget, objectName="dodajPostavkoBtn")
        self.dodajPostavkoBtn.setGeometry(QRect(380, 380, 120, 28))
        self.dodajPostavkoBtn.setText("Dodaj postavko")

        MainWindow.setCentralWidget(self.centralWidget)

class Ui_Koncaj():
    def setupUi(self, MainWindow):
        pass


class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        # self.uiZacetek = Ui_Zacetek()
        self.uiOkno = Ui_Izberi()
        self.show()
        
        self.uiOkno.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    sys.exit(app.exec_())
