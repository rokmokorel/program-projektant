############################# HEADER ######################################
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


class Ui_MainWindow():
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
        MainWindow.lokacijaExcelLb = QLabel(
            self.centralWidget, objectName="lokacijaExcelLb")
        MainWindow.lokacijaExcelLb.setGeometry(QRect(40, 20, 90, 20))
        MainWindow.lokacijaExcelLb.setText("Lokacija Excel")
        MainWindow.lokacijaExcelLe = QLineEdit(
            self.centralWidget, objectName="lokacijaExcelLe")
        MainWindow.lokacijaExcelLe.setGeometry(QRect(160, 20, 340, 22))
        # zakljuci zapis
        MainWindow.zakljuciZapisBtn = QPushButton(
            self.centralWidget, objectName="zakljuciZapisBtn")
        MainWindow.zakljuciZapisBtn.setGeometry(QRect(380, 50, 120, 28))
        MainWindow.zakljuciZapisBtn.setText("Zaključi zapis")
        # dodane postavke
        MainWindow.dodanePostavkeLb = QLabel(
            self.centralWidget, objectName="dodanePostavkeLb")
        MainWindow.dodanePostavkeLb.setGeometry(QRect(40, 100, 100, 20))
        MainWindow.dodanePostavkeLb.setText("Dodane postavke")
        MainWindow.dodanePostavkeTb = QTableView(
            self.centralWidget, objectName="dodanePostavkeTb")
        MainWindow.dodanePostavkeTb.setGeometry(QRect(160, 100, 340, 90))
        # skupaj
        MainWindow.skupajLb = QLabel(self.centralWidget, objectName="skupajLb")
        MainWindow.skupajLb.setGeometry(QRect(310, 200, 40, 20))
        MainWindow.skupajLe = QLineEdit(
            self.centralWidget, objectName="skupajLe")
        MainWindow.skupajLe.setGeometry(QRect(380, 200, 120, 22))
        MainWindow.skupajLb.setText("Skupaj")

        # horizontala
        MainWindow.delitev = QFrame(self.centralWidget, objectName="delitev")
        MainWindow.delitev.setGeometry(QRect(7, 230, 513, 20))
        MainWindow.delitev.setFrameShape(QFrame.HLine)
        MainWindow.delitev.setFrameShadow(QFrame.Sunken)
        # dodaj postavke
        MainWindow.dodajPostavkoLb = QLabel(
            self.centralWidget, objectName="dodajPostavkoLb")
        MainWindow.dodajPostavkoLb.setGeometry(QRect(40, 260, 160, 20))
        MainWindow.dodajPostavkoLb.setText("Dodajanje postavke")
        # izberi segment, model, velikost
        MainWindow.izberiSegmentLb = QLabel(self.centralWidget)
        MainWindow.izberiSegmentLb.setGeometry(QRect(40, 290, 90, 20))
        MainWindow.izberiSegmentLb.setText("Izberi model")
        MainWindow.izberiSegmentCb = QComboBox(self.centralWidget)
        MainWindow.izberiSegmentCb.setGeometry(QRect(240, 290, 260, 20))

        MainWindow.izberiModelLb = QLabel(self.centralWidget)
        MainWindow.izberiModelLb.setGeometry(QRect(40, 320, 90, 20))
        MainWindow.izberiModelLb.setText("Izberi model")
        MainWindow.izberiModelCb = QComboBox(self.centralWidget)
        MainWindow.izberiModelCb.setGeometry(QRect(240, 320, 260, 20))

        MainWindow.izberiVelikostLb = QLabel(self.centralWidget)
        MainWindow.izberiVelikostLb.setGeometry(QRect(40, 350, 90, 20))
        MainWindow.izberiVelikostLb.setText("Izberi velikost")
        MainWindow.izberiVelikostCb = QComboBox(self.centralWidget)
        MainWindow.izberiVelikostCb.setGeometry(QRect(240, 350, 260, 20))
        # gumb dodaj
        MainWindow.dodajPostavkoBtn = QPushButton(
            self.centralWidget, objectName="dodajPostavkoBtn")
        MainWindow.dodajPostavkoBtn.setGeometry(QRect(380, 380, 120, 28))
        MainWindow.dodajPostavkoBtn.setText("Dodaj postavko")

        MainWindow.setCentralWidget(self.centralWidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
