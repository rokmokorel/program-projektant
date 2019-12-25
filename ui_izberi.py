########################### ui_zacetek.py ####################################
#
# razred zacetnega okna aplikacije
#
# MainWindow - osnovno okolje okoli gradnikov/widgetov
# Widget - gradnik funkcionalnosti
# Layout - prostor, kjer prebivajo gradniki
#############################################################################

from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QFrame, QTableView, QComboBox, QFileDialog
from PyQt5.QtCore import QRect, QSize

class Ui_Izberi(QWidget):
    def setupUi(self, MainWindow):
        # postavi glavni gradnik
        self.centralWidget = QWidget(MainWindow)
        # lokacija excel
        self.lokacijaExcelBtn = QPushButton("Lokacija excel", self.centralWidget)
        self.lokacijaExcelBtn.setGeometry(QRect(40, 19, 100, 24))
        self.lokacijaExcelLe = QLineEdit(self.centralWidget)
        self.lokacijaExcelLe.setGeometry(QRect(160, 20, 340, 22))
        
        # zakljuci zapis
        self.zakljuciZapisBtn = QPushButton(self.centralWidget)
        self.zakljuciZapisBtn.setGeometry(QRect(380, 50, 120, 28))
        self.zakljuciZapisBtn.setText("Zaključi zapis")
        # dodane postavke
        dodanePostavkeLb = QLabel(self.centralWidget)
        dodanePostavkeLb.setGeometry(QRect(40, 100, 100, 20))
        dodanePostavkeLb.setText("Dodane postavke")
        dodanePostavkeTb = QTableView(self.centralWidget)
        dodanePostavkeTb.setGeometry(QRect(160, 100, 340, 90))
        # skupaj
        skupajLb = QLabel(self.centralWidget)
        skupajLb.setGeometry(QRect(310, 200, 40, 20))
        skupajLe = QLineEdit(self.centralWidget)
        skupajLe.setGeometry(QRect(380, 200, 120, 22))
        skupajLb.setText("Skupaj")

        # horizontala
        delitev = QFrame(self.centralWidget)
        delitev.setGeometry(QRect(7, 230, 513, 20))
        delitev.setFrameShape(QFrame.HLine)
        delitev.setFrameShadow(QFrame.Sunken)
        # dodaj postavke
        dodajPostavkoLb = QLabel(self.centralWidget)
        dodajPostavkoLb.setGeometry(QRect(40, 260, 160, 20))
        dodajPostavkoLb.setText("Dodajanje postavke")
        # izberi segment, model, velikost
        izberiSegmentLb = QLabel(self.centralWidget)
        izberiSegmentLb.setGeometry(QRect(40, 290, 90, 20))
        izberiSegmentLb.setText("Izberi segment")
        izberiSegmentCb = QComboBox(self.centralWidget)
        izberiSegmentCb.setGeometry(QRect(240, 290, 260, 20))
        segmenti = ["residential", "comercial"]
        izberiSegmentCb.addItems(segmenti)

        izberiModelLb = QLabel(self.centralWidget)
        izberiModelLb.setGeometry(QRect(40, 320, 90, 20))
        izberiModelLb.setText("Izberi model")
        izberiModelCb = QComboBox(self.centralWidget)
        izberiModelCb.setGeometry(QRect(240, 320, 260, 20))

        izberiVelikostLb = QLabel(self.centralWidget)
        izberiVelikostLb.setGeometry(QRect(40, 350, 90, 20))
        izberiVelikostLb.setText("Izberi velikost")
        izberiVelikostCb = QComboBox(self.centralWidget)
        izberiVelikostCb.setGeometry(QRect(240, 350, 260, 20))

        # gumb dodaj
        dodajPostavkoBtn = QPushButton("Dodaj postavko", self.centralWidget)
        dodajPostavkoBtn.setGeometry(QRect(380, 380, 120, 28))
        MainWindow.setCentralWidget(self.centralWidget)

    def fileDialog(self):
        fname = QFileDialog.getExistingDirectory(self, "Izberi mapo")
        self.lokacijaExcelLe.setText(fname)